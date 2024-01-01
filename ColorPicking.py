import tkinter as tk
import pyautogui
from PIL import ImageTk

full_screenshot = pyautogui.screenshot()
zoomed_screenshot = None

ZOOM_FACTOR = 5
def getting_color(event):
    global zoomed_screenshot, zoom_region_top_left

    if zoomed_screenshot:
        zoom_x, zoom_y = zoom_region_top_left
        x = (event.x // ZOOM_FACTOR) + zoom_x
        y = (event.y // ZOOM_FACTOR) + zoom_y
    else:
        x, y = event.x_root, event.y_root

    r, g, b = full_screenshot.getpixel((x, y))
    print(r,g,b)
    root.destroy()

def zoom(event):
    global zoomed_screenshot, zoom_region_top_left

    root.attributes('-alpha', 0.0)
    REGION_SIZE = 50

    x, y = event.x_root, event.y_root
    zoom_x = x - REGION_SIZE // 2
    zoom_y = y - REGION_SIZE // 2
    zoom_region_top_left = (zoom_x, zoom_y)

    zoom_screenshot = pyautogui.screenshot(region=(zoom_x, zoom_y, REGION_SIZE, REGION_SIZE))
    zoomed_screenshot = zoom_screenshot.resize((REGION_SIZE * ZOOM_FACTOR, REGION_SIZE * ZOOM_FACTOR))
    root.attributes('-alpha', 0.3)

    top = tk.Toplevel()
    top.config(cursor="circle") 
    zoomed_photo = ImageTk.PhotoImage(zoomed_screenshot)
    label = tk.Label(top, image=zoomed_photo, borderwidth=0)
    label.image = zoomed_photo
    label.pack()

    top.overrideredirect(True)
    label.bind('<ButtonPress-1>', getting_color)

root = tk.Tk()
root.config(cursor="circle") 
root.overrideredirect(True)
root.state('zoomed')
root.attributes('-alpha', 0.3)

canvas = tk.Canvas(root, bg="#232529", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind('<ButtonPress-1>', getting_color)
canvas.bind('<ButtonPress-3>', zoom)

root.mainloop()
