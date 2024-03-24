# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 17:01:34 2023

@author: Aastha
"""

from tkinter import*
from tkinter import ttk
import random
from random import shuffle
from tkinter import messagebox

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
    # this function returns all dictionary words that can be constructed from 'possibleChars'.
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
img = PhotoImage(file='bg1.png')
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0,image=img,anchor = "nw") 

timer_label = Label(word, text="", bg="yellow", font=("Helvetica", 16))
timer_label.place(x=270,y=0)
def start_timer():
        update_timer(60)

def update_timer(counter):
    global count,boy
    if counter > 0:
        timer_label.config(text=f"Time Left: {counter} seconds")
        word.after(1000, update_timer, counter - 1)
    else:
        timer_label.config(text="Time's up!")
        messagebox.showinfo("Time's Up", "Your time is up!")
        stop()
        e.place_forget()
        b1.place_forget()
    #b2.place(y=90,x=110,width=80,height=50)
        b3.place_forget()
        b4.place_forget()
        b5.place_forget()
        b6.place_forget()
          
        bt2.place_forget()
        bt1.place_forget()
        fl=Label(word,text=f"points earned={count}",fg="black",bg="white",font=("Helvetica", 15),)
        fl.place(x=100,y=200)
        messagebox.showinfo("Time's Up", "Your time is up!")
        boy = canvas1.create_image(400, 200, image=bi)
        if count>0:
            move_boy()
        else:
            word.destroy()
class Balloon:
    def __init__(self):
        self.radius = random.randint(7, 50)
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
        self.radius = random.randint(7, 50)
        self.x = random.randint(self.radius, 600 - self.radius)
        self.y = -self.radius
        self.image_path = random.choice(["cap1.png"])
        self.image = PhotoImage(file=self.image_path)
        self.id = canvas1.create_image(self.x, self.y, image=self.image)
        self.speed = random.randint(2, 5)

# Create a list to store Balloon instances
balloons = []

# Create function to add new balloons and move existing ones
def animate():
    new_balloon = Balloon()
    balloons.append(new_balloon)
    
    for balloon in balloons:
        balloon.move()

    if not stop_animation:
        word.after(100, animate)

# Function to stop the animation
def stop():
    global stop_animation
    stop_animation = True


answer=getWords()

words_6=[]

for i in answer:
    if(len(i)==6):
        words_6.append(i)
       
answer1=StringVar()
e=Entry(word,borderwidth="1",bg="white",font="Canada 10",textvariable=answer1)


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
       
   

   
b1=Button(word,borderwidth=10,bg="pink",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[0],command=lambda:entry_update(current_sw[0]))


b2=Button(word,borderwidth=10,bg="olive",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[1],command=lambda:button_click(current_sw[1]))


b3=Button(word,borderwidth=10,bg="blue",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[2],command=lambda:button_click(current_sw[2]))



b4=Button(word,borderwidth=10,bg="white",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[3],command=lambda:button_click(current_sw[3]))


b5=Button(word,borderwidth=10,bg="orange",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[4],command=lambda:button_click(current_sw[4]))


b6=Button(word,borderwidth=10,bg="yellow",fg="magenta",activeforeground="green",activebackground="black",text=current_sw[5],command=lambda:button_click(current_sw[5]))


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
       lb3=Label(word,text="Sorry!!Better luck next time!!")
       lb3.place(x=110,y=230)
       lb3.after(2000, lambda: lb3.destroy())
       reset()
   
   elif(word_count==6):
      lb2=Label(word,text="Congratulations!you won!!")
      lb2.place(x=110,y=230)
      lb2.after(2000, lambda: lb2.destroy())
      
      reset();

def check():
        global word_count,chances,count
        flag=0
        result=solveWordCrossPuzzle(current_sw,2,3,4,5,6)
        user_input=e.get()
        for i in result:
            if user_input==i:
                flag=1
               
               
        if(flag==1):
            word_count=word_count+1
            update_progress()
            stop()
            lb2=Label(word,text="Congratulations!that is correct!")
            lb2.place(x=110,y=230)
            lb2.after(2000, lambda: lb2.destroy())
            count+=10
            e.delete(0,END)
            winner_loser()
        else:
            chances=chances-1
            lb3=Label(word,text="Wrong guess...Try again")
            lb3.place(x=110,y=230)
            lb3.after(2000, lambda: lb3.destroy())
            e.delete(0,END)
            winner_loser()
           
                   
           
           
def reset():
        e.delete(0,END)
        global current_sw
        current_sw=Random_word_creation()
        
        b1.configure(text=current_sw[0])
        b2.configure(text=current_sw[1])
        b3.configure(text=current_sw[2])
        b4.configure(text=current_sw[3])
        b5.configure(text=current_sw[4])
        b6.configure(text=current_sw[5])
def toggle_visibility():
    if myButton.winfo_ismapped():
        myLabel.pack_forget()
        myButton.pack_forget()
def myDelete():
    global myLabel,myButton,b2
    myLabel.place_forget()
    myButton.place_forget()
    b2.place_forget()
    progress_bar.place(x=50,y=50)
    e.place(x=75,y=10)
    b1.place(y=90,x=20,width=80,height=50)
    #b2.place(y=90,x=110,width=80,height=50)
    b3.place(y=90,x=110,width=80,height=50)
    b4.place(y=90,x=200,width=80,height=50)
    b5.place(y=150,x=110,width=80,height=50)
    b6.place(y=150,x=200,width=80,height=50)
          
    bt2.place(x=10,y=250)
    bt1.place(x=200,y=250)
    start_timer()
text="Harry wants to celebrate his birthday but lacks some money.\n Help him to win exciting birthday gifts!!"
        
def myClick():
    global myLabel
    global myButton
    myLabel = Label(
        bg="red",fg='black',font=("Helvetica", 14)
    )
    myLabel.place(x=5,y=50)
    update_text()
    myButton.place_forget()
   
def update_text(index=0):
    global myLabel,text
    if index < len(text):
        myLabel.config(text=text[:index+1])  # Update label text up to the current index
        word.after(100, update_text, index+1)  # Schedule the next update
    else:
        myLabel.config(text=text)  # Set the final text when all letters are displayed
               
       
myButton = Button(word, text="Be Ready to boost your brain!!", command=myClick, bg="green")
myButton.place(x=150,y=0)



b2 = Button(word, text="Start", command=myDelete, bg="pink",font=("Helvetica", 14))
b2.place(x=205,y=100)     
       

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
animate()


word.mainloop()
