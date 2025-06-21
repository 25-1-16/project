# 🗣️ TTS 모듈

이 폴더는 인식된 과자 이름을 **음성으로 안내하는 기능**을 담당합니다.  
Google의 gTTS(Google Text-to-Speech) API를 기반으로 음성을 생성하고,  
Pygame을 이용해 mp3 파일을 재생합니다.

<br>

🗣️ TTS Module

This folder is responsible for providing voice guidance of the recognized snack names.

It generates speech using Google’s gTTS (Google Text-to-Speech) API and plays the resulting mp3 files with Pygame.

<br>

---
## 📖 파일 설명

- `speak.py` : 프로젝트 본 코드에서 사용하는 **음성 안내 함수** 정의 
- `test_gtts.py` : TTS 기능을 단독으로 실행해보는 **테스트용 스크립트**

<br>

📖 File Descriptions

speak.py : Defines the voice guidance functions used in the main project code

test_gtts.py : A test script for running the TTS feature independently

<br>

---
## 🔧 동작 방식 요약

1. 텍스트 → gTTS로 mp3 파일 생성
2. 임시 mp3를 저장하고 재생 (Pygame 활용)
3. 음성 출력 후 파일 자동 삭제

<br>

🔧 Operation Summary

1. Converts text to speech using gTTS and generates an mp3 file
2. Saves and plays the temporary mp3 file (using Pygame)
3. Automatically deletes the file after the audio is played

<br>

---
## 📦 의존라이브러리 설치 

`pip install -r requirements.txt`

---

## 🧪 사용 예시

```python
from tts.speak import speak
speak("초코파이")


