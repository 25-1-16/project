from gtts import gTTS   # gTTS (Google Text-to-Speech) 모듈에서 gTTS 클래스만 가져오기
import os   # os 모듈을 사용하면 mp3 파일을 자동으로 실행(재생)시킬 수 있어

product_name = "새우깡"   # 음성으로 읽을 과자 이름 지정
text = f"이 제품은 {product_name}입니다"   # 최종으로 말할 문장 구성

tts = gTTS(text=text, lang='ko')   # gTTS 객체 생성: 위의 텍스트를 한국어(lang='ko')로 음성 변환 준비
tts.save("output.mp3")   # 음성 파일(mp3)로 저장 (파일명은 'output.mp3')

os.system("start output.mp3")  # 저장된 mp3 파일을 시스템 기본 음악 플레이어로 실행 (윈도우 기준)
