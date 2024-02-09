from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
title_text = "Timer"
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    title.config(text='Timer')
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmarks.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, title_text
    reps += 1

    work = WORK_MIN * 60
    s_break = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(l_break)
        title_text = "It's Time For A Long Break."
        title.config(text=title_text, fg=RED)
    elif reps % 2 == 0:
        count_down(s_break)
        title_text = "It's Time For A Short Break."
        title.config(text=title_text, fg=PINK)
    else:
        count_down(work)
        title_text = "Let's Put In The Hard Work."
        title.config(text=title_text, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    minutes = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f'{minutes}:{sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check = ''
        for _ in range(math.floor(reps/2)):
            check += " ✔"
        checkmarks.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(height=500, width=1000)
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'), width=30)
title.grid(row=1, column=1)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 125, image=img)
timer_text = canvas.create_text(100, 160, text='00:00', fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=2, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=3, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=3, column=2)

checkmarks = Label(text='', fg='green', bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
checkmarks.grid(row=4, column=1)

window.mainloop()