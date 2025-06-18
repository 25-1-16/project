# Snack Recognition

**프로젝트는 Anaconda 가상환경에서 이루어졌습니다.**

<br/>

웹캠을 이용해 실시간으로 과자를 인식하는 프로그램입니다.

YOLOv5 객체 탐지 모델을 사용하며, 각 간식 종류별로 신뢰도가 가장 높은 결과만 화면에 표시합니다.

이 코드는 시각장애인을 위한 과자 인식 시스템의 실시간 카메라 프레임 수집과 과자 종류 판별 기능을 담당합니다.

<br/>

## 📸 주요 기능
- 컴퓨터 내장 카메라를 통해 실시간 영상 수신
- 프레임 단위로 이미지 캡처
- YOLOv5 분석 모듈에 프레임 전달
- 클래스 별 최고 신뢰도 결과만 표시
- 바운딩 박스 및 라벨 시각화
- CPU 환경에서 동작
- `q` 키를 누르면 영상 종료

<br/>

## 📂 필요한 라이브러리
* opencv-python
* torch
* numpy
* YOLOv5 실행에 필요한 패키지 : requirements.txt

<br/>

## 💻 코드 작동 방법
`$ python camera_stream.py`

<br/>

## 🍪 실행 결과
<img width="484" alt="Image" src="https://github.com/user-attachments/assets/e30e6663-461c-4eb8-b59c-ca5081036d2c" />
