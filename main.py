from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 4
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_seconds = LONG_BREAK_MIN
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_seconds = SHORT_BREAK_MIN
    elif reps % 1 == 0:
        title_label.config(text="Work", fg=GREEN)
        count_seconds = WORK_MIN
    count_down(count_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    # Always have seconds displayed in two digits
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        count -= 1
        global timer
        timer = window.after(1000, count_down, count)
    else:
        checks = ""
        work_sessions_completed = (reps + 1) // 2
        for i in range(work_sessions_completed):
            checks += "✔"
        checkmarks.config(text=checks)

        if reps == 8:
            reset_timer()

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0, borderwidth=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), bg=GREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), bg=GREEN, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

window.mainloop()
