import platform
import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import time
from playsound import playsound
from math import floor

from .cat import Cat, CatType

CATS = {typ: Cat(typ) for typ in CatType}

cat_dimensions = (120, 120)
center_dimensions = None

spawnInterval = 5

event_number = random.randrange(1, 3, 1)

# https://stackoverflow.com/a/57935285
def widget_drag_free_bind(widget):
    """Bind any widget or Tk master object with free drag"""
    master = widget

    x, y = 0, 0
    def mouse_motion(event):
        global x, y
        # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
        offset_x, offset_y = event.x - x, event.y - y
        new_x = master.winfo_x() + offset_x
        new_y = master.winfo_y() + offset_y
        new_geometry = f"+{new_x}+{new_y}"
        master.geometry(new_geometry)

    def mouse_press(event):
        global x, y
        count = time.time()
        x, y = event.x, event.y

    widget.bind("<B1-Motion>", mouse_motion)  # Hold the left mouse button and drag events
    widget.bind("<Button-1>", mouse_press)  # The left mouse button press event, long calculate by only once


#window.after is after y ms, do the function action -> can provide parameters as further arguments
# transfer random no. to event
def event(cat, cycle, window, label):
    window.after(150, update, cat, cycle, window, label)

def new_image(window, label, frame):
    if platform.system() == "Darwin":
        label.destroy()
        new_label = tk.Label(window, width=100, bg='systemTransparent')
        new_label.pack()
        new_label.configure(image=frame)
    elif platform.system() == "Windows":
        label.configure(image=frame)
    else:
        label.configure(image=frame)


def update(cat, cycle, window, label):
    # cycle is frame number

    global startTime
    if time.time() - startTime >= spawnInterval and window == mainWindow:
        create_display(mainWindow, (random.randrange(XRange[0], XRange[1], 1), random.randrange(YRange[0], YRange[1], 1)))
        startTime = time.time()

    is_last_cycle = cycle >= cat.get_frame_count()
    if is_last_cycle:
        cycle = 0
        cat = random.choice(list(CATS.values()))

    frame = cat.get_frame(cycle)
    delta_x, delta_y = cat.get_pos_delta(cycle)
    cat.play_audio(cycle)

    _, cur_x, cur_y, *_ = window.geometry().split('+')
    new_x = int(cur_x) + delta_x
    new_y = int(cur_y) + delta_y
    window.geometry(f"+{new_x}+{new_y}")

    new_image(window, label, frame)

    window.after(1, event, cat, cycle + 1, window, label)


def setup_window_create_label(window) -> tk.Label:
    window.attributes("-topmost", True)
    widget_drag_free_bind(window)
    label = tk.Label(window, width=100)
    label.pack()

    if platform.system() == "Darwin":
        window.overrideredirect(1)
        window.overrideredirect(0)
        window.wm_attributes("-transparent", True)
        window.wm_attributes("-topmost", True)
        window.config(bg="systemTransparent")

        label.config(bg='systemTransparent')
    elif platform.system() == "Windows":
        window.wm_attributes("-transparentcolor", "black")
        window.overrideredirect(True)

        label.config(bg='black')
    else:
        window.overrideredirect(True)

        label.config(bg='black')

    return label

def create_display(masterWindow = None, location = None):
    if not masterWindow:
        window = tk.Tk()
        window.title("Main")

        label = setup_window_create_label(window)

        window.eval('tk::PlaceWindow . center')

        _, cur_x, cur_y, *_ = window.geometry().split('+')
        x = int(cur_x) - cat_dimensions[0] // 2 + 450
        y = int(cur_y) - cat_dimensions[1] // 2
        window.geometry(f"+{x}+{y}")

        global center_dimensions
        center_dimensions = (x, y)
    else:
        window = tk.Toplevel(masterWindow)
        window.title("New")

        label = setup_window_create_label(window)

        if location:
            window.geometry("+%s+%s" % location)
        else:
            window.geometry("+%s+%s" % center_dimensions)

    window.after(1, update, CATS[CatType.Idle], 0, window, label)
    return window

mainWindow = create_display()
XRange = (30, center_dimensions[0] * 2 - cat_dimensions[0])
YRange = (30, center_dimensions[1] * 2 - cat_dimensions[1])

startTime = time.time()

mainWindow.mainloop()
