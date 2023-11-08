import tkinter as tk
import time


class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")

        # Increase the window size
        self.root.geometry("500x170")

        self.text = "This is a simple typing speed tester. Type this sentence as fast as you can."

        self.prompt_label = tk.Label(root, text=self.text, wraplength=500, justify="left")
        self.prompt_label.pack()

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack()

    def start_typing_test(self):
        self.start_time = time.time()
        self.input_entry.config(state="normal")
        self.input_entry.delete(0, "end")
        self.input_entry.bind("<Return>", self.end_typing_test)
        self.start_button.config(state="disabled")

    def end_typing_test(self, event):
        self.end_time = time.time()
        user_input = self.input_entry.get()
        self.input_entry.config(state="disabled")

        correct_chars = sum(c1 == c2 for c1, c2 in zip(self.text, user_input))
        accuracy = (correct_chars / len(self.text)) * 100
        time_elapsed = self.end_time - self.start_time
        wpm = self.calculate_wpm(user_input, time_elapsed)

        result_text = f"Time elapsed: {time_elapsed:.2f} seconds\nAccuracy: {accuracy:.2f}%\nTyping speed (WPM): {wpm:.2f}"
        self.result_label.config(text=result_text)
        self.start_button.config(state="normal")

    def calculate_wpm(self, text, time_elapsed):
        words = len(text.split())
        characters = len(text)
        minutes = time_elapsed / 60
        wpm = (characters / 5) / minutes
        return wpm


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
