import sounddevice as sd
import vosk
import json
import os
import pyttsx3
import datetime
import time

# ---------------- CONFIG ----------------
MODEL_PATH = "vosk-model-small-hi-0.22"  # Put the Hindi Vosk model folder here
SAMPLE_RATE = 16000

if not os.path.exists(MODEL_PATH):
    print("Model not found! Download from https://alphacephei.com/vosk/models and unzip.")
    exit()

# ---------------- LOAD MODEL ----------------
model = vosk.Model(MODEL_PATH)
recognizer = vosk.KaldiRecognizer(model, SAMPLE_RATE)

# ---------------- TTS ----------------
def speak(text):
    print("Assistant:", text)
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine
        time.sleep(0.3)
    except Exception as e:
        print("Voice error:", e)

# ---------------- COMMANDS ----------------
last_response = ""

def execute_command(cmd):
    global last_response
    now = datetime.datetime.now()

    if cmd == "नमस्ते":
        print("Assistant: नमस्ते! मैं आपकी मदद के लिए हूँ।")
        last_response = "Namaste! Main aapki madad ke liye hoon"
    elif cmd == "समय":
        print(f"Assistant: समय है {now.strftime('%H:%M')}")
        last_response = f"Samay hai {now.strftime('%H:%M')}"
    elif cmd == "तारीख":
        print(f"Assistant: तारीख {now.strftime('%d %B %Y')}")
        last_response = f"tarikh {now.strftime('%d %B %Y')}"
    elif cmd == "नाम":
        print("Assistant: मेरा नाम हिंदी असिस्टेंट है।")
        last_response = "Mera naam Hindi Assistant hai"
    elif cmd == "मौसम":
        print("Assistant: मौसम सामान्य है।")
        last_response = "mausam normal hai"
    elif cmd == "धन्यवाद":
        print("Assistant: आपका स्वागत है।")
        last_response = "Aapka swagat hai"
    elif cmd == "मदद":
        print("Assistant: समय, तारीख, मौसम, नाम या चुटकुला पूछ सकते हैं।")
        last_response = "Samay, tarikh, mausam, naam, joke pooch sakte hain"
    elif cmd == "चुटकुला":
        print("Assistant: प्रोग्रामर छुट्टी पर था, क्योंकि कैश क्लियर कर रहा था!")
        last_response = "Programmer holiday pe tha, kyonki Cache clear kar rha tha!"
    elif cmd == "कैसे हो":
        print("Assistant: मैं बिल्कुल ठीक हूँ।")
        last_response = "Main bilkul theek hoon"
    elif cmd == "फिर बोलो":
        print("Assistant:", last_response if last_response else "दोहराने के लिए कुछ नहीं है।")
        last_response = last_response if last_response else "Kuch dohrane ko nahi hai"
    elif cmd == "दिन":
        print(f"Assistant: {now.strftime('%A')} है।")
        last_response = f"{now.strftime('%A')} hai"
    elif cmd == "साल":
        print(f"Assistant: साल {now.strftime('%Y')} है।")
        last_response = f"Saal {now.strftime('%Y')}"
    elif cmd == "किसने बनाया":
        print("Assistant: मुझे आपके प्रोजेक्ट के लिए बनाया गया है।")
        last_response = "Mujhe aapke project ke liye banaya gaya hai"
    elif cmd == "तुम कौन":
        print("Assistant: मैं एक ऑफलाइन हिंदी वॉयस असिस्टेंट हूँ।")
        last_response = "Main ek offline Hindi voice assistant hoon"
    elif cmd in ["अलविदा", "बंद"]:
        print("Assistant: अलविदा! फिर मिलेंगे।")
        last_response = "Alvida! Phir milenge"
    else:
        print("Assistant: माफ़ कीजिए, मैं समझ नहीं पाया।")
        last_response = "Maaf kijiye, main samajh nahi paaya"

    speak(last_response)
    return cmd in ["अलविदा", "बंद"]

# ---------------- LISTEN FUNCTION ----------------
def listen():
    print("\n 🎤 कृपया हिंदी में बोलिए...")
    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype='int16', channels=1) as stream:
        while True:
            data, _ = stream.read(4000)
            if recognizer.AcceptWaveform(bytes(data)):
                result = json.loads(recognizer.Result())
                recognizer.Reset()
                text = result.get("text", "")
                if text:
                    print("You said:", text)
                    return text

# ---------------- MAIN LOOP ----------------
print("Assistant: हिंदी वॉइस असिस्टेंट शुरू हो गया है।")
speak("Hindi voice assistant shuru ho gaya hai")

while True:
    command_text = listen()
    stop = execute_command(command_text)
    if stop:
        break
