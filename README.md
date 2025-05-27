# 🖱️ Transparent Overlay Line Tool
## TOOL PROGRAM, USING AI

A simple and lightweight transparent overlay tool that draws a horizontal guide line following your mouse cursor vertically.  
Useful for comparing documents side by side or aligning content visually.

![장난감2](https://github.com/user-attachments/assets/b5160bf8-26ac-4bcd-9712-c3fbff2f59d4)

---

## ✨ Features

- 🎯 **Mouse Y-axis tracking**: A thin red horizontal line follows the cursor across the screen.
- 🧼 **Transparent overlay**: The overlay is fully transparent except for the guide line.
- 🖱 **Click-through enabled**: You can interact with windows underneath as usual — the overlay doesn't block input.
- 📌 **Always on top**: Stays above all windows for continuous visibility.
- ⚙️ **Customizable** (line color, thickness, multiple lines, etc. can be added easily)

---

## 🛠️ Built With

- `tkinter` — GUI window management  
- `pyautogui` — Mouse tracking  
- `pywin32` — Windows API access for click-through functionality  

---

## 📦 Installation

1. Install dependencies:

   ```
   pip install pywin32 pyautogui
   or
   pip install -r requirements.txt
   ```

2. Clone the repository and run the script:

   ```
   git clone https://github.com/Tarrow9/mouse_wing.git
   cd mouse_wing
   python main.py
   ```

3. *(Optional)* Create an `.exe` file using [PyInstaller](https://pyinstaller.org/):

   ```
   pip install pyinstaller
   pyinstaller --noconsole --onefile --name mouse_wing main.py
   ```

---

## 📌 Use Cases

- Aligning lines when comparing two documents side-by-side  
- Visual aid during proofreading, editing, or presentations  
- Live coding or design demos where consistent visual tracking helps

---

## 🧪 Example

```
canvas.create_line(0, y, screen_width, y, fill="red", width=1)
```

The core logic draws a line from the left to right side of the screen at the current mouse Y position.

---

## 📝 License

MIT License. Feel free to use, modify, and share!

---

## 💬 Feedback

Feel free to open an issue or pull request. Contributions are welcome!
