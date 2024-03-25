from tkinter import*
from tkinter import ttk
import random
from random import shuffle
from tkinter import messagebox
import pygame
import sqlite3

def getWords():
    # Opens a file named 'words.txt' and extracts all the words in it as list
    # 'words.txt' contains 50000+ dictionary words
   
    filename = "words.txt"    
    fh = open(filename,"r")              # read file
    words = fh.readline().split(" ")     # read the content and split into list
    fh.close()                           # close file handle
    return words

def mapCharacter(word):
    # count each letter in 'word' and return a map of letter against count
    # the key in the returend dictionary is letter in word and the value is the number of times it occurs in the word
   
    wordDict = {}     # initialize dictionary
    for c in word:
        wordDict[c] = wordDict.get(c,0) + 1  # increment current character count in dictionary.
    return wordDict

def canFormWord(possibleCharMap, charMap):
    # checks if 'charMap' is a subset of 'possibleCharMap'
    # both inputs are dictionaries
   
    for c in charMap:
        if c not in possibleCharMap:  # return false if a character in 'charMap' is not in 'possibleCharMap'
            return False
        elif charMap[c] > possibleCharMap[c]:  # return false if a character occurs more in 'charMap' than in 'possibleCharMap'
            return False
    return True
def getNLetterWords(words,possibleCharMap, n):
    # returns all n-letter words that can formed from the letters in dictionary 'possibleCharMap'
    # words is a list of dictionary words
   
    nLetterWords = []       # initialize result list
    for word in words:    # go through each word in words
        if len(word) == n and canFormWord(possibleCharMap,mapCharacter(word)): # check if current word is n-letter and also if the word is a subset of possibleCharMap
            nLetterWords.append(word)     # add current word to the result list once it passes the above checks
           
    return nLetterWords
   
def solveWordCrossPuzzle(possibleChars, *wordsLength):
    # possibleChars is a string of charcters from which to construct all words
    # *wordsLength is a variable parameter that represents a list of word lengths to be constructed
    # this function returns list of  all dictionary words that can be constructed from 'possibleChars'.
    # The length of the returned words must be in 'wordsLength'
   
    lengthMap = {}
    possibleChars = possibleChars.lower()  # convert possibleChars to lower case
    possibleCharMap = mapCharacter(possibleChars) # map characters in 'possibleChar'
    for i in wordsLength:
        # map the number in wordsLength
        lengthMap[i] = lengthMap.get(i,0) + 1
       
    words = getWords()  # get all dictionary words
    result = []
    for i in lengthMap:
        result = result + getNLetterWords(words,possibleCharMap,i) # get words for each word length
    return result

res=solveWordCrossPuzzle("disco",3,3,3,4)
print(res)

word=Tk()
word.geometry("500x500")
word.title("Word Puzzle")
word.configure(bg="pink")
#lb1=Label(word,font='times 20')
#lb1.place(x=100 ,y=30)
canvas1 = Canvas( word, width = 480, height = 490) 
img = PhotoImage(file='bd2.png')
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0,image=img,anchor = "nw")

def close_window():
    word.destroy()

    
pygame.mixer.init()

timer_label = Label(word, text="", bg="yellow", font=("Helvetica", 16))
timer_label.place(x=370,y=400)
def start_timer():
        update_timer(60)

def plright():
   pygame.mixer.music.load("check.mp3")
   pygame.mixer.music.play()

def plwrong():
   pygame.mixer.music.load("wrong.mp3")
   pygame.mixer.music.play()
#user scores saving in database
nam=StringVar()
name=Entry(word,textvariable=nam,fg="black",bg="white",font=("Helvetica", 15))

def savename():
    global count,name,fnm,ok
    playernm=name.get()
    fnm.place_forget()
    ok.place_forget()
    lb2=Label(word,text="Saved score!!")
    lb2.place(x=110,y=230)
    lb2.after(2000, lambda: lb2.destroy())
    name.place_forget()
    save_score(playernm, count)
    # To retrieve and display all the scores:
    
    #top_scores = get_top_scores()
    #print("Top scores are")
    #for rank, (username, score) in enumerate(top_scores, start=1):
        #print(f"Rank {rank}: {username} - Score: {score}")

    
    #word.after(10000, close_window)



fnm=Label(word,text=f"enter name:",fg="black",bg="orange",font=("Helvetica", 15),)
ok=Button(word,text="click ok to save your name",fg="black",bg="orange",command=savename)

def update_timer(counter):
    global count,boy,nam
    if counter > 0:
        timer_label.config(text=f"Time Left: {counter} seconds")
        word.after(1000, update_timer, counter - 1)
    else:
        timer_label.config(text="Time's up!")
        #messagebox.showinfo("Time's Up", "Your time is up!")
        stop()
        del1()
        progress_bar.destroy()
        e.place_forget()
        b1.place_forget()
        bT2.place_forget()
        b3.place_forget()
        b4.place_forget()
        b5.place_forget()
        b6.place_forget()
        byt.place_forget(); 
        bt2.place_forget()
        bt1.place_forget()
        fl=Label(word,text=f"points earned={count}",fg="black",bg="orange",font=("Helvetica", 15),)
        fl.place(x=300,y=200)
        
        
        
        finallbl=Label(text="Time's Up Your time is up!",font=("Helvetica", 15),fg="red",bg="white")
        finallbl.place(x=50,y=230)
        finallbl.after(1000, lambda: finallbl.destroy())
        boy = canvas1.create_image(400, 200, image=bi)
        if count>0:
            fnm.place(x=120,y=200)
        
            name.place(x=125,y=250)
            
            ok.place(x=130,y=300)
            move_boy()
        else:
            close_window()



    
    
class Caps:
    def __init__(self):
        self.radius = random.randint(7, 20)
        self.x = random.randint(self.radius, 600 - self.radius)
        self.y = -self.radius
        self.image_path = random.choice([ "cap1.png",])
        self.image = PhotoImage(file=self.image_path)
        self.id = canvas1.create_image(self.x, self.y, image=self.image)
        self.speed = random.randint(2, 5)

    def move(self):
        self.y += self.speed
        canvas1.move(self.id, 0, self.speed)
        if self.y - self.radius > 400:
            self.reset()

    def reset(self):
        canvas1.delete(self.id)
        self.radius = random.randint(7, 20)
        self.x = random.randint(self.radius, 600 - self.radius)
        self.y = -self.radius
        self.image_path = random.choice(["cap1.png"])
        self.image = PhotoImage(file=self.image_path)
        self.id = canvas1.create_image(self.x, self.y, image=self.image)
        self.speed = random.randint(2, 5)
class Balloon:
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas=canvas
        self.image=canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity=xVelocity
        self.yVelocity=yVelocity
       
    def move(self):
        coordinates=self.canvas.coords(self.image)
   
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity=-self.xVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[0]<0):
            self.yVelocity=-self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)

class Strip:
    def __init__(self, canvas, x, y, width, height, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_rectangle(x, y, x + width, y + height, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if (coordinates[2] >= self.canvas.winfo_width()) or (coordinates[0] <= 0):
            self.xVelocity = -self.xVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)
        if (coordinates[3] >= self.canvas.winfo_height()) or (coordinates[1] <= 0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)

strip_1 = Strip(canvas1, 10, 350, 200, 10, 3, 0, "red")
strip_2 = Strip(canvas1, 10, 400, 100, 10, 4, 0, "blue")
strip_3 = Strip(canvas1, 10, 450, 150, 10, 2, 0, "green")

balloon_1=Balloon(canvas1,0,0,100,1,1,"red")
balloon_2=Balloon(canvas1,0,0,50,4,3,"blue")
balloon_3=Balloon(canvas1,0,0,75,3,4,"green")

# Create a list to store Balloon instances
cap = []
def stani():
    strip_1.move()
    strip_2.move()
    strip_3.move()
    balloon_1.move()
    balloon_2.move()
    balloon_3.move()
    if not stop_st:
        word.after(100, stani)
# Create function to add new balloons and move existing ones
def animate():
    new_balloon = Caps()
    cap.append(new_balloon)
    while len(cap) > 25:
        old_circle = cap.pop(0)
        old_circle.reset()
    
    for c in cap:
        c.move()

    if not stop_animation:
        word.after(100, animate)

# Function to stop the animation
def stop():
    global stop_animation
    stop_animation = True
def del1():
    global stop_st
    stop_st=True

answer=getWords()

words_6=[]

for i in answer:
    if(len(i)==6):
        words_6.append(i)


#Entry label
answer1=StringVar()
e=Entry(word,borderwidth="1",bg="white",font="Canada 14",textvariable=answer1)


def Random_word_creation():
 
        num=random.randint(0,len(words_6))    
       
        rw=words_6[num]  #random word is called
        sw=list(rw)
        shuffle(sw)
        return ''.join(sw)
   
current_sw=Random_word_creation()
   
def entry_update(text):
    #entry.delete(0,END)
    e.insert(END,text)
   
def button_click(num):
    stop_animation=False
    animate()
    return entry_update(num)
       
   

   
b1=Button(word,borderwidth=10,bg="pink",font=("Helvetica", 14),fg="magenta",activeforeground="green",activebackground="black"
          ,text=current_sw[0],command=lambda:entry_update(current_sw[0]))


bT2=Button(word,borderwidth=10,bg="olive",font=("Helvetica", 14),fg="magenta",activeforeground="green",activebackground="black",text=current_sw[1],command=lambda:button_click(current_sw[1]))


b3=Button(word,borderwidth=10,bg="blue",font=("Helvetica", 14),fg="magenta",activeforeground="green",activebackground="black",text=current_sw[2],command=lambda:button_click(current_sw[2]))



b4=Button(word,borderwidth=10,bg="white",font=("Helvetica", 14),fg="magenta",activeforeground="green",activebackground="black",text=current_sw[3],command=lambda:button_click(current_sw[3]))


b5=Button(word,borderwidth=10,bg="orange",font=("Helvetica", 14),fg="magenta",activeforeground="green",activebackground="black",text=current_sw[4],command=lambda:button_click(current_sw[4]))


b6=Button(word,borderwidth=10,bg="yellow",font=("Helvetica", 14),fg="magenta",activeforeground="green",
          activebackground="black",text=current_sw[5],command=lambda:button_click(current_sw[5]))




word_count=0
chances=5
progress_bar=ttk.Progressbar(word,orient="horizontal",mode="determinate",length=200)



count=0
def update_progress():
        global word_count
        progress=(word_count/6)*100
        progress_bar["value"]=progress
def winner_loser():
   global word_count,chances,count
   #update_progress()
   if(chances==0):
       lb3=Label(word,text="Sorry!!Better luck next time!!",bg="blue")
       lb3.place(x=110,y=300)
       lb3.after(2000, lambda: lb3.destroy())
       reset()
   
   elif(word_count==6):
      lb2=Label(word,text="Congratulations!you won!!",bg="orange")
      count+=20
      pro_s=Label(word,text="Earned 20 Extra!!",bg="orange")
      progress_bar["value"]=0
      lb2.place(x=110,y=400)
      lb2.after(2000, lambda: lb2.destroy())
      pro_s.place(x=110,y=0)
      pro_s.after(2000, lambda: lb2.destroy())
      
      reset();
guessed_words=set()
def check():
        global word_count,chances,count,guessed_words
        flag=0
        result=solveWordCrossPuzzle(current_sw,2,3,4,5,6)
        user_input=e.get()
        

        if user_input not in guessed_words:
            guessed_words.add(user_input)
            for i in result:
                if user_input==i:
                    flag=1
               
               
            if(flag==1):
                word_count=word_count+1
                update_progress()
                plright()
                lb2=Label(word,text="Congratulations!that is correct!",bg="green")
                lb2.place(x=110,y=300)
                lb2.after(2000, lambda: lb2.destroy())
                count+=10
                e.delete(0,END)
                winner_loser()
            else:
                plwrong()
                chances=chances-1
                lb3=Label(word,text="Wrong guess...Try again",bg="red")
                lb3.place(x=110,y=300)
                lb3.after(2000, lambda: lb3.destroy())
                e.delete(0,END)
                winner_loser()

        else:
            lb4=Label(word,text="You have already guessed this word!",bg="pink")
            plwrong()
            lb4.place(x=110,y=300)
            lb4.after(2000,lambda:lb4.destroy())
            e.delete(0,END)
           
                   
           
           
def reset():
        global word_count,chances,guessed_words
        words_count=0
        chances=6
        guessed_words.clear()
        progress_bar["value"]=0
        e.delete(0,END)
        global current_sw
        current_sw=Random_word_creation()
        
        b1.configure(text=current_sw[0])
        bT2.configure(text=current_sw[1])
        b3.configure(text=current_sw[2])
        b4.configure(text=current_sw[3])
        b5.configure(text=current_sw[4])
        b6.configure(text=current_sw[5])
def clear():
    e.delete(0,END)
def myDelete():
    global myLabel,myButton,b2
   # myLabel.place_forget()
    myButton.place_forget()
    b2.place_forget()
    progress_bar.place(x=150,y=50)
    e.place(x=130,y=10)
    b1.place(y=200,x=200,width=80,height=50)
    bT2.place(y=260,x=200,width=80,height=50)
    b3.place(y=200,x=100,width=80,height=50)
    b4.place(y=200,x=300,width=80,height=50)
    b5.place(y=260,x=100,width=80,height=50)
    b6.place(y=260,x=300,width=80,height=50)
    byt.place(x=205,y=320)     
    bt2.place(x=100,y=320)
    bt1.place(x=300,y=320)
    start_timer()
text="Harry wants to celebrate his birthday but lacks some\n money.Help him to win exciting birthday gifts!!"
        
def myClick():
    global myLabel
    global myButton
    myLabel = Label(
        bg="red",fg='black',font=("Lucida Calligraphy", 12)
    )
    
    myLabel.place(x=5,y=290)
    myLabel.after(13000,lambda:myLabel.destroy())
    update_text()
    myButton.place_forget()
   
def update_text(index=0):
    global myLabel,text
    if index < len(text):
        myLabel.config(text=text[:index+1])  # Update label text up to the current index
        word.after(100, update_text, index+1)  # Schedule the next update
    else:
        myLabel.config(text=text)  # Set the final text when all letters are displayed
               
       
myButton = Button(word, text="Be Ready to boost your brain!!", command=myClick, bg="magenta",fg="olive",font=("Helvetica", 14))
myButton.place(x=150,y=0)



b2 = Button(word, text="Start", command=myDelete, bg="pink",font=("Helvetica", 14))
b2.place(x=205,y=100)     
       
byt=Button(word,borderwidth="5",height="1",width="10",text="Clear",activeforeground="green",activebackground="black",command=clear)

bt1=Button(word,borderwidth="5",height="1",width="10",text="Check",activeforeground="green",activebackground="black",command=check)

bt2=Button(word,borderwidth="5",height="1",width="10",text="Reset",activeforeground="green",activebackground="black",command=reset)
bi = PhotoImage(file='boy.png')

# Display the boy's image on the canvas


# Function to move the boy's image from right to left
def move_boy():
    global boy
   # canvas1.delete("mybut")
    x, _ = canvas1.coords(boy)  # Get current x-coordinate
    canvas1.move(boy, -5, 0)  # Move the boy's image 5 pixels to the left
    if x < 0:
        # Reset the boy's image to the right side when it goes off-screen
        canvas1.coords(boy, 400, 200)

    word.after(100, move_boy)

    
stop_animation=False
stop_st=False
stani()
def infogm():
     description=(  "Step into a world of linguistic challenges\n"
                    "and mental prowess with our captivating word game!\n "
        "Immerse yourself in the excitement as you encounter a canvas of\n"
                    "jumbled letters gracefully laid out \n"
        "on six distinct buttons, each beckoning you to unravel its\n"
                    "hidden treasures.\n"
        "Your mission, should you choose to accept, is to rearrange\n"
                    "these enigmatic letters into meaningful words.\n "
        "With every correct word gracefully woven from the chaos,\n"
                    "the air tingles with the sweet symphony of success,\n "
        "and you earn a commendable 10 points for each linguistic triumph.\n"
        "But wait, there's more! The thrill escalates as you confront the"
                    "\never-advancing progress bar, a relentless "
        "\n measure of your linguistic dexterity. Complete this bar, and"
                    "\nwitness the burst of euphoria as an additional "
        "\n 20 points cascade into your score, elevating your achievement"
                    "\n to new heights.\n"
        "As you navigate through the labyrinth of jumbled letters, each "
                    "\n correct word not only adds to your point tally "
        "\n but also unlocks a sense of accomplishment. Challenge yourself,"
                    "\n expand your vocabulary, and revel in the delightful "
        "\n fusion of intellect and entertainment that defines our "
                    "\n extraordinary word game. Let the linguistic "
                    "\n journey begin!"
    )
     return description
    
def aboutg():
    info=Toplevel(word,width=500,height=600)
    info.title("ABOUT THE GAME")
   
    game_description = Text(info,font=("Rage Italic", 14), wrap=WORD,bg="yellow",fg="purple", )
    game_description.place(x=10, y=10)

    # Insert the game description into the text widget
    game_description.insert(END, infogm())

    # Disable text widget editing
    game_description.config(state=DISABLED)

# Create a database connection
conn = sqlite3.connect('scores.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store scores if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        username TEXT,
        score INTEGER
    )
''')

conn.close()

def save_score(username, score):
    try:
        conn = sqlite3.connect('scores.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO scores (username, score) VALUES (?, ?)', (username, score))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error saving score: {e}")


def get_all_scores():
    try:
        conn = sqlite3.connect('scores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT username, score FROM scores ORDER BY score DESC')
        scores = cursor.fetchall()
        conn.close()
        return scores
    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving scores: {e}")
        return []
    
# Example usage:
# Replace 'username' and 'score' with the actual username and score values.
# Call save_score(username, score) to save a new score.

# To retrieve and display all the scores:


#def get_top_scores():
    #cursor.execute('SELECT username, score FROM scores ORDER BY score DESC LIMIT 10')
    #return cursor.fetchall()

# To retrieve the top 10 scores:

def display_scores_menu():
    scores = get_all_scores()
    
   
    # Create a new window (Toplevel) to display the top scores
    top_scores_window = Toplevel(word,width=100,height=300)
    top_scores_window.title("Top Scores")

    listbox_scores = Listbox(top_scores_window,bg="pink",fg="olive")
    listbox_scores.place(x=0,y=0)

    
    for rank, (username, score) in enumerate(scores, start=1):
        listbox_scores.insert(END, f"{rank}: {username} - Score: {score}")
    
# Close the connection when done


# To erase all previous data:
#erase_data()

def reset_scores():
    try:
        conn = sqlite3.connect('scores.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM scores')
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Scores reset successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error resetting scores: {e}")


#MENUBAR
menubar=Menu(word)
word.config(menu=menubar)
file_menu=Menu(menubar,tearoff=False)
#To remove the dashed line, you can set the tearoff property of the menu to False
help_menu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=file_menu,underline=0)#The underline option allows  to create a keyboard shortcut.
#It specifies the character position that should be underlined.Alt+F keyboard shortcut.
menubar.add_cascade(label="Help",menu=help_menu,underline=0)

help_menu.add_command(label="About..", command=aboutg)
file_menu.add_command(label="SCOREBOARD", command=display_scores_menu)
file_menu.add_command(label='RESET SCORES',command=reset_scores,)
file_menu.add_command(label='Exit',command=close_window,)


word.mainloop()

