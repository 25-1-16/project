# 🍪 Snack Perception: 시각장애인을 위한 과자 인식 프로그램

YOLOv5와 gTTS를 활용하여 **실시간으로 과자를 인식하고 음성으로 안내**하는 시각보조 프로그램입니다.  
웹캠으로 촬영된 영상에서 편의점 과자를 탐지한 뒤, 인식된 과자 이름을 한국어로 음성 안내해줍니다.

<br>

🍪 Snack Perception: Snack Recognition Program for the Visually Impaired

This is a visual aid program that utilizes YOLOv5 and gTTS to recognize snacks in real time and provide voice guidance.

After detecting convenience store snacks from webcam footage, it announces the recognized snack name in Korean.

<br>

---
# ✅ 주요 기능

- 📷 실시간 웹캠 영상에서 과자 인식 (YOLOv5 기반)
- 🔊 과자 이름을 한국어로 음성 안내 (gTTS 사용)
- 🔁 같은 과자 반복 인식 방지
- 🧠 confidence가 가장 높은 결과만 추출하여 정확도 향상
- 키보드에서 q를 눌러 프로그램을 종료시킴

<br>

✅ Key Features

Recognizes snacks in real time from webcam video (YOLOv5-based)

Announces snack names in Korean using voice guidance (gTTS)

Prevents repeated recognition of the same snack

Extracts only the result with the highest confidence to improve accuracy

The program can be terminated by pressing `q` on the keyboard

<br>

---
# 💡 프로젝트 목적

시각장애인도 편의점에서 간편하게 과자 종류를 인식할 수 있도록 보조 기술을 개발하고자 시작한 프로젝트입니다.  
단순 탐지가 아닌 음성 안내를 통해 직접적인 피드백을 받을 수 있도록 구현했습니다.

<br>

💡 Project Purpose

This project was initiated to develop assistive technology that enables visually impaired individuals to easily recognize snack types in convenience stores.

It is implemented to provide direct feedback through voice guidance, not just simple detection.

<br>

---
# 🛠 사용 기술

| 기술 | 설명 |

| Python 3.10 | 전체 구현 언어 |

| YOLOv5 | 객체 탐지 모델 (best.pt로 커스텀 학습) |

| OpenCV | 실시간 영상 처리 |

| gTTS | 음성 출력 (Google Text-to-Speech) |

| pygame | MP3 파일 재생 |

| PyTorch | 모델 추론 |

<br>
---
# ▶️ 실행 방법
```
(bash)
python snack_perception.py
```

<br>
---
# 📦 설치 방법
필수 라이브러리 일괄 설치

```
(bash)
pip install -r requirements.txt
```

<br>
---
# 📁 프로젝트 구조

Snack-Perception/

├── yolov5/               # YOLOv5 모델 코드 (git clone한 yolov5)

├── best.pt               # 커스텀 학습된 과자 인식 모델

├── snack_perception.py   # 메인 실행 파일

├── speak.py              # 텍스트를 음성으로 출력하는 모듈

└── README.md             # 프로젝트 설명 문서

(yolov5 디렉토리는 YOLOv5 공식 저장소를 클론해서 사용 - git clone https://github.com/ultralytics/yolov5.git)

<br>
---
# 📷 실행 화면
<img width="484" alt="과자 인식 실행 결과 예시" src="https://github.com/user-attachments/assets/507b263c-5724-4f6f-a795-042c462ce4ec" />

과자가 인식 되면 '이 제품은 ~~ 입니다.'라는 음성 메세지가 출력됨

<br>
---
# 📌 참고 사항
- mp3 재생을 위해 pygame 사용 시 간헐적인 파일 접근 오류를 방지하기 위해 고유한 파일명(uuid)으로 저장하고 삭제합니다.
- best.pt는 프로그램 제작을 위해 저희 조가 학습시킨 모델을 의미합니다.

<br>

📌 Notes

To prevent occasional file access errors when playing mp3 files with pygame, each file is saved and deleted with a unique filename (using uuid).

*best.pt* refers to the model our team trained for this program.
