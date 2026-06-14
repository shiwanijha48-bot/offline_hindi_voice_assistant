# 🎙️ Offline Hindi Voice Assistant

A simple **offline Hindi voice assistant** built using Python and the Vosk speech recognition toolkit. The assistant listens to Hindi voice commands through the microphone and responds using text-to-speech without requiring an active internet connection.

This project demonstrates how offline speech recognition and voice interaction can be implemented for Hindi language applications.

---

## ✨ Features

* 🎤 Recognizes Hindi voice commands offline
* 🗣️ Responds using text-to-speech
* 📶 Works without internet connectivity
* 🕒 Tells the current time and date
* 📅 Announces the current year and day
* 😄 Responds to greetings and basic conversations
* 😂 Tells a simple joke
* 🔁 Repeats the previous response
* 👋 Supports exit commands to close the assistant

---

## 🛠️ Technologies Used

* **Python 3**
* **Vosk** – Offline Hindi speech recognition
* **SoundDevice** – Microphone audio input
* **pyttsx3** – Text-to-speech engine
* **JSON** – Processing recognition output
* **datetime** – Date and time utilities

---

## 📂 Project Structure

```text
offline-hindi-voice-assistant/
│
├── vosk-model-small-hi-0.22/   # Hindi Vosk model
├── hindi_assistant.py          # Main application
├── requirements.txt
└── README.md
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

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Hindi Vosk Model

Download:

https://alphacephei.com/vosk/models

Use the model:

```text
vosk-model-small-hi-0.22
```

Extract it into the project directory so the structure looks like:

```text
offline-hindi-voice-assistant/
├── vosk-model-small-hi-0.22/
├── hindi_assistant.py
```

---

## ▶️ Running the Assistant

Start the assistant using:

```bash
python hindi_assistant.py
```

After launching, the assistant will display:

```text
हिंदी वॉइस असिस्टेंट शुरू हो गया है।
```

Then speak your commands in Hindi.

---

## 🎤 Supported Commands

| Hindi Command | Action                           |
| ------------- | -------------------------------- |
| नमस्ते        | Greeting                         |
| समय           | Tells current time               |
| तारीख         | Tells current date               |
| दिन           | Tells current day                |
| साल           | Tells current year               |
| नाम           | Introduces itself                |
| मौसम          | Gives a default weather response |
| कैसे हो       | Casual conversation              |
| धन्यवाद       | Replies politely                 |
| मदद           | Lists supported commands         |
| चुटकुला       | Tells a joke                     |
| फिर बोलो      | Repeats the previous response    |
| किसने बनाया   | Explains its purpose             |
| तुम कौन       | Introduces itself                |
| अलविदा        | Exits the assistant              |
| बंद           | Stops the assistant              |

---

## 📦 Requirements

```text
vosk
sounddevice
pyttsx3
```

Install manually if needed:

```bash
pip install vosk sounddevice pyttsx3
```

---

## 🚀 Future Improvements

Possible enhancements include:

* Opening desktop applications using voice commands
* Web searching capabilities
* Playing music automatically
* Weather updates from APIs
* Hindi question-answering using local language models
* Support for additional Indian languages
* Graphical user interface (GUI)

---

## 🎯 Learning Outcomes

This project demonstrates:

* Offline speech recognition in Hindi
* Real-time microphone audio processing
* Text-to-speech integration in Python
* Building simple voice-controlled applications
* Using Vosk for resource-efficient speech systems

---

### Empowering Hindi voice interaction through simple offline AI. 🇮🇳🎙️
