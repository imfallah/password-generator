<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
 
<a href="https://github.com/jokernets/password-generator">
<img src="public/Password generator(1).png"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


## `Translation`🔗





# مولد كلمة المرور🔒

### يدور هذا المشروع حول مولد كلمة المرور، والذي يمكننا من خلاله استخراج كلمة المرور
## هذا المشروع مكتوب بلغة بايثون، وواجهة المستخدم لهذا المشروع مكتوبة باستخدام مكتبة Tkinter

## أتمنى أن ترافق مارو حتى نهاية المناقشة🎄🎈

## تثبيت :

```python
pip install Tkinter
pip install Pillow
pip install random
pip install string
```
### تحديث التثبيت الحالي: (قم بالتحديث قدر الإمكان لأن هذه المكتبة قيد التطوير النشط)
`pip3 install tkinter --upgrade`


## كود أنيلايز 🔆

`الجزء 1`: 
### يقوم هذا الكود بتعيين نافذة Tkinter لمولد كلمة المرور بأبعاد وألوان وموضع محدد على الشاشة. يمكنك الاستمرار في البناء...
```python
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

root.mainloop()
```
<a href="https://github.com/jokernets/password-generator">
<img src="public/part1.png" width=150 heigth=200></a>


`الجزء 2`:
### يعرض هذا الرمز صورة شعار باستخدام حزمتي Image وImageTk في نافذة رسومية تسمى "root". سيتم عرض ملصق يحمل الرمز "PASSWORD GENERATOR" عند النقطة المحددة في النافذة.

- أولاً، بالنسبة لأيقونة الشعار، يتم تحويل الصورة المسماة "logo.png" إلى نواة قياس تسمى "img"، ثم يتم تعيين نافذة "الجذر" وفقًا لذلك.

````python

#icon_root
img=PhotoImage(file="C:/project_python/password generate/image/logo.png")
root.iconphoto(True,img)

#Logo_image
img=Image.open("C:/project_python/img/logo.png")
img=img.resize((80,70))
img=ImageTk.PhotoImage(img)
app_image=Label(root,height=60,padx=10,anchor="nw",image=img,bg=color_1)
app_image.place(x=110,y=-3)

#label_password_generator
lbl=Label(root,text="PASSWORD GENERATOR",font=("Goudy Old Style ",14),bg=color_1,fg="#7fff00")
lbl.place(x=30,y=60)

````

<a href="https://github.com/jokernets/password-generator">
<img src="public/part2.png" width=150 heigth=200></a>


## إضافة وظيفة في الكود ....

`الجزء 3`:

### وظيفة لإنشاء كلمة مرور عشوائية في بايثون. تستخدم هذه الوظيفة الأحرف الصغيرة والأحرف الكبيرة والأرقام والرموز لإنشاء كلمة مرور. يمكن للمستخدم اختيار الأحرف التي سيتم تضمينها في كلمة المرور النهائية. يتم تعيين طول كلمة المرور من قبل المستخدم ويتم عرض كلمة المرور التي تم إنشاؤها في التطبيق. يوجد أيضًا زر لنسخ كلمة المرور إلى الحافظة


```python

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
````

                

## الطلبات الاخيرة...

`الجزء 4`:

### يعد الرمز الذي قدمته جزءًا من واجهة مستخدم بسيطة لتطبيق إنشاء كلمة مرور عشوائي. فهو يتيح للمستخدمين اختيار ما إذا كانوا يريدون تضمين الأحرف الكبيرة والأحرف الصغيرة والأرقام والرموز في كلمة المرور. يمكن للمستخدمين أيضًا تحديد طول كلمة المرور المطلوبة. بمجرد إنشاء كلمة المرور، يمكن نسخها إلى الحافظة.

```python
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
 

```

<a href="https://github.com/jokernets/password-generator">
<img src="public/output.png" width=150 heigth=200></a>


# المزيد من الأمثلة والعرض 🎄👑


## صورة فيديو للتطبيق 📺



https://github.com/jokernets/password-generator/assets/165279911/648cbb10-2dd9-4307-9599-5e6ace95d536




<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>
