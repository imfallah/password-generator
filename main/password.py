
#----------------------------------------------------------------------------------

                #   Password generator --1
#-------------------------------------------------------------------------------

#importing libraries
from tkinter import *
from tkinter import Tk
import random
from PIL import Image , ImageTk
import string
#color
co1="#A6A6A6"
co2="#33398"
color_1="#2f4f4f"
fg_check="#7FFF00"

#window
root=Tk()
root.title("Password Generator")
root.resizable(False,False) 
root.geometry("300x515")
root.configure(bg=color_1)
root.geometry("300x515+{}+{}".format(root.winfo_screenwidth() // 2 -200, root.winfo_screenheight() // 2 - 270))


#icon_root
img=PhotoImage(file="C:/project_python/password-generator(github)/main/image/icon.png")
root.iconphoto(True,img)

#Logo_image
img=Image.open("C:/project_python/password-generator(github)/main/image/logo.png")
img=img.resize((80,70))
img=ImageTk.PhotoImage(img)
app_image=Label(root,height=60,padx=10,anchor="nw",image=img,bg=color_1)
app_image.place(x=110,y=-3)

#label_password_generator
lbl=Label(root,text="PASSWORD GENERATOR",font=("Goudy Old Style ",14),bg=color_1,fg="#7fff00")
lbl.place(x=30,y=60)



#working on frame box
var=IntVar()
var.set(10)

#function to password generator
def password_generator():
    lowercase_alphabet = string.ascii_lowercase
    uppercase_alphabet = string.ascii_uppercase
    numbers = "0123456789"
    symbol = "()[]+/;:\ "
#    normal_password=(symbol+numbers+lowercase_alphabet)  
    
    combine="" #or global combine
    
    
    # uppercase alphabet
    if state_1.get()== uppercase_alphabet:
        combine = uppercase_alphabet
    else:
        pass
    #lowercase_alphabet
    if state_lowercase.get()== lowercase_alphabet:
        combine += lowercase_alphabet
    else:
        pass
    #numbers
    if state_numbers.get()== numbers:
        combine += numbers
    else:
        pass
    #symbols
    if state_symbols.get()== symbol:
        combine += symbol
    else:
        pass
    

     #pass
    #password length
    length=int(spin.get())
    #password
    password="".join(random.sample(combine , length))
    #watching the password in app_password
    app_password["text"]=password
    #function Copy the passwor
    def copy_password():
        info =password 
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("PASSWORD GENERATOR","password has been copied")
        #button_copy_password

    copy_password_button=Button(root,text="Copy",command=copy_password,font=("Arial 10 bold"),bg="white",fg="black",padx=0,pady=12,width=6,height=1,relief=RAISED)    
    copy_password_button.place(x=240,y=201)

#variable
lowercase_alphabet=string.ascii_lowercase
uppercase_alphabet=string.ascii_uppercase
number="0123456789"
symbol="()[]+/;:\ "

#normal_password=(symbol+number+lowercase_alphabet)  
combine=""

#line
line=Label(root,text="Total number in password generator",height=0,font=("Gadugi 10 bold"),bg="#A2B5CD",fg="black")
line.place(x=15,y=130)

#spin_box
spin=Spinbox(root,from_=8,to=20,width=30,textvariable=var)
spin.place(x=33,y=170)

#working on Frame box
app_password=Label(root,text="View your password",width=0,height=3,relief='solid',pady=0,padx=50,anchor='center',font=("Arial 10"),bg="#333333",fg="white",activebackground=color_1)
app_password.place(x=4,y=200)

#Uppercase Label
uppercase_label=Label(root,text="ABC Uppercase",width=0,height=0,anchor='center',font=("Aria 13 bold"),bg=color_1,fg=fg_check)
uppercase_label.place(x=111,y=270)

state_1=StringVar()
state_1.set(False)       #set check state

check=Checkbutton(root,width=0,height=0,var=state_1,onvalue=uppercase_alphabet,offvalue="off",bg=color_1,activeforeground=color_1,activebackground=color_1)
check.place(x=86,y=269)
#lowercase Label
lowercase_label=Label(root,text="abc Lowercase",width=0,height=0,anchor='center',font=("Aria 13 bold"),bg=color_1,fg=fg_check)
lowercase_label.place(x=110,y=310)

state_lowercase=StringVar()
state_lowercase.set(False)

check_lowercase=Checkbutton(root,width=0,height=0,var=state_lowercase,onvalue=lowercase_alphabet,offvalue="off",bg=color_1,activeforeground=color_1,activebackground=color_1)
check_lowercase.place(x=86,y=310)
#number
numbers_label=Label(root,text="NUMBERS",width=0,height=0,anchor='center',font=("Aria 13 bold"),bg=color_1,fg=fg_check)
numbers_label.place(x=114,y=349)

state_numbers=StringVar()
state_numbers.set(False)

check_numbers=Checkbutton(root,width=-4,height=0,var=state_numbers,onvalue=number,offvalue="off",bg=color_1,activeforeground=color_1,activebackground=color_1)
check_numbers.place(x=86,y=349)
#Symbol_Label
symbols_label=Label(root,text="SYMBOLS",width=0,height=0,anchor='center',font=("Aria 13 bold"),bg=color_1,fg=fg_check)
symbols_label.place(x=110,y=383)

state_symbols=StringVar()
state_symbols.set(False)

check_symbols=Checkbutton(root,width=-4,height=0,var=state_symbols,onvalue=symbol,pady=3,offvalue="off",activeforeground=color_1,activebackground=color_1,bg=color_1)
check_symbols.place(x=86,y=380)





#button_generate

generate_password_button=Button(root,text="Generate Password",overrelief=SOLID,font=("Arial 10 bold"),bg="white",fg="black",command=password_generator,pady=12,padx=14,width=0)
generate_password_button.place(x=70,y=440)

root.mainloop()

#End!
