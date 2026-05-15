import google.generativeai as genai
from gtts import gTTS
import os
import PIL.Image


genai.configure(api_key='AIzaSyBl71ay1NP9xX9Su_dWnZ5qebcY6xAaKug')


model = genai.GenerativeModel('gemini-flash-latest')

def analyze_medical_image(image_path):
    print(f"Аналіз знімка: {image_path}...")
    try:
        img = PIL.Image.open(image_path)
        prompt = "Опиши цей медичний знімок українською мовою. Тільки візуальні факти, без діагнозів."
        response = model.generate_content([prompt, img])
        return response.text
    except Exception as e:
        return f"Помилка: {e}"

def text_to_speech(text):
    print("Генерація озвучки...")
    if "Помилка" in text: return
    tts = gTTS(text=text, lang='uk')
    tts.save("result.mp3")
    os.system("start result.mp3")

if __name__ == "__main__":
    file_path = "scan.jpg"
    if os.path.exists(file_path):
        desc = analyze_medical_image(file_path)
        print(f"\nОпис: {desc}")
        text_to_speech(desc)
    else:
        print("Файл scan.jpg не знайдено в папці!")