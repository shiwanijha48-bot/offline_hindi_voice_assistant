# 🎙️ Offline Hindi Voice Assistant

A lightweight, Python-based **offline voice assistant** that understands and responds in **Hindi**. Designed to work without continuous internet connectivity, the assistant leverages speech recognition and text-to-speech technologies to execute voice commands such as opening applications, performing searches, announcing the current time, and more.

This project demonstrates the integration of **Hindi speech recognition**, **natural voice interaction**, and **offline AI capabilities**, making voice technology more accessible to Hindi-speaking users.

---

## ✨ Features

* 🎤 Recognizes and processes **Hindi voice commands**
* 🗣️ Responds with **Hindi text-to-speech output**
* 🌐 Performs Google searches
* 🔗 Opens websites and desktop applications
* 🕒 Announces the current date and time
* 🎵 Plays music on command
* 📶 Works primarily **offline** using the Vosk speech recognition model
* 💻 Simple and lightweight implementation using Python

---

## 🛠️ Tech Stack

| Category             | Technologies        |
| -------------------- | ------------------- |
| Programming Language | Python 3            |
| Speech Recognition   | Vosk                |
| Text-to-Speech       | pyttsx3 / eSpeak NG |
| Audio Input          | SpeechRecognition   |
| Web Automation       | pywhatkit           |
| Operating System     | Windows/Linux       |

---

## 📂 Project Structure

```text
offline-hindi-voice-assistant/
│
├── vosk-model-small-hi-0.22/    # Hindi speech recognition model
├── hindi_assistant.py           # Main application
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shiwanijha48-bot/offline_hindi_voice_assistant.git
cd offline_hindi_voice_assistant
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install the packages manually:

```bash
pip install SpeechRecognition pyttsx3 vosk pywhatkit pyaudio
```

---

## ▶️ Usage

Run the assistant using:

```bash
python hindi_assistant.py
```

Once started, speak your commands in Hindi.

### Example Commands

* "गूगल पर मौसम खोजो"
* "समय बताओ"
* "यूट्यूब खोलो"
* "संगीत चलाओ"
* "आज की तारीख बताओ"

---

## 📦 Dependencies

* Python 3.11+
* SpeechRecognition
* Vosk
* pyttsx3
* eSpeak NG
* pywhatkit (optional)
* PyAudio

---

## 🚀 Future Enhancements

* Add support for more Hindi conversational commands
* Integrate local large language models (LLMs)
* Offline note-taking and reminders
* WhatsApp and email automation
* Multi-language support
* GUI/Desktop interface

---

## 🎯 Use Cases

* Hands-free desktop assistance
* Accessibility support for Hindi speakers
* Educational projects on speech technologies
* Demonstrating offline AI applications
* Learning speech recognition and text-to-speech systems

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request


---

### Building accessible voice technology for Hindi speakers through offline AI. 🇮🇳🎙️
