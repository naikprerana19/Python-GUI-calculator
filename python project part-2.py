from tkinter import * 
import calculator

root=Tk()
root.geometry("600x400")
root.title('My calculator')

a=StringVar()
b=StringVar()
result=StringVar()

def addition():
    r=calculator.addition(int(a.get()),int(b.get()))
    result.set(r)
def subtraction():
    r=calculator.subtraction(int(a.get()),int(b.get()))
    result.set(r)
def multiplication():
    r=calculator.multiplication(int(a.get()),int(b.get()))
    result.set(r)
def division():
    r=calculator.division(int(a.get()),int(b.get()))
    result.set(r)
lblHeading=Label(root,text='My calculator',font=('Arial',24),bg='orange').pack(side='top')


Label(root,text="First number:").pack()
Entry(root,textvariable=a).pack()

Label(root, text="Second Number:").pack()
Entry(root,textvariable=b).pack()

Label(root,text="").pack()

Button(root, text="Add", width=15, command=addition).pack()
Button(root, text="Subtract", width=15, command=subtraction).pack()
Button(root, text="Multiply", width=15, command=multiplication).pack()
Button(root, text="Divide", width=15, command=division).pack()

Label(root, text="").pack()
Label(root, text="Result:").pack()
Entry(root, textvariable=result, state="readonly").pack()

root.mainloop()

