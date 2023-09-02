import tkinter
import random
import pandas as pd

BG_COLOR = "wheat3"

current_card = {}

score = -1

def score_title():
    global score
    score += 1
    window.title(f"Çalışılan Kelime Sayısı: {score} **UYGAR YILANLI**")


def next_word():
    global current_card
    current_card = random.choice(to_dict)
    canvas.itemconfig(card_title, text="ENGLISH", fill="white")
    canvas.itemconfig(card_text, text=current_card["ENGLISH"], fill="black")


def flip_card():
    canvas.itemconfig(card_title, text="TÜRKÇE", fill="white")
    canvas.itemconfig(card_text, text=current_card["TÜRKÇE"], fill="black")


#DATAYI İÇERİ AKTARMA
read_csv = pd.read_csv("words.csv", encoding="utf-8")
to_dict = read_csv.to_dict(orient="records")


#EKRAN AYARLARI
window = tkinter.Tk()
window.title(f"Çalışılan Kelime Sayısı: 0 **UYGAR YILANLI**")
window.config(bg=BG_COLOR, padx=20, pady=20)


#KART AYARLARI
canvas = tkinter.Canvas(width=350, height=250, bg="SteelBlue", highlightthickness=3)
card_text = canvas.create_text(175, 150, text="Welcome!", font=("Ariel", 35, "italic"), fill="white")
card_title = canvas.create_text(175, 60, text="Hello", font=("Ariel", 50, "bold"), fill="black")
canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=3)


#BUTONLAR
true_image = tkinter.PhotoImage(file="images/true.png")
false_image = tkinter.PhotoImage(file="images/false.png")

true_button = tkinter.Button(image=true_image, bg=BG_COLOR, highlightthickness=0, command= lambda : [next_word(), score_title()])
true_button.grid(row=1, column=2)
false_button = tkinter.Button(image=false_image, bg=BG_COLOR, highlightthickness=0, command=flip_card)
false_button.grid(row=1, column=0)


window.mainloop()

