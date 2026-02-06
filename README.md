# 🎨 Emoji2Pixel

Transform emojis and images into beautiful pixel art with this powerful web-based converter. Create stunning animations, customize every detail, and export your creations as images or GIFs.

![Emoji2Pixel Banner](https://img.shields.io/badge/Emoji2Pixel-v1.0-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Languages](https://img.shields.io/badge/languages-8-orange)

## ✨ Features

### 🖼️ **Multi-Source Input**
- **Emoji Support**: Input emojis directly or browse from a comprehensive emoji library
- **Image Import**: Upload any image file for pixelation
- **Auto-Fit Mode**: Automatically adjust emoji scale to fit perfectly in the canvas
- **Search & Filter**: Quick emoji search with category navigation

### 🎬 **Animation System**
- **Keyframe Animation**: Create smooth animations with multiple keyframes
- **Tween Interpolation**: Automatic generation of transition frames between keyframes
- **Playback Controls**: Play, pause, and adjust animation speed in real-time
- **GIF Export**: Export animations as animated GIF files

### 🎛️ **Advanced Transform Controls**
- **Scale**: Resize your artwork from 0% to 200%
- **Position**: Fine-tune X/Y offset for perfect alignment
- **Rotation**: Rotate in any direction (0-360°)
- **Interactive Canvas**: Direct manipulation with click & drag + Hold Shift to rotate

### 🎨 **Powerful Rendering Engine**
- **Dual Render Modes**:
  - **Ideal Mode**: Professional pixel art with customizable gaps and borders
  - **Bare Mode**: Pure pixel rendering for authentic retro style
- **Flexible Canvas**: Adjustable grid size (8x8 to 128x128 pixels)
- **Pixel Styles**: Choose from square, rounded, or circular pixels
- **Color Quantization**: Reduce color palette to 2-256 colors for retro aesthetics
- **Sharpening Filters**: Enhance edge definition with adjustable strength

### 🖌️ **Editing Tools**
- **Background Removal**: Intelligent background removal with tolerance control
- **Selection Tools**: Rectangular selection with fill, erase, copy & paste
- **Layer System**: Non-destructive editing workflow
- **Undo Support**: Revert color picking and background removal operations

### 📏 **Professional Export Options**
- **Multiple Units**: Work in millimeters, inches, or grid units
- **Size Presets**: Quick presets for common display sizes
- **Export Formats**:
  - PNG (with transparency)
  - GIF (animated or static)
  - Raw pixel data
- **Frame Rendering**: Visualize physical pixel layout with real-world dimensions

### 🌍 **International Support**
Built-in translations for 8 languages:
- 🇨🇳 简体中文 (Simplified Chinese)
- 🇺🇸 English
- 🇫🇷 Français (French)
- 🇩🇪 Deutsch (German)
- 🇮🇹 Italiano (Italian)
- 🇯🇵 日本語 (Japanese)
- 🇰🇷 한국어 (Korean)
- 🇪🇸 Español (Spanish)

## 🚀 Quick Start

### Online Demo
Visit the live demo at: [Your Demo URL]

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emoji2pixel.git
   cd emoji2pixel
   ```

2. **Serve locally**
   
   Using Python:
   ```bash
   python -m http.server 8000
   ```
   
   Or using Node.js:
   ```bash
   npx http-server -p 8000
   ```

3. **Open in browser**
   ```
   http://localhost:8000
   ```

No build process required! This is a pure static web application.

## 📖 Usage Guide

### Basic Workflow

1. **Input**: Enter an emoji or upload an image
2. **Transform**: Adjust scale, position, and rotation to your liking
3. **Add Frame**: Click the `+` button to add to your animation
4. **Customize**: Tweak render settings, pixel style, and colors
5. **Export**: Download as PNG or GIF

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Space` | Toggle animation playback |
| `Enter` | Add current view as keyframe |
| `Delete` / `Backspace` | Delete selected frame |
| `←` / `→` | Navigate between frames |
| `Esc` | Cancel selection/color picking |
| `Ctrl/Cmd + C` | Copy selection |
| `Ctrl/Cmd + V` | Paste selection |

### Pro Tips

- 🎯 **Hold Shift** while dragging on canvas to rotate instead of moving
- 🔍 Use **Color Quantization** (8-64 colors) for authentic retro pixel art
- ⚡ Enable **Sharpening** (30-50% strength) to enhance edge clarity
- 🎬 Set **Tween Frames** to 5-10 for smooth animations
- 📐 Use **Frame Render Mode** to visualize physical LED matrix layouts

## 🛠️ Technical Stack

- **Pure Frontend**: HTML5, CSS3, Vanilla JavaScript
- **No Dependencies**: Zero external libraries or frameworks
- **Canvas API**: High-performance pixel manipulation
- **GIF.js**: Client-side GIF encoding
- **Responsive Design**: Works on desktop and tablet devices

## 📁 Project Structure

```
emoji2pixel/
├── index.html          # Main HTML structure
├── app.js              # Core application logic
├── styles.css          # Styling and layout
├── locales/            # Internationalization
│   ├── index.json      # Locale manifest
│   ├── en-US.json      # English translations
│   ├── zh-CN.json      # Chinese translations
│   └── ...             # Other languages
└── scripts/            # Build utilities
    └── generate_locales_index.py
```

## 🌐 Adding New Languages

1. Create a new locale file in `locales/` (e.g., `pt-BR.json`)
2. Copy the structure from an existing locale file
3. Translate all keys to your target language
4. Add a `selfName` field with a flag emoji
5. Run the locale index generator:
   ```bash
   python scripts/generate_locales_index.py
   ```

The new language will automatically appear in the language selector!

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🌍 Add or improve translations
- 📝 Improve documentation
- 🎨 Submit pixel art showcases

### Development Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Emoji data sourced from Unicode standards
- Inspired by classic pixel art tools and LED matrix displays
- Built with ❤️ for the pixel art community

## 📮 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/emoji2pixel/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/emoji2pixel/discussions)

---

<div align="center">

**Made with 🎨 and ⌨️**

If you find this project useful, please consider giving it a ⭐!

</div>
