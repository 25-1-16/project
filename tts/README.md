# 🗣️ TTS 모듈

이 폴더는 과자 이름을 음성으로 안내하는 기능을 포함합니다.

## 파일 설명

- `speak.py` : 프로젝트에서 사용하는 gTTS 기반 음성 안내 함수
- `test_gtts.py` : 초기 테스트용 코드 (단독 실행)

## 사용 예시

```python
from tts.speak import speak
speak("초코파이")
