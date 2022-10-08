import customtkinter
import tkinter

window = customtkinter.CTk()
window.geometry("1000x500")
window.title("Typing Speed Test")

#TODO: set timer on button click
#TODO:after timer runsout show a messagebox

class MainWindow:
    def __init__(self, master):
        # Start button
        self.start_btn = customtkinter.CTkButton(master=master, text="START", fg_color="#000000", text_color="#FFF",
                                                 text_font=('Times New Roman', 18), command=self.startTimer)
        self.start_btn.place(relx=0.04, rely=0.08)

        # Reset Button
        self.reset_btn = customtkinter.CTkButton(master=master, text="RESET", fg_color="#000000", text_color="#FFF",
                                                 text_font=('Times New Roman', 18))
        self.reset_btn.place(relx=0.35, rely=0.08)

        # label to display words for file
        self.words_txt = customtkinter.CTkTextbox(master=master, height=200, width=450, border_width=2,
                                                  border_color="black", text_font=('Arial', 20))
        self.words_txt.place(relx=0.04, rely=0.17)
        self.words_txt.insert(tkinter.END, "Words\nfrom\nfile")

        # Entry box to enter each words
        self.words_entry = customtkinter.CTkEntry(master=master, text_font=('Arial', 18),
                                                  placeholder_text="Type Words Here...", width=450)
        self.words_entry.place(relx=0.04, rely=0.7)

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
        self.timer = customtkinter.CTkLabel(master=self.frame, text="60", text_color="Red", text_font=('Times New Roman',24),
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
        sec = int(self.timer.text)
        if sec > 0:
            sec = sec - 1
            self.timer.configure(text=sec)
            self.timer.after(1000, self.startTimer)


app = MainWindow(window)
window.mainloop()
