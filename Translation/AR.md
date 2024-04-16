<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
 
<a href="https://github.com/jokernets/password-generator">
<img src="https://github.com/jokernets/jokernets/assets/165279911/ca37aa56-0c4d-489b-9c05-3e2b9bacd317"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


<p align="center">
  <img src="https://img.shields.io/github/last-commit/jokernets/password-generate/Translation/AR.md">
  <img src="https://img.shields.io/github/contributors/jokernets/password-generate">
  <img src="https://img.shields.io/github/issues/jokernets/password-generate">
  <img src="https://img.shields.io/github/stars/jokernets/password-generate">

</p>


## `ترجمة`🔗

- [English](https://github.com/jokernets/password-generate/tree/main?tab=readme-ov-file)
- [فارسی](https://github.com/jokernets/password-generate/blob/main/Translation/FA.md)





## جدول المحتويات✅✔
<!--ts-->
   * [التثبیت](#%D8%AA%D8%AB%D8%A8%D9%8A%D8%AA-)

   * [تحليل الكود📈](#%D9%83%D9%88%D8%AF-%D8%A3%D9%86%D9%8A%D9%84%D8%A7%D9%8A%D8%B2-)
     * [الجزء1✔](
#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-1)
     * [الجزء2 ✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-2)
     * [الجزء3 ✔](
#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-3)
     * [الجزء4 ✔](
#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-4)
   * [المزيد من الأمثلة💯](#%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9-%D9%85%D9%86-%D8%A8%D8%B1%D9%88%DA%98%D9%87-)
     * [صورة المشروع🔆](
#%D8%A7%D9%84%D9%85%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-%D8%A7%D9%84%D8%A3%D9%85%D8%AB%D9%84%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D8%B1%D8%B6-)
     * [فيديو للمشروع📺](#%D8%B5%D9%88%D8%B1%D8%A9-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%84%D9%84%D8%AA%D8%B7%D8%A8%D9%8A%D9%82-)

   * [`تواصل معي🌐👻`](#%D8%A7%D8%B1%D8%AA%D8%A8%D8%A7%D8%B7-%D8%A8%D8%A7-%D9%85%D9%86)
   
<!--te-->


# مولد كلمة المرور🔒

### يدور هذا المشروع حول مولد كلمة المرور، والذي يمكننا من خلاله استخراج كلمة المرور
## هذا المشروع مكتوب بلغة بايثون، وواجهة المستخدم لهذا المشروع مكتوبة باستخدام مكتبة Tkinter

## أتمنى أن ترافق مارو حتى نهاية المناقشة🎄🎈

## تثبيت :

```python
pip install Tk
pip install pillow
pip install random
pip install string
```
### تحديث التثبيت الحالي: (قم بالتحديث قدر الإمكان لأن هذه المكتبة قيد التطوير النشط)
`pip3 install tkinter --upgrade`


## كود أنيلايز 🔆

### `الجزء 1`: 
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
<img src="https://github.com/jokernets/password-generate/assets/165279911/d4bdbe5b-909a-46f3-b042-44e2fd33d9c1" width=150 heigth=200></a>


### `الجزء 2`:
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
<img src="https://github.com/jokernets/password-generate/assets/165279911/9fc450b5-f855-471f-98d6-44b19001eeb4" width=150 heigth=200></a>

## إضافة وظيفة في الكود ....

#### `الجزء 3`:

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

### `الجزء 4`:

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

## الصورة من بروژه 🔆

<a href="https://github.com/jokernets/password-generator">
<img src="https://github.com/jokernets/password-generate/assets/165279911/6317cb50-c2cd-4678-96f7-e16a2fe13ce1" width=150 heigth=200></a>



# المزيد من الأمثلة والعرض 🎄👑


## صورة فيديو للتطبيق 📺



https://github.com/jokernets/password-generate/assets/165279911/b3abca66-9d2f-4b64-a0a6-1dbeb16e5fdf






# `ارتباط با من`🌐👻

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammad-fallahnejad-849031293/" height="40" width="60" /></a>
