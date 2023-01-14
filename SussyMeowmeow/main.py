#import pyautogui
import random
import tkinter as tk
from PIL import Image, ImageTk
import time

cat_dimensions = (120, 120)
center_dimensions = None
cycle = 0 #cycle is the index -> which frame we want to currently play
check = 0 # first animation is idle
idle = [1, 2, 3, 4, 5] # idle numbers
jump_Up = [6, 7]
jump_Right = [8, 9]
jump_Left = [10, 11]
roll_Left = [12, 13]
roll_Right = [14, 15]
spawnInterval = 5

event_number = random.randrange(1, 3, 1)
impath = '../Cat GIFs/'

#window.after is after y ms, do the function action -> can provide parameters as further arguments
# transfer random no. to event
def event(cycle, check, event_number, window, label):
    if event_number in idle:
        check = 0
        #print('idle')
        window.after(150, update, cycle, check, event_number, window, label)  # no. 1,2,3 = idle
    elif event_number in jump_Up:
        check = 1
        #print('jump up')
        window.after(150, update, cycle, check, event_number, window, label)  # no. 4,5 = jump up
    elif event_number in jump_Right:
        check = 2
        #print('jump right')
        window.after(150, update, cycle, check, event_number, window, label)  # no. 6,7 = jump right
    elif event_number in jump_Left:
        check = 3
        #print('jump left')
        window.after(150, update, cycle, check, event_number, window, label)  # no 8,9 = jump left
    elif event_number in roll_Left:
        check = 4
        #print('roll left')
        window.after(150, update, cycle, check, event_number, window, label)  # no. 12,13 = roll left
    elif event_number in roll_Right:
        check = 5
        #print('roll right')
        window.after(150, update, cycle, check, event_number, window, label)  # no. 14,15 = roll right


# making gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
    # cycle is the index, frames is the array, event_number is. what event
    # first_num and last_num is just for random calculation
    #debug_event(event_number)
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


def update(cycle, check, event_number, window, label):
    # cycle is frame number
    # check is which action 
    # event_number is which event
    # x is the coordinate x

    x = 0
    y = 0
    global startTime
    if time.time() - startTime >= spawnInterval and window == mainWindow:
        create_display(mainWindow, (random.randrange(XRange[0], XRange[1], 1), random.randrange(YRange[0], YRange[1], 1)))
        startTime = time.time()
    # idle
    if check == 0:
        frame = idle_Frames[cycle]
        cycle, event_number = gif_work(cycle, idle_Frames, event_number, 1, 15)
    # jump up
    elif check == 1:
        frame = jump_Up_Frames[cycle]
        cycle, event_number = gif_work(cycle, jump_Up_Frames, event_number, 1, 15)
        if cycle < len(jump_Up_Frames) / 2:
            y = -2
        else:
            y = 2
    # jump right
    elif check == 2:
        frame = jump_Right_Frames[cycle]
        cycle, event_number = gif_work(cycle, jump_Right_Frames, event_number, 1, 15)
        x = 2
        if cycle < len(jump_Right_Frames) / 2:
            y = -2
        else:
            y = 2
    # jump left
    elif check == 3:
        frame = jump_Left_Frames[cycle]
        cycle, event_number = gif_work(cycle, jump_Left_Frames, event_number, 1, 15)
        x = -2
        if cycle < len(jump_Left_Frames) / 2:
            y = -3
        else:
            y = 3
    # roll left
    elif check == 4:
        frame = roll_Left_Frames[cycle]
        cycle, event_number = gif_work(cycle, roll_Left_Frames, event_number, 1, 15)
        x = -3
    # roll right
    elif check == 5:
        frame = roll_Right_Frames[cycle]
        cycle, event_number = gif_work(cycle, roll_Right_Frames, event_number, 1, 15)
        x = 3

    window_details = window.geometry().split('+')
    curr_x = int(window_details[1])
    curr_y = int(window_details[2])
    window.geometry('+{}+{}'.format(str(curr_x + x), str(curr_y + y)))

    label.configure(image=frame)

    # after 1ms, perform event with event_number returned from 

    window.after(1, event, cycle, check, event_number, window, label)

def debug_event(event_number):
    if event_number in idle:
        print('idle')
    elif event_number in jump_Up:
        print('Jump up')
    elif event_number in jump_Left:
        print('Jump left')
    elif event_number in jump_Right:
        print('Jump right')
    elif event_number in roll_Left:
        print('Roll left')
    elif event_number in roll_Right:
        print('Roll right')

def open_image(path):
    gifArray = []
    with Image.open(impath + path) as im: 
        im.seek(0)  # open the first frame

        try:
            while True:
                # append frame to array
                gifArray.append(ImageTk.PhotoImage(im.resize(cat_dimensions)))
                im.seek(im.tell() + 1)
        except EOFError:
            return gifArray  # end of sequence

def create_display(masterWindow = None, location = None):
    if not masterWindow:
        window = tk.Tk()
        window.title("Main")
        label = tk.Label(window, bd=0, bg='white')
        label.pack()
        window.eval('tk::PlaceWindow . center')
        window_details = window.geometry().split('+')
        x = int(window_details[1]) - cat_dimensions[0] // 2
        y = int(window_details[2]) - cat_dimensions[1] // 2
        global center_dimensions
        center_dimensions = (x, y)
        window.geometry('+{}+{}'.format(center_dimensions[0], center_dimensions[1]))
    else:
        window = tk.Toplevel(masterWindow)
        window.title("New")
        label = tk.Label(window, bd=0, bg='white')
        label.pack()
        if location:
            window.geometry('+{}+{}'.format(location[0], location[1]))
        else: 
            window.geometry('+{}+{}'.format(center_dimensions[0], center_dimensions[1]))
    window.after(1, update, cycle, check, event_number, window, label)
    return window

mainWindow = create_display()
XRange = (30, center_dimensions[0] * 2 - cat_dimensions[0])
YRange = (30, center_dimensions[1] * 2 - cat_dimensions[1])

# call buddy's action gif
idle_Frames = open_image('idle.GIF')  # idle gif
jump_Up_Frames = open_image('jumpUp.GIF') # sleep gif
jump_Right_Frames = open_image('jumpRight.GIF')  # jump right gif
jump_Left_Frames = open_image('jumpLeft.GIF') # jump right gif
roll_Left_Frames = open_image('rollLeft.GIF')  # roll left gif
roll_Right_Frames = open_image('rollRight.GIF')  # roll right gif

startTime = time.time()

mainWindow.mainloop()