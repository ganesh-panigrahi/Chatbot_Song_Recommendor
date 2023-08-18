from tkinter import * 
# GUI 

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

     

    if (user == "happy" or user == "Happy" ): 

        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """Good Vibrations (The Beach Boys) 

             \n Uptown Girl (Billie Joel)  

            \n Eye of the Tiger (Survivor)  

            \n I'm a Believer (The Monkees) 

            \n Girls Just Wanna Have Fun (Cyndi Lauper) 

            \n Livin' on a Prayer (Jon Bon Jovi) 

            \n I Will Survive (Gloria Gaynor) 

            \n Walking on Sunshine (Katrina & The Waves) 

            """) 

    elif (user == "good" or user == "good" ): 

        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """Good Vibrations (The Beach Boys) 

             \n Uptown Girl (Billie Joel) 

            \n Eye of the Tiger (Survivor) 

            \n I'm a Believer (The Monkees) 

            \n Girls Just Wanna Have Fun (Cyndi Lauper) 

            \n Livin' on a Prayer (Jon Bon Jovi) 

            \n I Will Survive (Gloria Gaynor) 

            \n Walking on Sunshine (Katrina & The Waves) 

            """) 

 

    elif (user == "Sad" or user == "sad" ): 

        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """'Nothing Compares 2 U' by Sinéad O'Connor. ... 

                         \n 'Hurt' by Johnny Cash. ... 

                         \n 'Only Love Can Break Your Heart' by Neil Young. ... 

                         \n 'Teardrop' by Massive Attack. ... 

                         \n 'I Know It's Over' by The Smiths. ... 

                         \n 'No Distance Left to Run' by Blur. ... 

                         \n 'The Boxer' by Simon & Garfunkel. ... 

                         \n 'No Name #5' by Elliott Smith. 

            """) 

    elif(user=="busy" or user =="busy"): 

                txt.insert(END,"\n Bot -> Here are some song recommendations for you! \n" + """'Nothing Compares 2 u' by Sinead o'Connor. ... 

                                \n'Stay Flo' by solange. ... 

                                \n'Healing-kygo remix' by Marvin Gaye,Kygo. ... 

                                \n'you got to feed the fire' by usher. ... 

                                \n'two winters long' by Irma Thomas. ... 

                                \n'Dilemma' by Nelly,Kelly Rowland. ... 

                                \n'back from the hospital' by Hot Sugar. ... 

                                """)     

 

    elif(user=="hectic" or user =="hectic"): 

        txt.insert(END,"\n Bot -> Here are some song recommendations for you! \n" + """'Nothing Compares 2 u' by sinead o connor. ... 

                        \n'sleep music' by Marconi Union. ... 

                        \n'Mellomaniac' by Dj Shah-Chillout Mix. ... 

                        \n'Watermark' by Enya. ... 

                        \n'Strawberry' Swing by Coldplay. ... 

                        \n'please dont go' by barcelona. ... 

                        \n'pure shores' by all saints. ... 

                        """)   

                                                   

 

    elif (user == "Angry" or user == "angry" ): 

        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """Kelis - 'I Hate You So Much Right Now' ... 

\n Linkin Park - 'In The End' ... 

\n Taylor Swift - 'We Are Never Ever Getting Back Together' ... 

\n Kanye West - 'Black Skinhead' ... 

\n Pink - 'So What' ... 

\n 30 Seconds To Mars - 'The Kill' ... 

\n Rage Against The Machine - 'Killing In The Name 

            """) 

 

    elif (user == "boring" or user == "boring" ): 

        txt.insert(END, "\n Bot -> Here are some song recommendations for you! \n" + """This Is Sleepy Hallow 

Die Young (feat. 347aidan)Sleepy Hallow. 

2 Mins of Pain (feat. Alborosie)Sleepy Hallow, Alborosie. 

Weight On MeSheff G, Sleepy Hallow. 

Basketball Dreams (Intro)Sleepy Hallow. 

MollySleepy Hallow, Sheff G. 

Breakin Bad (Okay)Sleepy Hallow, Sheff G. 

            """) 

    else: 

        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that") 

  

    e.delete(0, END) 

  

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to College Chatbot Music Recommendation System!", font=FONT_BOLD, pady=4, width=50, height=1).grid( 

    row=0) 

lable2 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Ask your any query about our college", font=FONT_BOLD, pady=4, width=50, height=3).grid( 

    row=1) 

  

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60) 

txt.grid(row=1, column=0, columnspan=2) 

  

scrollbar = Scrollbar(txt) 

scrollbar.place(relheight=1, relx=0.974) 

txt.insert(END, "\n" + "Bot -> Hi there, how can I help? ") 

txt.insert(END, "\n" + "Bot -> How was your day today? ") 

 

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55) 

e.grid(row=2, column=0) 

 

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, 

              command=send).grid(row=2, column=1) 

  

root.mainloop() 


