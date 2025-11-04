# 🎨 AI Poster Generator

Generate stunning, professional posters using AI-powered image generation. This Python tool leverages Stability AI's SDXL model to create custom posters with text overlays for events, movies, motivation, and more.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🤖 **AI-Powered Image Generation** - Uses Stability AI's Stable Diffusion XL model
- 🎯 **Smart Text Overlays** - Automatically adds titles and subtitles with custom positioning
- 🎨 **Customizable Design** - Control dimensions, text placement, and styling
- 💾 **High-Quality Output** - Saves posters as high-resolution PNG files
- 🚀 **Easy to Use** - Simple API with sensible defaults

## 📋 Requirements

- Python 3.8 or higher
- Stability AI API key ([Get one here](https://platform.stability.ai))

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ai-poster-generator.git
cd ai-poster-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export STABILITY_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
STABILITY_API_KEY=your-api-key-here
```

## 📦 Dependencies

```
stability-sdk
pillow
requests
```

## 💻 Usage

### Basic Example

```python
from ai_poster_generator import AIPosterGenerator

# Initialize the generator
generator = AIPosterGenerator()

# Create a poster
poster, path = generator.create_poster(
    prompt="vibrant music festival at sunset, colorful lights, crowd silhouettes",
    title="SUMMER MUSIC FEST",
    subtitle="July 15-17, 2024",
    width=1024,
    height=1536
)

print(f"Poster saved to: {path}")
```

### Advanced Usage

```python
# Custom positioning and dimensions
poster, path = generator.create_poster(
    prompt="futuristic cyberpunk city, neon lights, rainy streets",
    title="NEON DREAMS",
    subtitle="Coming Soon",
    width=768,
    height=1152,
    text_position="top",  # Options: "top", "bottom", "center"
    output_path="my_custom_poster.png"
)
```

### Generate Image Only

```python
# Generate image without text overlay
image = generator.generate_image(
    prompt="majestic mountain landscape at golden hour",
    width=1024,
    height=1024
)
image.save("landscape.png")
```

### Add Text to Existing Image

```python
from PIL import Image

# Load existing image
image = Image.open("your_image.png")

# Add text overlay
poster = generator.add_text_overlay(
    image,
    title="YOUR TITLE",
    subtitle="Your subtitle",
    position="bottom"
)
poster.save("poster_with_text.png")
```

## 🎯 Example Prompts

**Event Poster:**
```
"vibrant music festival scene at sunset, crowd silhouettes, colorful stage lights, energetic atmosphere, professional photography"
```

**Movie Poster:**
```
"futuristic cyberpunk city at night, neon lights, flying cars, rainy streets, blade runner style, cinematic"
```

**Motivational Poster:**
```
"majestic mountain peak at dawn, golden light, inspiring landscape, ultra realistic, cinematic"
```

**Product Launch:**
```
"minimalist product photography, sleek modern design, gradient background, studio lighting, professional"
```

## 🎨 Poster Examples

| Event Poster | Movie Poster | Motivational Poster |
|--------------|--------------|---------------------|
| ![Event](examples/event.png) | ![Movie](examples/movie.png) | ![Motivation](examples/motivation.png) |

## ⚙️ Configuration

### Poster Dimensions

Common poster sizes:
- **Standard Poster**: 1024 x 1536 (2:3 ratio)
- **Movie Poster**: 768 x 1152 (2:3 ratio)
- **Square Poster**: 1024 x 1024 (1:1 ratio)
- **Wide Banner**: 1536 x 768 (2:1 ratio)

### Text Positioning

- `"bottom"` - Text at bottom with dark overlay
- `"top"` - Text at top with dark overlay
- `"center"` - Text centered on image

## 📊 API Costs

Stability AI charges per image generation. Check their [pricing page](https://platform.stability.ai/pricing) for current rates. Typical costs:
- SDXL 1.0: ~$0.02 per image (1024x1024)

## 🛠️ Troubleshooting

**API Key Error:**
```
ValueError: API key required
```
Solution: Set your `STABILITY_API_KEY` environment variable or pass it to the constructor.

**Font Not Found:**
The script will fall back to default fonts if Arial isn't available. For better results, install custom fonts or specify font paths.

**Rate Limiting:**
If you hit rate limits, add delays between requests:
```python
import time
time.sleep(2)  # Wait 2 seconds between generations
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stability AI](https://stability.ai/) for the image generation API
- [Pillow](https://python-pillow.org/) for image processing

## 🔮 Roadmap

- [ ] Support for multiple AI providers (OpenAI DALL-E, Midjourney)
- [ ] Custom font support
- [ ] Batch poster generation
- [ ] Web interface
- [ ] Template system
- [ ] Image filters and effects
- [ ] QR code integration

---

⭐ If you find this project helpful, please give it a star!
