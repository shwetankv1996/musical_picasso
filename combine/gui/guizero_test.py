from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo
import time

def say_my_name():
	welcome_msg.value = my_name.value

def change_text_size(slider_value):
	welcome_msg.size = slider_value

app = App(title="test", width = 600, height = 800, bgcolor = "black", layout = "grid")
#film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid = [7,0],align="left")
#film_description = Text(app, text="Which film?", align="left")
welcome_msg = Text(app, text="Musical Picasso", size=40, color= "#ffa500", grid=[3,0], align = "center")
#my_name=TextBox(app)
#update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start = 10, end = 100, horizontal = False, grid=[0,1], align = "left", visible = False)
my_pic = Picture(app, image = "e14.png", grid = [0,2], align = "center")
app.display()
