
from tkinter import *
from random import randint
from tkinter.messagebox import *


def find():
    fr = open('snake/score.txt','r')
    r = fr.read()
    fr.close()
    if score > int(r):
        fw = open('snake/score.txt','w')
        fw.write(str(score))
        fw.close()
    w.destroy()
        

def cut():
    global cutthere
    o = int((len(snake))/2)
    for k in range(o):
        c.delete(snake.pop(0))
    cutthere = False
    c.delete(scissor)
        
def a(num):
    return float((num*32)+19)

def pause(f):
    global paused
    if paused:
        paused = False
    else:
        paused = True

def makeapple():
    global apple
    apple = c.create_image(cr[randint(1,20)],cr[randint(1,20)],image = aimg)

def gameover():
    showerror(title = 'Game Over!',message = 'Dontn\'t hit yourself.')
    find()

def check():
    x = [cr[num[0]],cr[num[1]]]
    for i in snake:
        if i != snake[len(snake)-1]:
            if x == c.coords(i):
                gameover()

def makescissors():
    if not paused:
        global scissor, cutthere
        scissor = c.create_image(cr[randint(1,20)],cr[randint(1,20)],image = scimg)
        cutthere = True
    w.after(randint(45000,50000),makescissors)


def up(f):
    global di
    if di == 'right' or di == 'left':
        di = 'up'
        w.unbind('<Right>')
        w.unbind('<Left>')
        w.unbind('<Up>')
        w.unbind('<Down>')
    else:
        w.bell()

def down(f):
    global di
    if di == 'right' or di == 'left':
        di = 'down'
        w.unbind('<Right>')
        w.unbind('<Left>')
        w.unbind('<Up>')
        w.unbind('<Down>')
    else:
        w.bell()

def right(f):
    global di
    if di == 'up' or di == 'down':
        di = 'left'
        w.unbind('<Right>')
        w.unbind('<Left>')
        w.unbind('<Up>')
        w.unbind('<Down>')
    else:
        w.bell()

def left(f):
    global di
    if di == 'up' or di == 'down':
        di = 'right'
        w.unbind('<Right>')
        w.unbind('<Left>')
        w.unbind('<Up>')
        w.unbind('<Down>')
    else:
        w.bell()

def move():
    global num, score
    if not paused:
        if di =='left':
            if num[0] != 20:
                num[0] += 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            else:
                num[0] = 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            x = [cr[num[0]],cr[num[1]]]
            if x == list(c.coords(apple)):
                c.delete(apple)
                makeapple()
                score += 1
                scorev.set('Score: '+str(score))
                w.update_idletasks
            else:
                c.delete(snake.pop(0))
            if cutthere:
                if x == list(c.coords(scissor)):
                    cut()
                
        if di =='right':
            if num[0] != 1:
                num[0] -= 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            else:
                num[0] = 20
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            x = [cr[num[0]],cr[num[1]]]
            if x == list(c.coords(apple)):
                c.delete(apple)
                makeapple()
                score += 1
                scorev.set('Score: '+str(score))
                w.update_idletasks
            else:
                c.delete(snake.pop(0))
            print(cutthere)
            if cutthere:
                print('x',x)
                print(list(c.coords(scissor)))
                if x == list(c.coords(scissor)):
                    cut()
        if di =='up':
            if num[1] != 1:
                num[1] -= 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            else:
                num[1] = 20
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            x = [cr[num[0]],cr[num[1]]]
            if x == list(c.coords(apple)):
                c.delete(apple)
                makeapple()
                score += 1
                scorev.set('Score: '+str(score))
                w.update_idletasks
            else:
                c.delete(snake.pop(0))
            if cutthere:
                if x == list(c.coords(scissor)):
                    cut()
        if di =='down':
            if num[1] != 20:
                num[1] += 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            else:
                num[1] = 1
                snake.append(c.create_image(cr[num[0]],cr[num[1]],image = simg))
            x = [cr[num[0]],cr[num[1]]]
            if x == list(c.coords(apple)):
                c.delete(apple)
                makeapple()
                score += 1
                scorev.set('Score: '+str(score))
                w.update_idletasks
            else:
                c.delete(snake.pop(0))
            if cutthere:
                if x == list(c.coords(scissor)):
                    cut()
        check()
        w.bind('<Right>',right)
        w.bind('<Left>',left)
        w.bind('<Up>',up)
        w.bind('<Down>',down)
        w.update_idletasks()
    w.after(400,move)


################################################



sw = Tk()
sw.minsize(width=250, height=200)
sw.title('🐍Sssnake🐍')
sw['bg']='#fff747'

def endless():
    sw.destroy()
    global w,bgimg,simg,aimg,scimg,snake,cr,c,bg,num,score,scorev,cutthere,di,paused,sl    
    w = Tk()
    w.minsize(width=600, height=600)
    w.title('Sssnake')
    w['bg']='#000000'

    bgimg = PhotoImage(file='snake/bg13.png')
    simg = PhotoImage(file='snake/snake.png')
    aimg = PhotoImage(file='snake/apple.png')
    scimg = PhotoImage(file='snake/scissors.png')

    snake = []

    f = Frame(w,relief = SOLID,padx = 0,pady = 0,bg='#000000',bd = 0)
    f.grid(column = 0, row = 4,padx = 5,pady = 5)

    w.rowconfigure(5,weight = 1)
    w.columnconfigure(0,weight = 1)
    
    cr = {1:a(0),2:a(1),3:a(2),4:a(3),5:a(4),6:a(5),7:a(6),8:a(7),9:a(8)
          ,10:a(9),11:a(10),12:a(11),13:a(12),14:a(13),15:a(14),16:a(15)
          ,17:a(16),18:a(17),19:a(18),20:a(19)}

    c = Canvas(w,width = 639,height = 639,bd = 2,relief = SOLID,background = '#000000')

    bg = c.create_image(4,4,anchor = 'nw',image = bgimg)

    snake.append(c.create_image(cr[10],cr[11],image = simg))
    snake.append(c.create_image(cr[10],cr[10],image = simg))

    num = [10,10]

    score = 0
    scorev = StringVar()
    scorev.set('Score: '+str(score))
    cutthere = False
    di = 'up'

    paused = False

    makeapple()
    w.after(randint(20000,50000),makescissors)


    w.bind('<p>',pause)

    w.after(1000,move)
    
    c.grid(column = 0,row = 5,padx = 0,pady = 0)

    fr = open('snake/score.txt','r')
    r = fr.read()
    fr.close()

    hsl = Label(f,text = 'High Score: '+r,font = 'Narkisim 22',anchor = 'w',relief=RAISED)
    hsl.grid(padx = 5, pady = 5,column=0,row=0,sticky = W)
    
    sl = Label(f,textvariable = scorev,font = 'Narkisim 22',anchor = 'w',relief=RAISED)
    sl.grid(padx = 5, pady = 5,column=1,row=0,sticky = W)

    c.focus_force()
    w.protocol("WM_DELETE_WINDOW", find)
    w.mainloop()

l1 = Label(sw,text = 'Sssnake',font = 'Narkisim 22',bg='#fff747',fg = 'blue')
l2 = Label(sw,text = 'Choose a Gamemode',font = 'Narkisim 18',bg='#fff747',fg = 'blue')


l1.grid(padx = 15, pady = 10,column=0,row=0)
l2.grid(padx = 15, pady = 10,column=0,row=1)


endlessb = Button(sw,width = 10,text = 'Endless',command = endless,font = 'Narkisim 15',fg = 'blue',activeforeground = 'blue',activebackground = 'cyan',bg = 'cyan')
endlessb.grid(column = 0, row = 3,padx = 5,pady = 5)

sw.mainloop()

