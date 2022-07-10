from tkinter import *

r=Tk()
r.config(background='maroon')
r.title('WELCOME')
r.geometry('1000x1000')

def first(e):
    r.destroy()
    import Final

img11=PhotoImage(file='welcome.png')
l=Label(r,image=img11,bd=5)
l.bind('<Motion>',first)
l.place(x=370,y=10)
Label(r,text='Rahul Joshi and Team',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=370,y=300)
Label(r,text='2GI19CS106',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=370,y=360)
Label(r,text=' 05',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=370,y=420)
Label(r,text='rahulrjoshi777@gmail.com',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=370,y=480)
Label(r,text='NAME:- ',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=90,y=300)
Label(r,text='USN:- ',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=90,y=360)
Label(r,text='BATCH:- ',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=90,y=420)
Label(r,text='EMAIL:- ',font=('Arial bold',20),bg='maroon',fg='yellow',bd=5).place(x=90,y=480)
Label(r,text='WELCOME',font=('Arial bold',30),bg='maroon',fg='yellow',bd=5).place(x=370,y=570)
Label(r,text='Î Î Hover Over The Picture Î Î',font=('Arial bold',15),bg='maroon',fg='yellow',bd=5).place(x=360,y=640)

r.mainloop()
