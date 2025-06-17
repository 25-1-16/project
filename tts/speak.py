from gtts import gTTS
from playsound import playsound
import os

def speak(product_name):
    """
    주어진 과자 이름을 음성으로 안내합니다.
    """
    text = f"이 제품은 {product_name}입니다"
    tts = gTTS(text=text, lang='ko')
    tts.save("output.mp3")
    playsound("output.mp3")
