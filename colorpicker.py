import tkinter as tk
from tkinter import ttk
import random
import time

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Színválasztó játék")

        self.colors = ["red", "green", "blue", "yellow", "black", "white", "orange", "purple", "pink"]
        self.available_colors = self.colors[:4] 

        self.correct_color = ""
        self.start_time = None
        self.best_time = None
        self.current_word = ""

        self.create_widgets()
        self.new_round()
    
    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="Szó", font=("Arial", 20), width=15)
        self.word_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.grid(row=1, column=0, columnspan=2, pady=10)
        self.entry.bind("<Return>", self.check_answer)

        self.timer_label = tk.Label(self.root, text="Eltelt idő: 0.0 mp", font=("Arial", 12))
        self.timer_label.grid(row=2, column=0, pady=10)

        self.best_label = tk.Label(self.root, text="Legjobb idő: N/A", font=("Arial", 12))
        self.best_label.grid(row=2, column=1, pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12), fg="red")
        self.feedback_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.color_count_label = tk.Label(self.root, text="Színek száma:", font=("Arial", 12))
        self.color_count_label.grid(row=4, column=0, pady=10)
        
        self.color_count = tk.IntVar(value=4)
        self.color_dropdown = ttk.Combobox(self.root, textvariable=self.color_count, values=[2, 3, 4, 5, 6, 7, 8, 9], state="readonly")
        self.color_dropdown.grid(row=4, column=1, pady=10)
        self.color_dropdown.bind("<<ComboboxSelected>>", self.update_color_count)
    
    def update_color_count(self, event=None):
        count = self.color_count.get()
        self.available_colors = self.colors[:count]
        self.new_round()
    
    def new_round(self):
        color_text = random.choice(self.available_colors)
        color_value = random.choice(self.available_colors)

        self.correct_color = color_value
        self.current_word = color_text

        self.word_label.config(text=color_text, fg=color_value)
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)

        self.start_time = time.time()
    
    def check_answer(self, event=None):
        user_input = self.entry.get().strip().lower()
        elapsed_time = round(time.time() - self.start_time, 2)
        
        if user_input == self.correct_color:
            self.feedback_label.config(text="Helyes!", fg="green")

            if self.best_time is None or elapsed_time < self.best_time:
                self.best_time = elapsed_time
                self.best_label.config(text=f"Legjobb idő: {self.best_time} mp")
            
            self.timer_label.config(text=f"Eltelt idő: {elapsed_time} mp")
            self.root.after(1000, self.new_round)  
        else:
            self.feedback_label.config(text=f"Helytelen! A helyes válasz: {self.correct_color}", fg="red")
            self.root.after(2000, self.new_round) 
    
if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()