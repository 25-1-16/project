# 🧪 모델 학습 (training)

YOLOv5 기반 과자 인식 모델을 학습한 폴더입니다.

## 📁 폴더 구성

- `MyTraining.ipynb` : 학습을 위한 주피터 노트북 파일  
- `dataset/` : Roboflow에서 다운로드한 학습용 이미지 및 라벨링 데이터  
- `roboflow/` : Roboflow에서 제공된 설정 및 클래스 정보  
- `best.pt` (X): 이제는 `snack_perception` 폴더로 이동했습니다

## ✅ 사용 도구

- Roboflow + YOLOv5
- Colab 또는 로컬 Jupyter 환경에서 학습 수행

## 📌 주의

- 학습 완료된 모델 파일(`best.pt`)은 이 폴더에 포함되지 않습니다
- 모델은 `snack_perception/best.pt`에 배치되어 사용됩니다
