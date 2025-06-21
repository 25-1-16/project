# 🍪 인터페이스 모듈 - 과자 인식 음성 안내 프로그램

본 인터페이스는 **시각장애인을 위한 과자 인식 음성 안내 프로젝트**의 시작점 역할을 합니다.  
사용자는 버튼 하나만 클릭하면, 카메라가 자동으로 켜지고 과자를 인식하며, 그 이름을 한국말 음성으로 안내합니다.

<br>

🍪 Interface Module – Snack Recognition Voice Guidance Program

This interface serves as the starting point for the snack recognition voice guidance project for the visually impaired.

With just a single button click, the user can automatically activate the camera, recognize snacks, and hear their names through voice guidance in Korean.

<br>

---

## 📌 목적

시각장애인이 **스스로 과자의 종류를 확인**할 수 있도록 돕는 프로그램입니다.  
기기의 복잡한 조작 없이 **버튼 하나만 클릭**하면 인식 및 안내가 자동으로 이루어집니다.

<br>

📌 Purpose

This program is designed to help visually impaired individuals identify different types of snacks by themselves.

Recognition and guidance are performed automatically with a single button click, without the need for complex device operations.

<br>

---

## 🖥️ 인터페이스 창 설명 

### 🎛 "시작" 버튼
- 버튼을 클릭하면 카메라가 켜지고, 실시간으로 과자를 인식합니다.
- 과자가 인식되면 이름이 음성으로 안내됩니다.

### 🪞 OpenCV 창
- 인식된 과자 화면이 실시간으로 표시되며,
- 과자명과 신뢰도(confidence)가 함께 출력됩니다.

### ❌ 종료 방법
- OpenCV 창에서 **`q` 키**를 누르면 인식이 종료됩니다.

<br>

🖥️ Interface Window Description

🎛 "Start" Button

When the button is clicked, the camera turns on and snacks are recognized in real time.

When a snack is recognized, its name is announced via voice guidance.

🪞 OpenCV Window

The recognized snack is displayed on the screen in real time,

along with the snack name and confidence score.

❌ How to Exit

Press the 'q' key in the OpenCV window to end recognition.

<br>

---

## 📦 의존 라이브러리
- `tkinter` - GUI 구성용 (Python 내장)
- `opencv-python` - 카메라 제어 및 영상 처리
- `torch` - YOLOv5 모델 실행
- `numpy` - 수치 계산
- `gTTS` - Google TTS (음성 생성)
- `pygame` - mp3 재생용
