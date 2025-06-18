import cv2
import torch
import numpy as np
import sys
import pathlib
from speak import speak  # speak.py의 speak 함수 임포트

pathlib.PosixPath = pathlib.WindowsPath

# YOLOv5 경로 추가
sys.path.append('./yolov5')
from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes
from utils.augmentations import letterbox

# YOLOv5 모델을 로드
detect_snack = DetectMultiBackend(weights='best.pt', device='cpu')
stride, names = detect_snack.stride, detect_snack.names

# 같은 class 별로 confidence 높은 것만 남기기
def filter_highest_confidence_per_class(detections):
    highest_conf = {}
    for det in detections:
        cls = int(det[-1].item())
        conf = det[-2].item()
        if cls not in highest_conf or conf > highest_conf[cls][-2].item():
            highest_conf[cls] = det
    if highest_conf:
        return torch.stack(list(highest_conf.values()))
    else:
        return torch.empty((0,6))

def get_camera_frame():
    cap = cv2.VideoCapture(0) # 0번 장치를 통해 노트북 카메라 켜기
    if not cap.isOpened():
        print("카메라 연결 실패")
        return

    last_snack = None  # 연속 같은 과자 음성 반복 방지

    while True:
        ret, frame = cap.read() # 실시간으로 한 장씩 프레임 가져오기
        if not ret:
            break

        # 1. 전처리: 이미지 크기 조정 및 텐서 변환
        img = letterbox(frame, 640, stride=stride, auto=True)[0]
        img = img.transpose((2, 0, 1))[::-1]
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to('cpu')
        img = img.float() / 255.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # 2. 추론
        pred = detect_snack(img, augment=False, visualize=False)
        pred = non_max_suppression(pred, 0.25, 0.45, classes=None, agnostic=False)

        snack_name = None

        # 3. 후처리 및 시각화
        for det in pred:
            if len(det):
                det = filter_highest_confidence_per_class(det) # 클래스별 confidence가 가장 높은 것만 남기기
                det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], frame.shape).round()
                for *xyxy, conf, cls in reversed(det):
                    label = f'{names[int(cls)]} {conf:.2f}'
                    x1, y1, x2, y2 = map(int, xyxy)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                    snack_name = names[int(cls)]  # 마지막으로 인식된 과자 이름

        if snack_name and snack_name != last_snack:
            print(f"음성 출력: {snack_name}")
            speak(snack_name)
            last_snack = snack_name

        cv2.imshow("Camera", frame)  # 받은 프레임 화면에 띄우기
        if cv2.waitKey(1) & 0xFF == ord('q'):  # q 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get_camera_frame()
