#!/usr/bin/env python
# coding: utf-8

# In[19]:


from tkinter import *
from tkinter import messagebox
import time
import pandas as pd
root=Tk()
root.geometry("1000x1000")
root.title("Tic Tac Toe")
root.config(bg="#116562")
root.iconbitmap(r"C:\Users\Anuj\Downloads\190320_game_tac_tic_red_toe_icon.ico")
count=0
turn=True
winner=False
flag=0
pw="123"
w=1
new_winner=None

#Labels
l=Label(root,width=40,height=3,bg="#D6D6D6",borderwidth=2, relief="solid",font=("Times",10,"bold"))
l1=Label(root,width=40,height=3,bg="#D6D6D6",fg="#004A94",borderwidth=2, relief="solid",font=("Times",10,"bold"))
    
l2=Label(root,text="PLAYER 1",bg="#116562",font=("Times",10,"bold"),height=2)
l2.place(x=30,y=50)
v1=StringVar
e1=Entry(root,textvariable=v1,bg="#D6D6D6",borderwidth=2, relief="solid",font=("Times",10,"bold"))
e1.place(x=140,y=50,height=35)

l3=Label(root,text="PLAYER 2",bg="#116562",font=("Times",10,"bold"),height=2)
l3.place(x=30,y=100)
v2=StringVar()
e2=Entry(root,textvariable=v2,bg="#D6D6D6",borderwidth=2, relief="solid",font=("Times",10,"bold"))
e2.place(x=140,y=100,height=35)

l4=Label(root,text="PASSWORD",bg="#116562",font=("Times",10,"bold"),height=2)
l4.place(x=30,y=150)
v3=StringVar()
e3=Entry(root,textvariable=v3,bg="#D6D6D6",borderwidth=2, relief="solid",font=("Times",10,"bold"))
e3.place(x=140,y=150,height=35)
       
lo=Button(root,text="LOGIN",width=20,height=1,borderwidth=2, relief="solid",font=("Times",10,"bold"),command=allow)
lo.place(x=30,y=200)


#to create database
import sqlite3
with sqlite3.connect("GAME record.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS RECORDS(S_NO integer PRIMARY KEY AUTOINCREMENT, PLAYER_1 TEXT NOT NULL,
               PLAYER_2 TEXT NOT NULL,PASSWORD TEXT NOT NULL,WINNER TEXT);""")



#to disable buttons after match end
def disable():
    b1["state"]=DISABLED
    b2["state"]=DISABLED
    b3["state"]=DISABLED
    b4["state"]=DISABLED
    b5["state"]=DISABLED
    b6["state"]=DISABLED
    b7["state"]=DISABLED
    b8["state"]=DISABLED
    b9["state"]=DISABLED

#to enable button   
def enable():
    b1["state"]='normal'
    b2["state"]='normal'
    b3["state"]='normal'
    b4["state"]='normal'
    b5["state"]='normal'
    b6["state"]='normal'
    b7["state"]='normal'
    b8["state"]='normal'
    b9["state"]='normal'

#to decide winner
def who_winner():
    global winner,w,count
    if(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1.config(bg="#FF0039")
        b2.config(bg="#FF0039")
        b3.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
          
    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        b4.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b6.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
        
     
    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        b7.config(bg="#FF0039")
        b8.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()

    elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        b1.config(bg="#FF0039")
        b4.config(bg="#FF0039")
        b7.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
        
    elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        b2.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b8.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        disable()
        add_user()
        
    elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        b3.config(bg="#FF0039")
        b6.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
        
    elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        b1.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
        
    elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        b3.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b7.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR X !!!")
        w=1
        count=0
        disable()
        add_user()
    
    elif(b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O"):
        b1.config(bg="#FF0039")
        b2.config(bg="#FF0039")
        b3.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        disable()
        add_user()
     
    elif(b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
        b4.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b6.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
        b7.config(bg="#FF0039")
        b8.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O"):
        b1.config(bg="#FF0039")
        b4.config(bg="#FF0039")
        b7.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
        b2.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b8.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
        b3.config(bg="#FF0039")
        b6.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
    
    elif(b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
        b1.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b9.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        b3.config(bg="#FF0039")
        b5.config(bg="#FF0039")
        b7.config(bg="#FF0039")
        winner=True
        messagebox.showinfo("Game Over","IT'S A WIN FOR O !!!")
        w=-1
        count=0
        disable()
        add_user()
        
    elif(count==9 and winner==False):
        messagebox.showinfo("Game Over","IT'S A DRAW!!!")
        w=0
        count=0
        disable()
        add_user()

#to insert the inputs
def click(b):
    global turn,count,flag
    flag=1
    if(b["text"]== " " and turn==True):
        b["text"]="X"
        turn=False
        count+=1
        who_winner()
    
    elif(b["text"]== " " and turn==False):
        b["text"]="O"
        turn=True
        count+=1
        who_winner()
        
    else:
        messagebox.showerror("error","Selected Box has been already marked")
        
    disable()
    
#to make the game interface
def game():
    global winner,turn
    winner=False
    timer(5)
    l1.config(text="Player 1 Turn (X)")
    flag=0
    turn=True
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    b1=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b1))
    b1.place(x=390,y=320)
    b2=Button(root,text=" ",bg="white",height=5,width=8,borderwidth=3, relief="solid",command=lambda: click(b2))
    b2.place(x=456,y=320)
    b3=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b3))
    b3.place(x=522,y=320)
    

    b4=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b4))
    b4.place(x=390,y=406)
    b5=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b5))
    b5.place(x=456,y=406)
    b6=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b6))
    b6.place(x=522,y=406)
    
    b7=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b7))
    b7.place(x=390,y=492)
    b8=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b8))
    b8.place(x=456,y=492)
    b9=Button(root,text=" ",bg="white",height=5,width=8, borderwidth=3, relief="solid",command=lambda: click(b9))
    b9.place(x=522,y=492)
    

#TO MAKE AN PLAY INTERFACE
def begin():
    b10=Button(root,text="PLAY",bg="#D6D6D6",fg="black",font=("Times",10,"bold"),borderwidth=2,
           relief="solid",height=4,width=40,command=game)
    b10.place(x=350,y=50)

    b11=Button(root,text="EXIT",bg="#D6D6D6",fg="black",font=("Times",10,"bold"),height=4,width=40,
           borderwidth=2, relief="solid",command=root.destroy)
    b11.place(x=350,y=140)

    l.place(x=640,y=250)
    l1.place(x=70,y=250)
    
#to check the password
def allow():
    if(e3.get()==pw):
        begin()
        
    else:
        messagebox.showerror("Error","Incorrect password!!")
        
# add to database
def add_user():
    global w
    new_player_1 = e1.get()
    new_player_2 = e2.get()
    new_password = e3.get()
    if(w==1):
        new_winner=e1.get()
    elif(w==-1):
        new_winner=e2.get()
    elif(w==0):
        new_winner="Draw"
    cursor.execute("INSERT INTO RECORDS (PLAYER_1,PLAYER_2,PASSWORD,WINNER)VALUES(?,?,?,?)",
                   (new_player_1,new_player_2,new_password,new_winner))
    db.commit()
    
#to make a timer
def timer(t):
    global flag,w,count
    if(t>-1):
        l.config(text=t)
        t=t-1
        l.after(1000,lambda: timer(t))
    else:
        if(flag==0 and turn==True):
            messagebox.showinfo("Game over"," Player 2 (O) Wins")
            w=-1
            count=0
            disable()
            add_user() 
            
        elif(flag==0 and turn==False):
            messagebox.showinfo("Game over"," Player 1 (X) Wins")
            w=1
            count=0
            disable()
            add_user()
            
        elif(flag==1):
            time.sleep(1)
            if(winner==False):
                enable()
                flag=0
                if(turn==True):
                    l1.config(text="Player 1 turn (X)")
                else:
                    l1.config(text="Player 2 turn (O)")
                timer(5)
        
root.mainloop()
df = pd.read_sql_query("SELECT * FROM RECORDS", db)
df


# In[ ]:




