#import pyautogui
import random
import tkinter as tk

x = 1400
cycle = 0 #cycle is the index -> which frame we want to currently play
check = 1
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
def event(cycle, check, event_number, x):
    if event_number in idle:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3 = idle
    elif event_number in jump_Up:
        check = 1
        print('jump up')
        window.after(100, update, cycle, check, event_number, x)  # no. 4,5 = jump up
    elif event_number in jump_Right:
        check = 2
        print('jump right')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = jump right
    elif event_number in jump_Left:
        check = 3
        print('jump left')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = jump left
    elif event_number in roll_Left:
        check = 4
        print('roll left')
        window.after(100, update, cycle, check, event_number, x)  # no. 12,13 = roll left
    elif event_number in roll_Right:
        check = 5
        print('roll right')
        window.after(100, update, cycle, check, event_number, x)  # no. 14,15 = roll right


# making gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
    # cycle is the index, frames is the array, event_number is. what event
    # first_num and last_num is just for random calculation
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


def update(cycle, check, event_number, x):
    # cycle is frame number
    # check is which action 
    # event_number is which event
    # x is the coordinate x
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    # jump up
    elif check == 1:
        frame = jump_Up[cycle]
        cycle, event_number = gif_work(cycle, jump_Up, event_number, 10, 10)
    # jump right
    elif check == 2:
        frame = jump_Right[cycle]
        cycle, event_number = gif_work(cycle, jump_Right, event_number, 10, 15)
    # jump left
    elif check == 3:
        frame = jump_Left[cycle]
        cycle, event_number = gif_work(cycle, jump_Left, event_number, 1, 1)
    # roll left
    elif check == 4:
        frame = roll_Left[cycle]
        cycle, event_number = gif_work(cycle, roll_Left, event_number, 1, 9)
        x -= -3
    # roll right
    elif check == 5:
        frame = roll_Right[cycle]
        cycle, event_number = gif_work(cycle, roll_Right, event_number, 1, 9)
        x -= -3
    # 480x480 is the window size
    # str(x) + 1050 is the position of the window
    # we only updates x on roll left or roll right because it changes position
    window.geometry('480x480+' + str(x) + '+1050')
    # 480 is sprite size, 1050 is supposed to be screen res
    label.configure(image=frame)

    # after 1ms, perform event with event_number returned from 
    window.after(1, event, cycle, check, event_number, x)


window = tk.Tk()
# call buddy's action gif
idle = [tk.PhotoImage(file=impath + 'idle.GIF', format='gif -index %i' % (i)) for i in range(6)]  # idle gif
jump_Up = [tk.PhotoImage(file=impath + 'jumpUp.GIF', format='gif -index %i' % (i)) for i in range(6)]  # sleep gif
jump_Right = [tk.PhotoImage(file=impath + 'jumpRight.GIF', format='gif -index %i' % (i)) for i in
                 range(14)]  # jump right gif
jump_Left = [tk.PhotoImage(file=impath + 'jumpLeft.GIF', format='gif -index %i' % (i)) for i in
                 range(14)]  # jump right gif
roll_Left = [tk.PhotoImage(file=impath + 'rollLeft.GIF', format='gif -index %i' % (i)) for i in
                 range(11)]  # roll left gif
roll_Right = [tk.PhotoImage(file=impath + 'rollRight.GIF', format='gif -index %i' % (i)) for i in
                 range(11)]  # roll right gif
# window configuration
label = tk.Label(window, bd=0, bg='white')
label.pack()
# loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()