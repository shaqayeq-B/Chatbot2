import speech_recognition as sr
from gtts import gTTS
import os
import json

word_definitions = {
    "سلام": "درود و احوالپرسی",
    "خداحافظ": "خداحافظی کردن",
    "پایتون": "یک زبان برنامه نویسی سطح بالا",
    "هوش مصنوعی": "شاخه ای از علوم کامپیوتر برای ساخت ماشین های هوشمند",
    "برنامه نویسی": "فرایند ساخت برنامه های کامپیوتری"
}

# ذخیره دیکشنری در فایل
SAVE_FILE = "dictionary.json"

def load_dictionary():
    global word_definitions
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            word_definitions = json.load(f)
    except FileNotFoundError:
        pass

def save_dictionary():
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(word_definitions, f, ensure_ascii=False)

def text_to_speech(text):
    tts = gTTS(text=text, lang='fa')
    tts.save("output.mp3")
    os.system("start output.mp3")

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("در حال گوش دادن...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language='fa-IR')
        print(f"شما گفتید: {text}")
        return text
    except:
        return None

def learn_new_word(word):
    text_to_speech(f"کلمه {word} رو نمی شناسم. لطفا تعریفش رو بگویید")
    print(f"کلمه جدید: {word} - لطفا تعریف را وارد کنید...")
    
    definition = None
    while not definition:
        definition = speech_to_text()
        if not definition:
            text_to_speech("تعریف رو متوجه نشدم. لطفا دوباره بگویید")
    
    word_definitions[word] = definition
    save_dictionary()
    
    text_to_speech(f"متشکرم! حالا کلمه {word} رو یاد گرفتم")
    return definition

def main():
    load_dictionary()
    
    while True:
        user_input = speech_to_text()
        
        if not user_input:
            text_to_speech("متوجه صحبت شما نشدم")
            continue
            
        if user_input.lower() in ["خروج", "بستن"]:
            text_to_speech("خداحافظ! تا بعدی")
            break
            
        definition = word_definitions.get(user_input)
        
        if not definition:
            definition = learn_new_word(user_input)
            
        print(f"تعریف: {definition}")
        text_to_speech(definition)

if __name__ == "__main__":
    main()