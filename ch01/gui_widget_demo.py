import tkinter as tk

def on_click():
    user_text = entry.get()
    label.config(text=f"입력한 내용: {user_text}")

root = tk.Tk()
root.title("tkinter 위젯 및 이벤트 실습")
root.geometry("400x200")

label = tk.Label(root, text="텍스트를 입력하세요:")
entry = tk.Entry(root)
button = tk.Button(root, text="확인", command=on_click)

label.pack(pady=5)
entry.pack(pady=5)
button.pack(pady=5)

root.mainloop()