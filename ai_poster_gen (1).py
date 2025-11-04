"""
AI Poster Generator using Stability AI and Pillow
Requires: pip install stability-sdk pillow requests
"""

import os
import io
import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class AIPosterGenerator:
    def __init__(self, api_key=None):
        """Initialize with Stability AI API key"""
        self.api_key = api_key or os.environ.get('STABILITY_API_KEY')
        self.api_host = 'https://api.stability.ai'
        
    def generate_image(self, prompt, width=1024, height=1024):
        """Generate image using Stability AI"""
        if not self.api_key:
            raise ValueError("API key required. Set STABILITY_API_KEY env variable or pass to constructor")
        
        url = f"{self.api_host}/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "text_prompts": [{"text": prompt, "weight": 1}],
            "cfg_scale": 7,
            "height": height,
            "width": width,
            "samples": 1,
            "steps": 30,
        }
        
        print(f"Generating image with prompt: {prompt}")
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
        
        data = response.json()
        
        # Decode base64 image
        import base64
        image_data = base64.b64decode(data["artifacts"][0]["base64"])
        image = Image.open(io.BytesIO(image_data))
        
        return image
    
    def add_text_overlay(self, image, title, subtitle="", position="bottom"):
        """Add text overlay to image"""
        img = image.copy()
        draw = ImageDraw.Draw(img)
        width, height = img.size
        
        # Try to load a nice font, fallback to default
        try:
            title_font = ImageFont.truetype("arial.ttf", 80)
            subtitle_font = ImageFont.truetype("arial.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Calculate text position
        if position == "bottom":
            y_offset = height - 200
        elif position == "top":
            y_offset = 100
        else:
            y_offset = height // 2
        
        # Add semi-transparent background for text
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        if position == "bottom":
            overlay_draw.rectangle([(0, height-250), (width, height)], fill=(0, 0, 0, 180))
        else:
            overlay_draw.rectangle([(0, 0), (width, 250)], fill=(0, 0, 0, 180))
        
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
        draw = ImageDraw.Draw(img)
        
        # Draw title
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, y_offset), title, font=title_font, fill="white")
        
        # Draw subtitle if provided
        if subtitle:
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            subtitle_x = (width - subtitle_width) // 2
            draw.text((subtitle_x, y_offset + 90), subtitle, font=subtitle_font, fill="white")
        
        return img.convert('RGB')
    
    def create_poster(self, prompt, title, subtitle="", width=1024, height=1536, 
                     text_position="bottom", output_path=None):
        """Complete poster creation workflow"""
        # Generate base image
        image = self.generate_image(prompt, width, height)
        
        # Add text overlay
        poster = self.add_text_overlay(image, title, subtitle, text_position)
        
        # Save poster
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"poster_{timestamp}.png"
        
        poster.save(output_path, quality=95)
        print(f"Poster saved to: {output_path}")
        
        return poster, output_path


# Example usage
if __name__ == "__main__":
    # Initialize generator (set your API key as environment variable or pass directly)
    generator = AIPosterGenerator()
    
    # Example 1: Event poster
    try:
        poster, path = generator.create_poster(
            prompt="vibrant music festival scene at sunset, crowd silhouettes, colorful stage lights, energetic atmosphere, professional photography",
            title="SUMMER MUSIC FEST",
            subtitle="July 15-17, 2024",
            width=1024,
            height=1536,
            text_position="bottom"
        )
        print("✓ Event poster created!")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Motivational poster
    try:
        poster, path = generator.create_poster(
            prompt="majestic mountain peak at dawn, golden light, inspiring landscape, ultra realistic, cinematic",
            title="REACH NEW HEIGHTS",
            subtitle="Believe in Yourself",
            width=1024,
            height=1536,
            text_position="top"
        )
        print("✓ Motivational poster created!")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Movie-style poster
    try:
        poster, path = generator.create_poster(
            prompt="futuristic cyberpunk city at night, neon lights, flying cars, rainy streets, blade runner style, cinematic",
            title="NEON DREAMS",
            subtitle="Coming Soon",
            width=768,
            height=1152,
            text_position="bottom"
        )
        print("✓ Movie poster created!")
    except Exception as e:
        print(f"Error: {e}")