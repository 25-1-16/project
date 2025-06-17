import cv2

def get_camera_frame():
    cap = cv2.VideoCapture(0)  # 0번 장치를 통해 노트북 카메라 켜기

    if not cap.isOpened():
        print("카메라 연결 실패")
        return

    while True:
        ret, frame = cap.read() # 실시간으로 한 장씩 프레임 가져오기
        if not ret:
            break

        # YOLO 처리 (나중에 연결)
        # result = detect_snack(frame)
        # print("인식 결과:", result)

        cv2.imshow("Camera", frame) # 받은 프레임 화면에 띄우기
        if cv2.waitKey(1) & 0xFF == ord('q'): # q 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get_camera_frame()
