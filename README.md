# 🍪 16조 Project - 시각장애인을 위한 과자 인식 프로그램
YOLOv5 + gTTS 기반 시각보조 서비스


카메라로 과자를 인식하고 음성으로 안내해주는 AI 편의점 도우미

<br/>

🍪 Snack Recognition Program for the Visually Impaired

YOLOv5 + gTTS-Based Visual Assistance Service

An AI convenience store assistant that recognizes snacks using a camera and provides audio guidance

<br/>

---

## 👨‍👩‍👧‍👦 제작자 및 팀 소개
이 프로젝트는 숙명여자대학교 오픈소스프로그래밍 수업의 팀프로젝트로 제작되었습니다.

👤 김경민 — 팀장, 데이터 수집 및 가공, YOLOv5 모델 학습, 과자 이미지 인식 모듈 개선, 보고서 작성

👤 김가은 — 데이터 수집 및 가공, YOLOv5 모델 학습, 음성 안내 출력 모듈 개선, 인터페이스 구현, 보고서 작성

👤 심세희 — 데이터 수집 및 가공, YOLOv5 모델 학습, 과자 이미지 인식 모듈 개선, 기능 연결, 보고서 작성

<br/>

👨‍👩‍👧‍👦 Team Introduction

This project was created as a team project for the Open Source Programming course at Sookmyung Women's University

<br/>

---

## 🎯 주제

> **시각장애인을 위한 편의점 과자 인식 프로그램**

- 웹캠을 통해 실시간으로 과자를 인식하고
- 인식된 과자명을 **gTTS**로 음성 안내합니다
- YOLOv5 모델을 활용하여 다양한 과자 종류를 탐지합니다

<br/>

🎯 Project Topic

Snack recognition program for the visually impaired

Recognizes snacks in real-time through a webcam

Provides audio guidance of the recognized snack name using gTTS

Detects a variety of snack types using the YOLOv5 model

<br/>

---

## 📁 파일별 설명 요약

### 📷 `camera_stream/`

- `camera_stream.py`: 카메라 테스트용. 실시간 영상이 제대로 출력되고 과자를 인지하는지 확인

### 🧠 `snack_perception/`

- `snack_perception.py`: YOLOv5를 사용해 과자를 인식하고 결과를 시각화
- `speak.py`: 인식된 과자명을 한국어 음성으로 변환 (gTTS + pygame 사용)

### 💻 `interface/`

- `interface.py`: GUI 버튼 기반 실행 인터페이스 (Tkinter 사용)
- 사용자가 "시작" 버튼을 클릭하면 과자 인식 프로그램이 실행됨

### 🗣 `tts/`

- `test_gtts.py`: gTTS 음성 출력 테스트용 코드
- `speak.py`: 합치기 전 speak 코드 

### 🔍 `training/`

- `MyTraining.ipynb`: YOLOv5를 활용한 과자 학습 코드
- `dataset/`: 학습에 사용된 과자 이미지 및 라벨링 데이터
- `best.pt`: 학습된 최종 모델 파일
<br/>
---

## ✅ 주요 기능

- 과자 탐지: 실시간으로 YOLOv5가 과자 종류 탐지
- 음성 안내: gTTS 기반 TTS로 과자명 안내
- UI 인터페이스: 시작 버튼만 누르면 작동, 접근성 강화

<br/>

✅ Key Features

Snack detection: YOLOv5 detects snack types in real time

Voice guidance: Announces snack names with gTTS-based TTS

UI interface: Operates with a single "Start" button for enhanced accessibility

<br/>

---

## 🔧 실행 방법

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```
### 2. interface.py 실행하기

### 3. 종료 시 `q` 누르기

<br/>

🔧 How to Run

1. install dependencies

2. Run interface.py

3. Press `q` to quit


