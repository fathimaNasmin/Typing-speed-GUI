import customtkinter
import tkinter as tk
from tkinter import messagebox as msg
import random

window = customtkinter.CTk()
window.geometry("1000x500")
window.title("Typing Speed Test")



class MainWindow():
    def __init__(self, master):
        self.msg = None
        self.messagebox = None
        self.counter = 0
        self.game_is_on = False
        # Start button
        self.start_btn = customtkinter.CTkButton(master=master, text="START", fg_color="#000000", text_color="#FFF",
                                                 text_font=('Times New Roman', 18), command=self.startTimer)
        self.start_btn.place(relx=0.04, rely=0.08)

        # Reset Button
        self.reset_btn = customtkinter.CTkButton(master=master, text="RESET", fg_color="#000000", text_color="#FFF",
                                                 text_font=('Times New Roman', 18),command=self.reset)
        self.reset_btn.place(relx=0.35, rely=0.08)

        # TextBox to display words from file
        self.words = open("wordslist.txt", 'r').read().split("\n")
        self.display_word = tk.StringVar(master)
        self.display_word.set(random.choice(self.words))
        self.words_txt = tk.Label(master=master, font=('Arial', 20), textvariable=self.display_word)
        self.words_txt.place(relx=0.04, rely=0.27)


        # Entry box to enter each words
        self.entered_word = tk.StringVar(master)
        self.words_entry = customtkinter.CTkEntry(master=master, text_font=('Arial', 18),
                                                  width=450)
        self.words_entry.place(relx=0.04, rely=0.7)
        self.words_entry.configure(state="disabled")
        self.words_entry.bind('<Return>', self.display)

        # Score Board
        self.frame = customtkinter.CTkFrame(master=master, border_color="green", width=350, height=350)
        self.frame.place(relx=0.58, rely=0.08)
        self.score_board = customtkinter.CTkLabel(master=self.frame, text="SCORE BOARD",
                                                  text_font=('Times New Roman', 24),
                                                  anchor="n")
        self.score_board.place(relx=0.25, rely=0.04)

        # Timer label
        self.timer_lbl = customtkinter.CTkLabel(master=self.frame, text="Timer:", text_font=('Times New Roman', 24),
                                                anchor="nw")
        self.timer_lbl.place(relx=0.1, rely=0.12)
        self.timer = customtkinter.CTkLabel(master=self.frame, text="60", text_color="Red",
                                            text_font=('Times New Roman', 24),
                                            anchor="ne")
        self.timer.place(relx=0.47, rely=0.12)

        # Word count
        self.wc_lbl = customtkinter.CTkLabel(master=self.frame, text="Word Count:", text_font=('Times New Roman', 24),
                                             anchor="nw")
        self.wc_lbl.place(relx=0.1, rely=0.21)
        self.wc = customtkinter.CTkLabel(master=self.frame, text="0", text_font=('Times New Roman', 24),
                                         anchor="ne")
        self.wc.place(relx=0.47, rely=0.21)

        # Display final result
        self.result_lbl = customtkinter.CTkLabel(master=self.frame, text="RESULT", text_font=('Times New Roman', 24),
                                                 anchor="n")
        self.result_lbl.place(relx=0.25, rely=0.5)
        self.wpm_lbl = customtkinter.CTkLabel(master=self.frame, text="WPM", text_font=('Times New Roman', 24),
                                              anchor="nw")
        self.wpm_lbl.place(relx=0.1, rely=0.6)
        self.wpm = customtkinter.CTkLabel(master=self.frame, text="0", text_font=('Times New Roman', 24),
                                          anchor="ne")
        self.wpm.place(relx=0.47, rely=0.6)

    def startTimer(self):
        self.game_is_on = True
        sec = int(self.timer.text)
        self.words_entry.configure(state="normal")
        if sec > 0:
            sec = sec - 1
            self.timer.configure(text=sec)
            self.timer.after(1000, self.startTimer)

        else:
            self.game_is_on = False
            self.wpm.configure(text=str(self.counter))
            self.words_entry.configure(state="disabled")
            # self.msg.showinfo(master=self.master, title="Game Over", message="You're Done!")

    def reset(self):
        self.words_entry.delete(0, tk.END)
        self.words_entry.configure(state="disabled")
        self.timer.configure(text="60")
        self.wc.configure(text="0")
        self.wpm.configure(text="0")
        self.display_word.set(random.choice(self.words))
        self.counter = 0

    def display(self, event):
        print(self.display_word.get())
        print(self.words_entry.get())
        if self.words_entry.get() == self.display_word.get():
            self.counter += 1
            print(self.counter)
            self.wc.configure(text=str(self.counter))
        else:
            print("entered wrong word")
        self.words_entry.delete(0, tk.END)
        self.display_word.set(random.choice(self.words))
        self.words_txt.configure(textvariable=self.display_word)





app = MainWindow(window)
window.mainloop()
