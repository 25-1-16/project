import tkinter as tk
import threading
import sys
import os

# 상위 폴더(snack_perception 모듈 경로)를 import 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 과자 인식 함수 불러오기
from snack_perception.snack_perception import get_camera_frame

def start_program():
    # UI 멈추지 않도록 별도 쓰레드에서 실행
    threading.Thread(target=get_camera_frame).start()

# GUI 설정
window = tk.Tk()
window.title("🍪 과자 인식 시작")
window.geometry("300x180")
window.resizable(False, False)

label = tk.Label(window, text="과자 인식을 시작하려면\n아래 버튼을 눌러주세요", font=("맑은 고딕", 12), pady=20)
label.pack()

start_button = tk.Button(window, text="시작", command=start_program, font=("맑은 고딕", 12), bg="lightblue", width=12)
start_button.pack(pady=10)

window.mainloop()
