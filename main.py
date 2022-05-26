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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_label.config(text="", fg=GREEN, font=(FONT_NAME, 18, "bold"))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0 :
        count_down(long_break_sec)
        text_label.config(text= "Long Break", bg=YELLOW, fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text="Short Break", bg=YELLOW, fg= PINK)
    else:
        count_down(work_sec)
        text_label.config(text="Work Time!", bg=YELLOW, fg= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"{count_sec:02d}"
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✓"
            check_label.config(text=check_mark, fg=GREEN, font=(FONT_NAME, 18, "bold"))




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro by Aquomedirion")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# Text Label
text_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
text_label.config(bg=YELLOW)
text_label.grid(column=1, row=0)

# Check Label
check_label = Label(text="", fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_label.config(bg=YELLOW)
check_label.grid(column=1, row=4)

# Start Button
button = Button(text="Start", command=start_timer)
button.grid(column=0, row=3)

# Reset Button
button = Button(text="Reset", command=reset_timer)
button.grid(column=2, row=3)

window.mainloop()
