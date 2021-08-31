import time
import json
from tkinter import Tk, Label, StringVar, RAISED, Entry

gui = Tk()
gui.geometry("605x480")
gui.title("Typing Speed Test with TKINTER")

game_on = True

text = Label(text="""Set your name and start typing text to start the Speed Test""", bg="yellow")
text.grid(row=0, column=1)

text_str = '''A Policeman, finding a man that had fallen in a fit, said, This man is drunk, and began beating him on the head with his club. A passing Citizen said: Why do you murder a man that is already harmless? Thereupon the Policeman left the man in a fit and attacked the Citizen, who, after receiving several severe contusions, ran away. Alas, said the Policeman, why did I not attack the sober one before exhausting myself upon the other? Thenceforward he pursued that plan, and by zeal and diligence rose to be Chief, and sobriety is unknown in the region subject to his sway.'''

input_text = StringVar()
input_text.set(text_str)

label = Label(gui, textvariable=input_text, relief=RAISED, bg="grey", wraplength=600, justify="center")
label.grid(row=1, column=1)


def convert_str_to_list(string):
    li = list(string.split(" "))
    return li


# scoreboard file
def print_score():
    f = open('data.json')
    data = json.load(f)
    return data


def write_score(x_name, x_score):
    data = print_score()
    data["score"].append({"name": x_name, "score": x_score})
    json_object = json.dumps(data, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)


text_list = convert_str_to_list(str(text_str))

input_text_list = StringVar()
input_text_list.set(text_list)

label_name = Label(gui, text="FIRST SET YOUR NAME", bg="yellow")
label_name.grid(row=3, column=1)

input_name = StringVar()
name = Entry(gui, textvariable=input_name, width=20, font='Helvetica 14').grid(row=4, column=1)

label3 = Label(gui, text="START TYPING HERE", bg="yellow")
label3.grid(row=5, column=1)

E1 = Entry(gui, bd=15, width=65)
E1.grid(row=6, column=1)

score = StringVar()
score.set("YOUR SCORE IS:")

sec = StringVar()
Entry(gui, textvariable=sec, width=2, font='Helvetica 14').grid(row=10, column=1)
sec.set('00')

score_board = Label(gui, textvariable=score, bg="yellow")
score_board.grid(row=11, column=1)

score_all = StringVar()
score_to_str = ""
for i in print_score()["score"]:
    score_to_str += str(f'{i["name"]} {i["score"]}\n')
score_all.set(score_to_str)
score_board_all = Label(gui, textvariable=score_all, bg="grey")
score_board_all.grid(row=12, column=1)


def set_output_text(entry, color):
    text_from_user = StringVar()
    if color:
        fg_color = "green"
    else:
        fg_color = "red"
    text_from_user.set(entry)
    label4 = Label(gui, textvariable=text_from_user, fg=fg_color, wraplength=600, justify="center")
    label4.grid(row=7, column=1)


def countdown_timer():
    times = 600
    while times > -1:
        sec.set(times)
        # Update the time
        gui.update()
        time.sleep(0.05)
        user_entry = convert_str_to_list(E1.get())
        worlds_check = []
        x = 0
        for word in user_entry:
            if word == text_list[x]:
                worlds_check.append(True)
            else:
                worlds_check.append(False)
            color = worlds_check[x - 1]
            x += 1
        set_output_text(user_entry, color)
        if len(E1.get()) != 0:
            if times == 0:
                sec.set('0')
            times -= 1
        final_score = 0
        for value in worlds_check:
            if value:
                final_score += 1

        score.set(f"{input_name.get()}, YOUR SCORE IS: {final_score}")
        if times == 0:
            write_score(input_name.get(), final_score)


countdown_timer()

gui.mainloop()
