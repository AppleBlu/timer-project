import tkinter as tk
import math

FONT = ("Technology", 35)
clock_timer = None

# Window creation
window = tk.Tk()
window.title("Timer")
window.config(bg="Black", width=300, height=75, padx=50, pady=10)

# Label creation
timer = tk.Label(pady=20, padx=20)
timer.config(fg="White", bg="Black", text="00:00", font=FONT)
timer.grid(row=0, column=1)

# Spinbox creation
time_entry = tk.Spinbox(from_=0, to=120, width=5, bg="Black", highlightthickness=0, fg="White")
time_entry.grid(row=1, column=1)

# Canvas creation
canvas = tk.Canvas(width=100, height=50, highlightthickness=0, bg="Black")
timer_text = canvas.create_text(50, 25, text='00:00', font=FONT, fill='White')
canvas.grid(row=0, column=1)


def reset_timer():
    """Resets the timer"""
    window.after_cancel(clock_timer)
    canvas.itemconfig(timer_text, text="00:00")


def start_action():
    clock_time = time_entry.get()
    start_timer(int(clock_time) * 60)


def start_timer(time):
    """Starts the timer"""
    global clock_timer
    count_min = math.floor(int(time) / 60)
    count_seconds = int(time) % 60

    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    # Showing the timer
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if time > 0:
        clock_timer = window.after(1000, start_timer, int(time) - 1)


# Button creation
reset = tk.Button()
reset.config(text="Reset", bg="Black", fg="White", highlightthickness=0, command=reset_timer)
reset.grid(row=0, column=0)

start = tk.Button()
start.config(text="Start", bg="Black", fg="White", highlightthickness=0, command=start_action)
start.grid(row=0, column=2)

window.mainloop()
