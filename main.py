# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:53:32 2020

@author: AROOJ NAEEM
"""

# Name          : AROOJ NAEEM
# Registration no: 2019-CE-23

from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
import math



root=Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")
root.iconbitmap("img\Guillendesign-variations-3-Calculator.ico")


calc= Frame(root)
calc.grid()
#################################
# Creating Functions
class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    def numberEnter(self,num):
        self.resut=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
        
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
    def MathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)
    def squard(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)
    def exp(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
    def acosh(self):
        self.result=False
        self.current=math.acosh(float(txtDisplay.get()))
        self.display(self.current)
    def asinh(self):
        self.result=False
        self.current=math.asinh(float(txtDisplay.get()))
        self.display(self.current)
    def expm1(self):
        self.result=False
        self.current=math.expm1(float(txtDisplay.get()))
        self.display(self.current)
    def lgamma(self):
        self.result=False
        self.current=math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)
    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)
    def log1p(self):
        self.result=False
        self.current=math.log1p(float(txtDisplay.get()))
        self.display(self.current)

added_value=Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'),bg="powder blue",bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bg="red",bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1
        
        
        
        
        
#################################
#creting Button
btnClear = Button(calc, text=chr(67),width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.Clear_Entry).grid(row=1,column=0,pady=1)
btnAllclear = Button(calc, text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.all_Clear_Entry).grid(row=1,column=1,pady=1)

btnsq= Button(calc, text="√",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.squard).grid(row=1,column=2,pady=1)
btnAdd = Button(calc, text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                command=lambda : added_value.operation("add")).grid(row=1,column=3,pady=1)
btnSub = Button(calc, text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                command=lambda : added_value.operation("sub")).grid(row=2,column=3,pady=1)
btnMult = Button(calc, text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                 command=lambda : added_value.operation("multi")).grid(row=3,column=3,pady=1)
btnDiv = Button(calc, text=chr(247),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                command=lambda : added_value.operation("divide")).grid(row=4,column=3,pady=1)
btnZero = Button(calc, text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                 command=lambda : added_value.numberEnter(0)).grid(row=5,column=0,pady=1)
btnDot = Button(calc, text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",
                command=lambda : added_value.numberEnter(".")).grid(row=5,column=1,pady=1)
btnPM = Button(calc, text=chr(177),width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.MathsPM).grid(row=5,column=2,pady=1)
btnEquals = Button(calc, text="=",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.sum_of_total).grid(row=5,column=3,pady=1)

##############################Scientific Calculator##################################
btnPi = Button(calc, text="π",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.pi).grid(row=1,column=4,pady=1)
btncos = Button(calc, text="cos",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.cos).grid(row=1,column=5,pady=1)
btntan= Button(calc, text="tan",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.tan).grid(row=1,column=6,pady=1)
btnsin = Button(calc, text="sin",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.sin).grid(row=1,column=7,pady=1)
#####################################################################################
btn2Pi = Button(calc, text="2π",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.tau).grid(row=2,column=4,pady=1)
btnCosh = Button(calc, text="cosh",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.cosh).grid(row=2,column=5,pady=1)
btnSinh = Button(calc, text="sinh",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.sinh).grid(row=2,column=6,pady=1)
btntanh = Button(calc, text="tanh",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.tanh).grid(row=2,column=7,pady=1)
##################################################################################
btnlog = Button(calc, text="log",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.log).grid(row=3,column=4,pady=1)
btnExp = Button(calc, text="Exp",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.exp).grid(row=3,column=5,pady=1)
btnMod = Button(calc, text="Mod",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=lambda : added_value.operation("mod")).grid(row=3,column=6,pady=1)
btnE = Button(calc, text="e",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.e).grid(row=3,column=7,pady=1)
###################################################################################
btnlog2 = Button(calc, text="log2",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.log2).grid(row=4,column=4,pady=1)
btndeg = Button(calc, text="deg",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.degrees).grid(row=4,column=5,pady=1)
btnacosh = Button(calc, text="acosh",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.acosh).grid(row=4,column=6,pady=1)
btnasinh = Button(calc, text="asinh",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.asinh).grid(row=4,column=7,pady=1)
###################################################################################
btnlog10 = Button(calc, text="log10",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.log10).grid(row=5,column=4,pady=1)
btnCos = Button(calc, text="log1p",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.log1p).grid(row=5,column=5,pady=1)
btnexmp1 = Button(calc, text="exmpl",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.expm1).grid(row=5,column=6,pady=1)
btnlgamma = Button(calc, text="lgamma",width=6,height=2,font=('arial',20,'bold'),
                  bd=4,bg="powder blue",command=added_value.lgamma).grid(row=5,column=7,pady=1)


lblDisplay=Label(calc,text="Scientific Calculator",font=("arial",30,"bold"),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)
#########################Temperature Converter##############################
lblDisplay=Label(calc,text="Temperature Converter",font=("arial",20,"bold"))
lblDisplay.grid(row=6,column=0,columnspan=3)


def c_to_f():
    value=float(txtDisplay.get())
    answer=(value*9/5)+32
    showinfo("Answer",f"{value} ᵒC = {answer} F")
    
def f_to_c():
    value=float(txtDisplay.get())
    answer=(value-32)*5/9
    showinfo("Answer",f"{value} F = {answer} ᵒC")

button1=Button(calc,text="Celsius to Farenhite",bd=8,bg="powder blue",font=("arial",15,"bold"),command=c_to_f)
button1.grid(row=7,column=0,columnspan=2)
button2=Button(calc,text="Farenhite to Celsius",bd=8,bg="powder blue",font=("arial",15,"bold"),command=f_to_c)
button2.grid(row=7,column=2,columnspan=2)
##########################Multiplication Table######################################
lblDisplay=Label(calc,text="Multiplication Table",font=("arial",20,"bold"),justify=RIGHT)
lblDisplay.grid(row=0,column=8)


def TimeTable():
    for x in range(1,13):
        m=float(txtDisplay.get())
        display.insert(END,(x),'\t',"x",'\t',(m),'\t',"=",'\t',(x*m))
        display.insert(END,'\n\n')
        
display=Text(calc,bd=30,height=23,font=("arial",10,"bold"),
                    width=30,bg="powder blue")
display.grid(row=2,column=8,rowspan=23)
btnTimeTable=Button(calc,padx=16,pady=16,bd=8,fg="Black",font=("arial",10,"bold"),
                    text="Multiplication",bg="powder blue",
                    command=TimeTable,width=18).grid(row=1,column=8)
########################Currency Converter#########################################
lblDisplay=Label(calc,text="Currency Converter(From US Dollar to Pakistani Rupee)",font=("arial",10,"bold"),justify=RIGHT)
lblDisplay.grid(row=6,column=4,columnspan=3)

def converter():
    here=float(txtDisplay.get())
    final1=here*165.65
    showinfo("Pakistani rupee",f"{here} $ = {final1}Pakistani Rs.")
    
    
def reverse():
    here=float(txtDisplay.get())
    final2=here/165.86
    showinfo("US Dollar",f"{here}Pakistani Rs. = {final2} $")
btn1=Button(calc,text="Converter",bd=8,bg="powder blue",font=('arial',15,'bold'),command=converter).grid(row=7,column=4,columnspan=2)
btn2=Button(calc,text="Reverser",bd=8,font=('arial',15,'bold'),bg="powder blue",command=reverse).grid(row=7,column=5,columnspan=2)

################Functions#################
 
def iExit():
    iExit = tkinter.messagebox.askyesno("Scintific Calculator","Confirm if you want to Exit")
    if iExit>0:
        root.destroy()
        return

def iHelp():
    
    tkinter.messagebox.showinfo("Scientific Calculator."
                                        ,"This is a Scientific Calculator.This Calculator contains many menu.i.e. Scientific Menu,standard menu,Temperature converter menu,Multiplication menu,Currency converter menu, and exit menu.This Calculator can perform scientific features and also convert Temperator also convert currency of pakistan into US Dollar  and can plot Multiplication Table.My Calculator can perform Sin,cos,tan,tanh,cosh,sinh,degree,pi,2pi,mod,square,log,log1p,asinh,acosh,atanh,exp,exmpl,lgamma,e and etc.And Convert Celcius into Farenhite and Farinhite into Celcius.And it can also plot Multiplication tables and also convert currency.")
    
    
    
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("955x568+0+0")
    
    
def Standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")
    
def Temperature():
    root.resizable(width=False,height=False)
    root.geometry("480x655+0+0")
    
def Multiplication():
    root.resizable(width=False,height=False)
    root.geometry("1227x655+0+0")

def Currency_Converter():
    root.resizable(width=False,height=False)
    root.geometry("944x655+0+0")

    

menubar = Menu(calc)
##########################
#File Menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_command(label="Standard",command=Standard)
filemenu.add_command(label="Temperature",command=Temperature)
filemenu.add_command(label="Currency Converter",command=Currency_Converter)
filemenu.add_command(label="Multiplication",command=Multiplication)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)




###########################
#Edit Menu
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")
###############################
#Help menu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Veiw Help",command=iHelp)

root.config(menu=menubar)
root.mainloop()

