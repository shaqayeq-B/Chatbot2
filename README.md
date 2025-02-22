```markdown
# 🗣️ Voice Dictionary with Auto-Learning

A smart voice-controlled dictionary that learns new words through conversation!

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)
[![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10.0-green)](https://pypi.org/project/SpeechRecognition/)

## 🌟 Cool Features
- 🎤 Voice-controlled interface (Persian)
- 🤖 Automatic word learning - teaches itself new words
- 💾 Saves learned words between sessions
- 🔊 Text-to-speech responses
- 📁 JSON storage for easy management

## 🚀 Quick Start
1. Install requirements:
```bash
pip install SpeechRecognition gtts pyaudio
```

2. Run the magic:
```bash
python smart_dictionary.py
```

3. Start talking! Try:
- "سلام" (Hello)
- "ماشین یادگیری" (Say an unknown word to teach it)

## How It Learns
When you say an unknown word:
1. Bot asks: "I don't know this word. Please define it"
2. Speak your definition
3. Saves it forever in dictionary.json
4. Now knows your word! 🎉

## 🛠️ Tech Stack
- Python 3.7+
- SpeechRecognition library
- Google Text-to-Speech (gTTS)
- JSON data storage

## 🤝 Want to Help?
- Add more starter words
- Improve voice recognition accuracy
- Create a GUI version
- Add multi-language support

```bash
# For contributors
git clone https://github.com/yourusername/smart-voice-dictionary.git
```

## ⚠️ Heads Up
- Needs internet connection
- Works best with quiet environments
- First run creates dictionary.json

Made with ❤️ - Give it a star if you love talking dictionaries! ⭐
```
