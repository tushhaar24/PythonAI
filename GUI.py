from cgitb import text as cgitb_text
from cgitb import text
from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    conversation_text.insert(END, 'User--->' + user_val + "\n")
    if bot_val is not None:
        conversation_text.insert(END, "BOT--->" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    send=entry.get()
    bot=action.Action(send)
    conversation_text.insert(END, 'User--->' + send + "\n")
    if bot is not None:
        conversation_text.insert(END, "BOT--->" + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def del_text():
    conversation_text.delete("1.0","end")

# Create the main Tkinter window
root = Tk()
root.title("AI Assistant")
root.geometry("850x950")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Create a Text widget for conversation display
conversation_text = Text(root, width=50, height=8, font=("Arial", 12), wrap=WORD, bg="#356696")
conversation_text.place(x=180, y=480)

# Create a frame for AI Assistant information
frame = LabelFrame(root, padx=160, pady=7, borderwidth=3, relief="raised", bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=15, columnspan=2)


# Add a label and an image to the frame
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bd=2, relief="solid", bg="#6F8FAF")
text_label.grid(row=0, column=0, padx=20, pady=10)

image_path = r"D:\PythonAI\SimbaAI\image\png-clipart-lion-king-lion-king-thumbnail.png"
image = ImageTk.PhotoImage(Image.open(image_path))
image_label = Label(frame, image=image, bg="#6F8FAF")
image_label.grid(row=1, column=0, padx=20, pady=10)

# Create an entry for additional input
entry = Entry(root, justify=CENTER)
entry.place(x=250, y=640, width=350, height=30)

# Create functions for buttons
button_functions = [ask, send, del_text]
button_texts = ['ASK', 'SEND', 'DELETE']

# Create buttons dynamically
for i, (func, text) in enumerate(zip(button_functions, button_texts)):
    button = Button(root, text=text, bg="#356696", pady=16, padx=30, borderwidth=3, relief=SOLID, command=func)
    button.place(x=40 + i * 310, y=720)

# Start the main loop
root.mainloop()
