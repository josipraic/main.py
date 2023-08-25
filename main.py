import nltk
from nltk.corpus import words
from tkinter import *
import random


nltk.download('words')
word_list = words.words()


timer = None
timer_running = False
score = 0
current_word = ""

def start_timer():
    global timer_running, score, current_word
    if not timer_running:
        timer_running = True
        score = 0
        start_button.config(state="disabled")
        current_word = random.choice(word_list)
        window_word_label.config(text=f"{current_word}")
        window_score_label.config(text=f"Score: {score}")
        count_down(60)

def count_down(count):
    global timer, timer_running, word_list, score, current_word
    global current_word
    if count > -1:
        window_main_label.config(text=f"seconds:{count}")
        timer = window.after(1000, count_down, count - 1)
        user_input = word_entry.get().strip()
        if user_input.lower() == current_word.lower():
            score += 1
            current_word = random.choice(word_list)
            window_word_label.config(text=f"{current_word}")
            word_entry.delete(0, "end")
            window_score_label.config(text=f"Score: {score}")
    else:
        timer_running = False
        start_button.config(state="normal")

def reset_timer():
    global timer_running
    window.after_cancel(timer)
    window_main_label.config(text="START THE TEST!")
    window_word_label.config(text="Word:")
    window_score_label.config(text="Score:")
    start_button.config(state='normal')
    timer_running = False


window = Tk()
window.title("Typing Speed Test")

window_main_label = Label(text="START THE TEST!", font=("Helvetica", 24), fg="blue")
window_main_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

window_score_label = Label(text=f"Score:", font=("Helvetica", 18), fg="black")
window_score_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

window_word_label = Label(text=f"Word:", font=("Helvetica", 20), fg="green")
window_word_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

word_entry = Entry(width=40)
word_entry.grid(row=3, column=0, padx=10, pady=(50, 10), columnspan=2)

start_button = Button(text="Start!", width=30, font=("Helvetica", 12), fg="red", command=start_timer)
start_button.grid(row=4, column=0, padx=10, pady=(60, 10))

reset_button = Button(text="Reset", width=30, font=("Helvetica", 12), fg="blue", command=reset_timer)
reset_button.grid(row=4, column=1, padx=10, pady=(60, 10))


window.columnconfigure(0, weight=1)

window.geometry("800x500")
window.config(padx=50, pady=50)

window.mainloop()