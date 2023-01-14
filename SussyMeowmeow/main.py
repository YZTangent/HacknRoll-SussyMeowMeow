#import pyautogui
import random
import tkinter as tk

dimensions = (480, 480)
cycle = 0 #cycle is the index -> which frame we want to currently play
check = 0 # first animation is idle
idle = [1, 2, 3, 4, 5] # idle numbers
jump_Up = [6, 7]
jump_Right = [8, 9]
jump_Left = [10, 11]
roll_Left = [12, 13]
roll_Right = [14, 15]

event_number = random.randrange(1, 3, 1)
impath = './Cat GIFs/'

#window.after is after y ms, do the function action -> can provide parameters as further arguments
# transfer random no. to event
def event(cycle, check, event_number):
    if event_number in idle:
        check = 0
        #print('idle')
        window.after(150, update, cycle, check, event_number)  # no. 1,2,3 = idle
    elif event_number in jump_Up:
        check = 1
        #print('jump up')
        window.after(150, update, cycle, check, event_number)  # no. 4,5 = jump up
    elif event_number in jump_Right:
        check = 2
        #print('jump right')
        window.after(150, update, cycle, check, event_number)  # no. 6,7 = jump right
    elif event_number in jump_Left:
        check = 3
        #print('jump left')
        window.after(150, update, cycle, check, event_number)  # no 8,9 = jump left
    elif event_number in roll_Left:
        check = 4
        #print('roll left')
        window.after(150, update, cycle, check, event_number)  # no. 12,13 = roll left
    elif event_number in roll_Right:
        check = 5
        #print('roll right')
        window.after(150, update, cycle, check, event_number)  # no. 14,15 = roll right


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


def update(cycle, check, event_number):
    # cycle is frame number
    # check is which action 
    # event_number is which event
    # x is the coordinate x

    x = 0
    y = 0

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

    window.after(1, event, cycle, check, event_number)

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

window = tk.Tk()
# call buddy's action gif
idle_Frames = [tk.PhotoImage(file=impath + 'idle.GIF', format='gif -index %i' % (i)) for i in range(6)]  # idle gif
jump_Up_Frames = [tk.PhotoImage(file=impath + 'jumpUp.GIF', format='gif -index %i' % (i)) for i in range(6)]  # sleep gif
jump_Right_Frames = [tk.PhotoImage(file=impath + 'jumpRight.GIF', format='gif -index %i' % (i)) for i in
                 range(14)]  # jump right gif
jump_Left_Frames = [tk.PhotoImage(file=impath + 'jumpLeft.GIF', format='gif -index %i' % (i)) for i in
                 range(14)]  # jump right gif
roll_Left_Frames = [tk.PhotoImage(file=impath + 'rollLeft.GIF', format='gif -index %i' % (i)) for i in
                 range(11)]  # roll left gif
roll_Right_Frames = [tk.PhotoImage(file=impath + 'rollRight.GIF', format='gif -index %i' % (i)) for i in
                 range(11)]  # roll right gif
# window configuration
label = tk.Label(window, bd=0, bg='white')
label.pack()
# place window at center of screen
window.eval('tk::PlaceWindow . center')
window_details = window.geometry().split('+')
x = int(window_details[1]) - dimensions[0] // 2
y = int(window_details[2]) - dimensions[1] // 2
window.geometry('+{}+{}'.format(str(x), str(y)))
# loop the program
window.after(1, update, cycle, check, event_number)
window.mainloop()