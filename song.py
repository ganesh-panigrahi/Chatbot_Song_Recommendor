from tkinter import *

root = Tk()

root.title("Chatbot")

BG_GRAY = "#ABB2B9"

BG_COLOR = "#17202A"

TEXT_COLOR = "#EACEEE"

FONT = "Helvetica 14"

FONT_BOLD = "Helvetica 13 bold"

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    if (user == "happy"):
        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """Good Vibrations (The Beach Boys)
        \n Uptown Girl (Billie Joel)
        \n Eye of the Tiger (Survivor)
        \n I'm a Believer (The Monkees)
        \n Girls Just Wanna Have Fun (Cyndi Lauper)
        \n Livin' on a Prayer (Jon Bon Jovi)
        \n I Will Survive (Gloria Gaynor)
        \n Walking on Sunshine (Katrina & The Waves)
        """)
    elif (user == "good"):
        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """Good Vibrations (The Beach Boys)
        \n Uptown Girl (Billie Joel)
        \n Eye of the Tiger (Survivor)
        \n I'm a Believer (The Monkees)
        \n Girls Just Wanna Have Fun (Cyndi Lauper)
        \n Livin' on a Prayer (Jon Bon Jovi)
        \n I Will Survive (Gloria Gaynor)
        \n Walking on Sunshine (Katrina & The Waves)
        """)
    elif (user == "sad"):
        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """'Nothing Compares 2 U' by Sinéad O'Connor.
        \n 'Hurt' by Johnny Cash.
        \n 'Only Love Can Break Your Heart' by Neil Young.
        \n 'Teardrop' by Massive Attack.
        \n 'I Know It's Over' by The Smiths.
        \n 'No Distance Left to Run' by Blur.
        \n 'The Boxer' by Simon & Garfunkel.
        \n 'No Name #5' by Elliott Smith.
        """)
    elif (user == "hi"):
        txt.insert(END,"\n Bot -> Oh Hi !!! \n So, in which mood are you now in? \n Are you happy / sad / good / busy ? \n Please tell me I will recommend best songs for you as per your mood !!! \n")
    elif (user == "busy"):
        txt.insert(END,"\n Bot -> Here are some song recommendations for you! \n" + """'Nothing Compares 2 u' by Sinead o'Connor.
        \n'Stay Flo' by solange.
        \n'Healing-kygo remix' by Marvin Gaye,Kygo.
        """)
    else:
        txt.insert(END, "\n Bot -> I'm sorry, I didn't understand. Please try again.")
        
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)

# Send button
send_btn = Button(root, text="Send", font=FONT_BOLD, bg=BG_COLOR, fg=TEXT_COLOR, command=send)

# Entry box
e = Entry(root, font=FONT)

# Place components on the screen
txt.pack(fill=BOTH, expand=True)
e.pack(side=LEFT, padx=20, pady=20)
send_btn.pack(side=RIGHT, padx=20, pady=20)

root.mainloop()
