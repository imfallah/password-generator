<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
 
<a href="https://github.com/jokernets/password-generator">
<img src="https://github.com/jokernets/jokernets/assets/165279911/ca37aa56-0c4d-489b-9c05-3e2b9bacd317"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

## `ترجمه`

- [English](/docs/README.ar-DZ.md)
- [العربية](Translation/AR.md)

  

فهرست مطالب ✅✔
=================

<!--ts-->
   *  [نصب کن](#%D9%86%D8%B5%D8%A8-%DA%A9%D9%86-)

   * [آنالیز کد📈](#%D8%A2%D9%86%D8%A7%D9%84%DB%8C%D8%B2-%DA%A9%D8%AF-%D9%87%D8%A7-
)
     * [پارت 1✔](#%D9%BE%D8%A7%D8%B1%D8%AA-1)
     * [پارت 2✔](#%D9%BE%D8%A7%D8%B1%D8%AA-2)
     * [پارت 3✔](
#%D9%BE%D8%A7%D8%B1%D8%AA-3)
     * [پارت 4✔](
#%D9%BE%D8%A7%D8%B1%D8%AA-4)
  
   *  [نمونه های بیشتر از ویترین 👀💪💯](#%D9%86%D9%85%D9%88%D9%86%D9%87-%D9%87%D8%A7%DB%8C-%D8%A8%DB%8C%D8%B4%D8%AA%D8%B1-%D8%A7%D8%B2-%D9%88%DB%8C%D8%AA%D8%B1%DB%8C%D9%86-)

  * [تصویر پروژ🔆](#%D8%AA%D8%B5%D9%88%DB%8C%D8%B1-%D8%A7%D8%B2-%D9%BE%D8%B1%D9%88%DA%98%D9%87-)

 
  * [ویدیو از پروژه📺](
#%D8%AA%D8%B5%D9%88%DB%8C%D8%B1-%D9%88%DB%8C%D8%AF%DB%8C%D9%88%DB%8C%DB%8C-%D8%A7%D8%B2-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-)

  
 * [ارتباط با من🌐👻](#%D8%A7%D8%B1%D8%AA%D8%A8%D8%A7%D8%B7-%D8%A8%D8%A7-%D9%85%D9%86)
<!--te-->


# تولید کننده رمز 🔒 ! 

#### این پروژه در مورد Password Generator است که می توانیم رمز عبور را از آن استخراج کنیم
#### این  پروژه به زبان پایتون نوشته شده است و رابط کاربری این پروژه با استفاده از کتابخانه Tkinter نوشته شده است
### امیدوارم تا پایان بحث مارو همراهی کنید🎄🎈

# نصب کن !
### ماژول را با پیپ نصب کنید:
```python
pip install tk
pip insall random2
pip install Pillow 
pip install  string
```

### نصب موجود را به روز کنید: pip3 install tkinter --upgrade
### (تا حد امکان به روز رسانی کنید زیرا این کتابخانه در حال توسعه فعال است)


# آنالیز کد ها :

## `پارت 1`:
این کد پنجره Tkinter را برای برنامه تولید رمز عبور با ابعاد، رنگ ها و موقعیت خاص روی صفحه تنظیم می کند. می توانید به ساختن ادامه دهید ...



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


## `پارت 2`: 
این کد یک تصویر لوگو را با استفاده از بسته های Image و ImageTk در یک پنجره گرافیکی به نام "root" نمایش می دهد. برچسب با نماد "PASSWORD GENERATOR" در نقطه مشخص شده در پنجره نمایش داده می شود.
- ابتدا برای نماد لوگو، تصویری با نام “logo.png” به یک هسته اندازه گیری به نام “img” تبدیل می شود و سپس پنجره “root” بر این اساس تنظیم می شود.


```python 
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
```
<a href="https://github.com/jokernets/password-generator">
<img src="https://github.com/jokernets/password-generate/assets/165279911/9fc450b5-f855-471f-98d6-44b19001eeb4" width=150 heigth=200></a>



## اضافه کردن دستورات تابع ...
## `پارت 3`:
یک تابع برای ایجاد رمز عبور تصادفی در پایتون است. این تابع از حروف کوچک، حروف بزرگ، اعداد و نمادها برای ساخت رمز عبور استفاده می‌کند. کاربر می‌تواند انتخاب کند که کدام دسته از کاراکترها در رمز عبور نهایی گنجانده شوند. طول رمز عبور توسط کاربر تعیین می‌شود و رمز عبور ساخته شده در برنامه نمایش داده می‌شود. همچنین، یک دکمه برای کپی کردن رمز عبور به کلیپ‌بورد وجود دارد

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
```
## اخرین دستورات ...

## `پارت 4`:
کدی که ارائه کرده اید بخشی از رابط کاربری ساده یک برنامه کاربردی برای تولید رمزهای عبور تصادفی است. این به کاربران اجازه می دهد تا انتخاب کنند که آیا حروف بزرگ، حروف کوچک، اعداد و نمادها در رمز عبور گنجانده شده است یا خیر. کاربران همچنین می توانند طول رمز عبور دلخواه را مشخص کنند. پس از ایجاد رمز عبور، می توان آن را در کلیپ بورد کپی کرد.

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
## تصویر از پروژه 🔆
<a href="https://github.com/jokernets/password-generator">
<img src="https://github.com/jokernets/password-generate/assets/165279911/6317cb50-c2cd-4678-96f7-e16a2fe13ce1" width=150 heigth=200></a>


## نمونه های بیشتر از ویترین 👀💪


### تصویر ویدیویی از برنامه 🎊



https://github.com/jokernets/password-generate/assets/165279911/b3abca66-9d2f-4b64-a0a6-1dbeb16e5fdf






# `ارتباط با من`🌐👻

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/luv-sahu-182356200/" height="40" width="60" /></a>
<a href="https://instagram.com/mrcode.co" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="luv_k_sahu" height="40" width="50" /></a>

