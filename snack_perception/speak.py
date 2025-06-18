from gtts import gTTS
import pygame
import time
import os
import uuid

def speak(product_name):
    text = f"이 제품은 {product_name}입니다"
    tts = gTTS(text=text, lang='ko')

    # 고유한 임시 mp3 파일명 생성
    filename = f"output_{uuid.uuid4()}.mp3"
    tts.save(filename)

    # pygame 초기화 및 재생
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # 재생이 끝날 때까지 대기
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # 명시적으로 언로드 및 초기화 후 삭제
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()  # mixer 완전 해제

    try:
        os.remove(filename)
    except PermissionError:
        print(f"파일 삭제 실패: {filename}")
