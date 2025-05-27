import tkinter as tk
import pyautogui
import win32con
import win32gui
import time
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading


def create_image():
    # 간단한 동그란 아이콘 이미지 생성
    image = Image.new("RGB", (64, 64), (255, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.ellipse((16, 16, 48, 48), fill=(255, 255, 255))
    return image


def on_quit(icon, item):
    icon.stop()
    root.quit()


def tray_thread():
    icon = Icon("OverlayLineTool", create_image(), menu=Menu(MenuItem("Quit", on_quit)))
    icon.run()


def make_window_clickthrough(hwnd):
    # 확장 스타일에 WS_EX_LAYERED | WS_EX_TRANSPARENT 설정
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
    # 투명 색상 지정
    win32gui.SetLayeredWindowAttributes(hwnd, 0x00FFFFFF, 255, win32con.LWA_COLORKEY)


def update_line():
    screen_width = root.winfo_screenwidth()
    x, y = pyautogui.position()
    canvas.delete("all")
    canvas.create_line(0, y-15, screen_width, y-15, fill="green", width=3)
    root.after(20, update_line)


def initialize_overlay():
    # 창이 뜰 때까지 잠깐 기다림
    time.sleep(0.5)
    hwnd = win32gui.FindWindow(None, "MyOverlayWindow")
    if hwnd == 0:
        print("❌ 창 핸들 찾기 실패: FindWindow가 0을 반환했어요.")
    else:
        make_window_clickthrough(hwnd)


# tkinter 설정
root = tk.Tk()
root.title("MyOverlayWindow")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.attributes("-transparentcolor", "white")

# 캔버스 생성
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# 클릭 통과 설정 (after로 창 생성 직후 처리)
root.after(100, initialize_overlay)
threading.Thread(target=tray_thread, daemon=True).start()
update_line()

root.mainloop()
