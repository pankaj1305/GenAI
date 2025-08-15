# Install necessary libraries
sudo apt install portaudio19-dev python3-pyaudio
!pip3 install SpeechRecognition googletrans==4.0.0-rc1 gTTS playsound


import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

# Define supported languages
input_languages = {
    "1": ("en", "English"),
    "2": ("hi", "Hindi"),
    "3": ("es", "Spanish"),
    "4": ("fr", "French"),
    "5": ("de", "German")
}

output_languages = {
    "1": ("en", "English"),
    "2": ("hi", "Hindi"),
    "3": ("es", "Spanish"),
    "4": ("fr", "French"),
    "5": ("de", "German")
}

# Choose input language
print("Select Input Language:")
for key, value in input_languages.items():
    print(f"{key}. {value[1]}")
input_choice = input("Enter choice: ").strip()
input_lang_code = input_languages[input_choice][0]

# Choose output language
print("\nSelect Output Language:")
for key, value in output_languages.items():
    print(f"{key}. {value[1]}")
output_choice = input("Enter choice: ").strip()
output_lang_code = output_languages[output_choice][0]

# Initialize recognizer & translator
recognizer = sr.Recognizer()
translator = Translator()

with sr.Microphone() as source:
    print("\nSpeak something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio, language=input_lang_code)
        print(f"Original ({input_languages[input_choice][1]}):", text)

        # Translate text
        translated = translator.translate(text, src=input_lang_code, dest=output_lang_code)
        print(f"Translated ({output_languages[output_choice][1]}):", translated.text)

        # Convert translated text to speech
        tts = gTTS(text=translated.text, lang=output_lang_code)
        output_file = "translated_audio.mp3"
        tts.save(output_file)
        playsound.playsound(output_file)
        os.remove(output_file)

    except Exception as e:
        print("Error:", e)
