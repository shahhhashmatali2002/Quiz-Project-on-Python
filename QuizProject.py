#......................| Import Library |.........................
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("Login Date:  %d/%m/%Y  \nLogin Time: %H:%M:%S")
print("date and time =", dt_string)
#.............................| Class |.....................
class login_system:
    def __init__(self, hashmat):
        # ______________________________| login window  |_____________________
        self.hashmat = hashmat
        self.hashmat.title("Login ID")
        self.hashmat.geometry('1360x768')
        self.hashmat.configure(background='skyblue')
        # title = Label(self.hashmat,text='Login Here',font=("times new roman", 10,"bold"),bg="gray",fg="black",width=120,height=2 ).place(x=0,y=0)

        # _____________________| background image in login window |__________________________
        self.bg = ImageTk.PhotoImage(file="C:/images/wall5.jpg")
        bg = Label(self.hashmat, image=self.bg).place(x=0, y=0, width=1360, height=768)

        # self.log = ImageTk.PhotoImage(file="C:/images/login2.png")
        # log = Label(frame1, image=self.log).place(x=150, y=150, width=450, height=400)

        # ____________________________| Frame1 in login window |_________________________
        frame1 = Frame(self.hashmat, bg='tomato').place(x=500, y=100, width=800, height=500)

        # _____________________| image in Frame1 in login window |__________________________
        self.log = ImageTk.PhotoImage(file="C:/images/login3.png")
        log = Label(frame1, image=self.log).place(x=152, y=120, width=451, height=450)

        # ____________________| title in frame1 in login window |__________________________
        title1 = Label(frame1, text="Sindh Madersatul Islam University", width='46', font=("times new roman", 20),
                       fg="white", bg="black").place(x=604, y=120)


        #..........................| variable for catch data from entry box in login window |..............................
        self.login = StringVar()
        self.password = StringVar()
        #................................| labels and entrys in login window |..........................................
        lbl = Label(self.hashmat, text="User Name", width='10', font=("times new roman", 15),fg='white',bg="black").place(x=650, y=200)
        entry = Entry(self.hashmat, textvariable=self.login, width=35, ).place(x=780, y=200, height=29)
        lbl1 = Label(self.hashmat, text="User Pasword", width='10', font=("times new roman", 15),fg='white',bg="black").place(x=650, y=300)
        entry1 = Entry(self.hashmat, textvariable=self.password, width=35, show="*").place(x=780, y=300, height=29)
        #....................................| button in login window |.................................
        btn = Button(frame1, text="Exit", width="20", font=("times new roman", 15), command=self.exit,activebackground="red").place(x=900, y=380)
        btn = Button(frame1, text="Login", width="20", font=("times new roman", 15), command=self.submit,activebackground="red").place(x=650, y=380)

    def exit(self):
        MsgBox = messagebox.askquestion('Exit Quiz Game', 'Are you sure you want to exit the quiz', icon='warning')
        if MsgBox == 'yes':
            self.hashmat.destroy()
            # else:
            #     messagebox.showinfo('Return', 'You will now return to the quiz game')
            # btn = Button(frame1, text="Login", width="20", font=("times new roman", 15), command=self.submit,activebackground="red").place(x=650, y=380)



#..................................| function in login window |....................................
    def submit(self):
#............| get user id and password |..................
       self.login.get()
       self.password.get()
#........| Condition After getting value |...............................
       if self.login.get()== "":
           messagebox.showerror("Error","Please Enter User id!")
       elif self.password.get()== "":
           messagebox.showerror("Error", "Please Enter User Pasword!")
       else:
           messagebox.showinfo("Info", "You have successfull login")
           self.hashmat.destroy()
           # main.get()
           # main(login)
#............| Function for call back window |.....................
           def back():
# ...............................| creating window after login for choosing subjects |.................................
               subjects = Tk()
               subjects.geometry('1360x768')
               subjects.configure(background="powderblue")
               subjects.title("Select Subjects")
# ...........................| label in subjects window |........................
               lbl1 = Label(subjects, text="Choose Subject for Quiz", width=62, font=("times new roman", 30),bg="gray17",fg="white").place(x=0, y=0)
# ...........................| Image in subjects window |.......................
#                log = ImageTk.PhotoImage(file="C:/images/quiz1.jpg", width=452, height=451)
#                log = Label(subjects, image=log).place(x=450, y=120)
               frame=Frame(subjects, width=452, height=451,bg="gray32").place(x=450, y=120)
               # .........................| Window title, configuration and background color in subjects window|.......................


# .............................| Choosing subject for Function for new window click on radio button |.....................
               def radEvent():
    # ....................| storing variable |..........................
                   radSelected = radValues.get()
    # .....................| Condition for first radio button |..........................
                   if radSelected == 1:
    # .......................| subjects windows Screen Destroy |.....................................
                       subjects.destroy()
    # ................................| New Window open click on first radio button (first window part1)|............
                       subject1 = Tk()

    # ...........................| subject1 window title, geometry and |.....................
                       subject1.title("Pthon Quiz")
                       subject1.geometry("1360x760")

    # .......................| Function Connect with submit and back button |..............................
                       def back1():
                           subject1.destroy()
                           back()

                       def Submit():
                           # ......................| condiotion for Q1 |...................
                           select1 = var.get()

                           if select1 == 1:
                               marks1 = 5
                               # print(marks1)

                           else:
                               marks1 = 0

                           # ......................| condiotion for Q2 |...................
                           select2 = var1.get()

                           if select2 == 3:
                               marks2 = 5
                               # print(marks2)
                           else:
                               marks2 = 0

                           # ......................| condiotion for Q3 |...................
                           select3 = var2.get()

                           if select3 == 2:
                               marks3 = 5

                           else:
                               marks3 = 0


                           # ......................| condiotion for Q4 |...................
                           select4 = var3.get()

                           if select4 == 3:
                               marks4 = 5

                           else:
                               marks4 = 0

                           # ......................| condiotion for Q5 |...................
                           select5 = var4.get()

                           if select5 == 1:
                               marks5 = 5

                           else:
                               marks5 = 0

                           # ......................| condiotion for Q6 |...................
                           select6 = var5.get()

                           if select6 == 1:
                               marks6 = 5

                           else:
                               marks6 = 0

                           # ......................| condiotion for Q7 |...................
                           select7 = var6.get()

                           if select7 == 2:
                               marks7 = 5

                           else:
                               marks7 = 0
                           # ......................| condiotion for Q8 |...................
                           select8 = var7.get()

                           if select8 == 1:
                               marks8 = 5
                           else:
                               marks8 = 0
                           # ......................| condiotion for Q9 |...................
                           select9 = var8.get()

                           if select9 == 1:
                               marks9 = 5
                           else:
                               marks9 = 0
                           # ......................| condiotion for Q10 |...................
                           select10 = var9.get()

                           if select10 == 2:
                               marks10 = 5
                           else:
                               marks10 = 0
#...........................| Condition for empty radio button here |...........................
                           if select1 == 0 or select2 == 0 or select3 == 0 or select4 == 0 or select5 == 0 or select6 == 0 or select7 == 0 or select8 == 0 or select9 == 0 or select10 == 0:
                               messagebox.showerror("Error", "Please Attempt All Questions! \n Before Submition")
                           else:
                               messagebox.showinfo("Info", "Your Quiz has been submitted")
#............................| here subject1 window destroy |..............................
                               subject1.destroy()
#............................| here new window create for show result |...................................
                               # ...
                               result = Tk()
#............................| Resuklt window title and geometry and confuguration |.....................................
                               result.title("Result Quiz")
                               result.geometry("500x400")
                               result.configure(background="darkgray")
#............................| Here calculation for totall marks |...............................................
                               marks0 = marks1 + marks2 + marks3 + marks4 + marks5 + marks6 + marks7 + marks8 + marks9 + marks10
                               print("Total Marks", marks0)
                               percentage = (marks0) * (100) / (50)
                               print("Your percentage is: - ", percentage, "%")

#.............................| here label on top of the screen |.............................................
                               label1=Label(result,text="Your Quiz Result", font=("times new roman", 15),fg='black',bg="darkkhaki",width=45).place(x=0,y=0)
                               # label2=Label(result,text="Subject: -",width=20).place()
                               label3 = Label(result, text="Subject: -", width=20, fg="black").place(x=130, y=50)
                               label4 = Label(result, text="Python", width=20, fg="red").place(x=270, y=50)
#.............................,| here will show user marks and percentage|..........................................................
                               marks11 = "Your Marks: "+str(marks0)
                               label5 = Label(result,text=marks11,width=20).place(x=200,y=100)
                               percentage_final = "Your Quiz Percentage:  " +str(percentage) + "%"
                               label6 =Label(result,text=percentage_final,width=40).place(x=130,y=150)
#...............................| Condition for grade in result window |.................................................
                               if percentage >= 90:
                                   Your_Grade = '"A+"'
                                   Grade = "Your Grade is: " + str(Your_Grade)+ "\n Congratulation Buddy"
                                   Label(result,text=Grade,width=20,bg="green").place(x=200,y=200)
                               elif percentage >= 80:
                                    Your_Grade = '"A+"'
                                    Grade = "Your Grade is: " + str(Your_Grade)+ "\n Congratulation Buddy"
                                    Label(result,text=Grade,width=20,bg="green").place(x=200,y=200)
                               elif percentage >= 70:
                                    Your_Grade = '"A"'
                                    Grade = "Your Grade is: " + str(Your_Grade)+ "\n You are Good Working! Keep doing"
                                    Label(result, text=Grade, width=30,bg="green").place(x=200, y=200)
                               elif percentage >= 60:
                                    Your_Grade = '"B"'
                                    Grade = "Your Grade is: " + str(Your_Grade)+ "\n you are in progress"
                                    Label(result,text=Grade,width=20,bg="green").place(x=200,y=200)
                               elif percentage >= 50:
                                    Your_Grade = '"C"'
                                    Grade = "Your Grade is: " + str(Your_Grade)+ "\n You need to do struggle"
                                    Label(result,text=Grade,width=20,bg="yellow").place(x=200,y=200)

                                    def back0():
                                        result.destroy()
                                        back()

                                    btn = Button(result, text="Try Again", width=20, activebackground="red",command=back0, bg="powderblue").place(x=200, y=300)
                               elif percentage >= 40:
                                    Your_Grade = '"D"'
                                    Grade = "Your Grade is: " + str(Your_Grade)+ "\n You need to do Struggle"
                                    Label(result,text=Grade,width=20,bg="orange").place(x=200,y=200)

                                    def back0():
                                        result.destroy()
                                        back()

                                    btn = Button(result, text="Try Again", width=20, activebackground="red",command=back0, bg="powderblue").place(x=200, y=300)
                               else:
                                   Your_Grade = '"F'
                                   Grade = "Your Grade is: " + str(Your_Grade)+ "\nYou Need to Hard Work"
                                   Label(result, text=Grade, width=20,bg="red").place(x=200, y=200)

                                   def back0():
                                       result.destroy()
                                       back()

                                   btn = Button(result, text="Try Again", width=20, activebackground="red",command=back0, bg="powderblue").place(x=200, y=300)


#..............................| Exit button |....................................
                               def exit():

                                   MsgBox = messagebox.askquestion('Exit Quiz Game','Are you sure you want to exit the quiz',icon='warning')
                                   if MsgBox == 'yes':
                                       result.destroy()
                                   # else:
                                   #     messagebox.showinfo('Return', 'You will now return to the quiz game')
                               # def back0():
                               #     result.destroy()
                               #     back()
                               # ...................| Exit button and try again button here |..............................
                               btn=Button(result, text="Exit", width=20, activebackground="red", command=exit,bg="powderblue").place(x=200, y=250)
                               # btn=Button(result, text="Try Again", width=20, activebackground="red", command=back0,bg="powderblue").place(x=200, y=300)
                               result.mainloop()
#..............................| here result window lock |..........................................
                               result.mainloop()
                           # subject1.destroy()

                        # .........................| Button in subject1 window |.........................
                       b1 = Button(subject1, text='Submit', command=Submit, fg='blue', bg="cadet blue", activebackground='red',
                                    font='Helvetica 10 bold', width=20).place(x=1150, y=650)

                       b2 = Button(subject1, text='Back', command=back1, fg='blue', bg="cadet blue", activebackground='sky blue',
                                    font='Helvetica 10 bold', width=20).place(x=900, y=650)

                        # .................| Q1 in subject1 window |...........................
                       Q1 = Label(subject1,text='1. What is a correct syntax to output "Hello world" in Python?', font='Helvetica 10 bold').place(x=10, y=60)
                        # .....................| storing data for applying condition on radio button |.........................
                       var = IntVar()
                        # ......................| Option for Q1 in subject1 window |...............................
                       Radiobutton(subject1, text='print("Hello World")', padx=5, variable=var, value=1, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=80)
                       Radiobutton(subject1, text='echo "Hello World"', padx=5, variable=var, value=2, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=100)
                       Radiobutton(subject1, text='echo("Hello World");', padx=5, variable=var, value=3, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=120)
                        # .................| Q2 in subject1 window |...........................
                       Q2 = Label(subject1, text="2. How do you insert COMMENTS in Python code?", font='Helvetica 10 bold').place(x=10,
                                                                                                                                   y=180)
                        # .....................| storing data for applying condition on radio button |.........................
                       var1 = IntVar()
                        # ......................| Option for Q2 in subject1 window |...............................
                       Radiobutton(subject1, text="//This is a comment", padx=5, variable=var1, value=1, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=200)
                       Radiobutton(subject1, text="/This is a comment/", padx=5, variable=var1, value=2, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=220)
                       Radiobutton(subject1, text="#This is a comment", padx=5, variable=var1, value=3, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=240)
                        # .................| Q3 in subject1 window |...........................
                       Q3 = Label(subject1, text="3. Which one is NOT a legal variable name?", font='Helvetica 10 bold').place(x=10, y=300)
                        # .....................| storing data for applying condition on radio button |.........................
                       var2 = IntVar()
                        # ......................| Option for Q3 in subject1 window |...............................
                       Radiobutton(subject1, text="my_var", padx=5, variable=var2, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=320)
                       Radiobutton(subject1, text="Myvar", padx=5, variable=var2, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=340)
                       Radiobutton(subject1, text="my-var", padx=5, variable=var2, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=360)
                        # .................| Q4 in subject1 window |...........................
                       Q4 = Label(subject1, text="4. How do you create a variable with the numeric value 5?",
                                   font='Helvetica 10 bold').place(
                            x=10, y=420)

                        # .....................| storing data for applying condition on radio button |.........................
                       var3 = IntVar()
                        # ......................| Option for Q4 in subject1 window |...............................
                       Radiobutton(subject1, text="x = int(0.5)", padx=5, variable=var3, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=440)
                       Radiobutton(subject1, text="x = int(10)", padx=5, variable=var3, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=460)
                       Radiobutton(subject1, text="x = int(5)", padx=5, variable=var3, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=480)
                        # .................| Q5 in subject1 window |...........................
                       Q5 = Label(subject1, text="5. What is the correct file extension for Python files?",
                                   font='Helvetica 10 bold').place(
                            x=10, y=540)
                        # .....................| storing data for applying condition on radio button |.........................
                       var4 = IntVar()
                        # ......................| Option for Q5 in subject1 window |...............................
                       Radiobutton(subject1, text=".py", padx=5, variable=var4, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=560)
                       Radiobutton(subject1, text=".pyt", padx=5, variable=var4, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(
                            x=10, y=580)
                       Radiobutton(subject1, text=".pt", padx=5, variable=var4, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(
                            x=10, y=600)
                        # .................| Q6 in subject1 window |...........................
                       Q6 = Label(subject1,
                                   text="6.Which method can be used to remove any whitespace from both the beginning and the end of a string?",
                                   font='Helvetica 10 bold').place(x=600, y=60)

                        # .....................| storing data for applying condition on radio button |.........................
                       var5 = IntVar()
                        # ......................| Option for Q6 in subject1 window |...............................
                       Radiobutton(subject1, text="strip()", padx=5, variable=var5, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=80)
                       Radiobutton(subject1, text="ptrim()", padx=5, variable=var5, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=100)
                       Radiobutton(subject1, text="trim()", padx=5, variable=var5, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=120)
                        # .................| Q7 in subject1 window |...........................
                       Q7 = Label(subject1, text="7. Which method can be used to return a string in upper case letters?",
                                   font='Helvetica 10 bold').place(x=600, y=180)
                        # .....................| storing data for applying condition on radio button |.........................
                       var6 = IntVar()
                        # ......................| Option for Q7 in subject1 window |...............................
                       Radiobutton(subject1, text="uppercase()", padx=5, variable=var6, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=200)
                       Radiobutton(subject1, text="upper()", padx=5, variable=var6, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=220)
                       Radiobutton(subject1, text="upperCase()", padx=5, variable=var6, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=240)
                        # .................| Q8 in subject1 window |...........................
                       Q8 = Label(subject1, text="8. Which method can be used to replace parts of a string?",
                                   font='Helvetica 10 bold').place(
                            x=600, y=300)
                        # .....................| storing data for applying condition on radio button |.........................
                       var7 = IntVar()
                        # ......................| Option for Q8 in subject1 window |...............................
                       Radiobutton(subject1, text="replace()", padx=5, variable=var7, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=320)
                       Radiobutton(subject1, text="switch()", padx=5, variable=var7, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=340)
                       Radiobutton(subject1, text="repl()", padx=5, variable=var7, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=360)
                        # .................| Q8 in subject1 window |...........................
                       Q9 = Label(subject1, text="9. Which operator is used to multiply numbers?", font='Helvetica 10 bold').place(x=600,
                                                                                                                                    y=420)
                        # .....................| storing data for applying condition on radio button |.........................
                       var8 = IntVar()
                        # ......................| Option for Q9 in subject1 window |...............................
                       Radiobutton(subject1, text="*", padx=5, variable=var8, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(
                            x=600, y=440)
                       Radiobutton(subject1, text="/", padx=5, variable=var8, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(
                            x=600, y=460)
                       Radiobutton(subject1, text="%", padx=5, variable=var8, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(
                            x=600, y=480)
                        # .................| Q10 in subject1 window |...........................
                       Q10 = Label(subject1, text="10. How do you start writing a while loop in Python? ", font='Helvetica 10 bold').place(
                            x=600, y=540)
                        # .....................| storing data for applying condition on radio button |.........................
                       var9 = IntVar()
                        # ......................| Option for Q10 in subject1 window |...............................
                       Radiobutton(subject1, text="x > y while {", padx=5, variable=var9, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=560)
                       Radiobutton(subject1, text="while x > y:", padx=5, variable=var9, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=580)
                       Radiobutton(subject1, text="while (x > y)", padx=5, variable=var9, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=600)
    # .....................................| subject1 window  in Label  |............................
                       Label(subject1, text="Welcome To Python Quiz", font=("times new roman", 35)).place(x=340, y=0)  # here stop new window
                       subject1.mainloop()
                       # .....................| Condition for second radio button |..........................
                   elif radSelected == 2:
    # ................................| New Window open click on first radio button (subject2)|............
                       subjects.destroy()
    # ...........................| subjects2 window title, geometry and |.....................
                       subject2 = Tk()
                       subject2.title("Calculus Quiz")
                       subject2.geometry("1360x760")
#.......................| Function Connect with submit and back button in subject2 |..............................
                       def back1():
                           subject2.destroy()
                           back()

                       def Submit():
                            # ......................| condiotion for Q1 in suhject3 window |...................
                           select1 = var.get()

                           if select1 == 1:
                               marks1 = 5

                           else:
                               marks1 = 0
                                # print(marks1)

                            # ......................| condiotion for Q2 in suhject3 window |...................
                           select2 = var1.get()

                           if select2 == 3:
                               marks2 = 5
                           else:
                               marks2 = 0
                                # print(marks2)
                            # ......................| condiotion for Q3 in suhject3 window |...................
                           select3 = var2.get()


                           if select3 == 1:
                               marks3 = 5

                           else:
                               marks3 = 0
                                # print(marks3)

                            # ......................| condiotion for Q4 in suhject3 window |...................
                           select4 = var3.get()

                           if select4 == 2:
                               marks4 = 5

                           else:
                               marks4 = 0
                                # print(marks4)
                            # ......................| condiotion for Q5 in suhject3 window |...................
                           select5 = var4.get()

                           if select5 == 3:
                                marks5 = 5

                           else:
                               marks5 = 0
                                # print(marks4)
                            # ......................| condiotion for Q6 in suhject3 window |...................
                           select6 = var5.get()

                           if select6 == 2:
                               marks6 = 5

                           else:
                               marks6 = 0
                                # print(marks4)
                            # ......................| condiotion for Q7 in suhject3 window |...................
                           select7 = var6.get()

                           if select7 == 1:
                               marks7 = 5

                                # print(marks4)
                           else:
                               marks7 = 0
                                # print(marks4)
                            # ......................| condiotion for Q8 in suhject3 window |...................
                           select8 = var7.get()

                           if select8 == 3:
                               marks8 = 5

                           else:
                               marks8 = 0
                                # print(marks4)
                            # ......................| condiotion for Q9 in suhject3 window |...................
                           select9 = var8.get()

                           if select9 == 1:
                               marks9 = 5

                           else:
                               marks9 = 0
                                # print(marks4)
                            # ......................| condiotion for Q10 in suhject3 window |...................
                           select10 = var9.get()

                           if select10 == 1:
                               marks10 = 5

                           else:
                               marks10 = 0

                           if select1 == 0 or select2 == 0 or select3 == 0 or select4 == 0 or select5 == 0 or select6 == 0 or select7 == 0 or select8 == 0 or select9 == 0 or select10 == 0:
                               messagebox.showerror("Error", "Please Attempt All Questions \n Before Submitting")
                           else:
                               messagebox.showinfo("Info", "Your Quiz has been submitted")
                                   # ............................| here subject1 window destroy |..............................
                               subject2.destroy()
                                   # ............................| here new window create for show result |......................................
                               result = Tk()
                                   # ............................| Resuklt window title and geometry and confuguration |.....................................
                               result.title("Result Quiz")
                               result.geometry("500x400")
                               result.configure(background="darkgray")
                                   # ............................| Here calculation for totall marks |...............................................
                               marks0 = marks1 + marks2 + marks3 + marks4 + marks5 + marks6 + marks7 + marks8 + marks9 + marks10
                               print("Tootal Marks", marks0)
                               percentage = (marks0) * (100) / (50)
                               print("Your percentage", percentage, "%")

                                   # .............................| here label on top of the screen |.............................................
                               label1 = Label(result, text="Your Quiz Result", font=("times new roman", 15),
                                                  fg='black', bg="darkkhaki", width=45).place(x=0, y=0)
                               label2 = Label(result, text="Subject: -", width=20).place()
                               label3 = Label(result, text="Subject: -", width=20, fg="black").place(x=130, y=50)
                               label4 = Label(result, text="ICT", width=20, fg="red").place(x=270, y=50)
                                   # .............................,| here will show user marks and percentage|..........................................................
                               marks11 = "Your Marks: " + str(marks0)
                               label5 = Label(result, text=marks11, width=20).place(x=200, y=100)
                               percentage_final = "Your Quiz Percentage: " + str(percentage) + "%"
                               label6 = Label(result, text=percentage_final, width=40).place(x=130, y=150)
                               # .............................| here label on top of the screen |.............................................
                               label1 = Label(result, text="Your Quiz Result", font=("times new roman", 15), fg='black',
                                              bg="darkkhaki", width=45).place(x=0, y=0)
                               # label2=Label(result,text="Subject: -",width=20).place()
                               label3 = Label(result, text="Subject: -", width=20, fg="black").place(x=130, y=50)
                               label4 = Label(result, text="Python", width=20, fg="red").place(x=270, y=50)
                               # .............................,| here will show user marks and percentage|..........................................................
                               marks11 = "Your Marks: " + str(marks0)
                               label5 = Label(result, text=marks11, width=20).place(x=200, y=100)
                               percentage_final = "Your Quiz Percentage:  " + str(percentage) + "%"
                               label6 = Label(result, text=percentage_final, width=40).place(x=130, y=150)
                               # ...............................| Condition for grade in result window |.................................................
                               if percentage >= 90:
                                   Your_Grade = '"A+"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n Congratulation Buddy"
                                   Label(result, text=Grade, width=20, bg="green").place(x=200, y=200)
                               elif percentage >= 80:
                                   Your_Grade = '"A+"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n Congratulation Buddy"
                                   Label(result, text=Grade, width=20, bg="green").place(x=200, y=200)
                               elif percentage >= 70:
                                   Your_Grade = '"A"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n You are Good Working! Keep doing"
                                   Label(result, text=Grade, width=30, bg="green").place(x=200, y=200)
                               elif percentage >= 60:
                                   Your_Grade = '"B"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n you are in progress"
                                   Label(result, text=Grade, width=20, bg="green").place(x=200, y=200)
                               elif percentage >= 50:
                                   Your_Grade = '"C"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n You need to do struggle"
                                   Label(result, text=Grade, width=20, bg="yellow").place(x=200, y=200)

                                   def back0():
                                       result.destroy()
                                       back()

                                   btn = Button(result, text="Try Again", width=20, activebackground="red",command=back0, bg="powderblue").place(x=200, y=300)
                               elif percentage >= 40:
                                   Your_Grade = '"D"'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\n You need to do Struggle"
                                   Label(result, text=Grade, width=20, bg="orange").place(x=200, y=200)

                                   def back0():
                                       result.destroy()
                                       back()

                                   btn = Button(result, text="Try Again", width=20, activebackground="red",
                                                command=back0, bg="powderblue").place(x=200, y=300)
                               else:
                                   Your_Grade = '"F'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\nYou Need to Hard Work"
                                   Label(result, text=Grade, width=20, bg="red").place(x=200, y=200)

                                   def back0():
                                       result.destroy()
                                       back()

                                   btn = Button(result, text="Try Again", width=20, activebackground="red",command=back0, bg="powderblue").place(x=200, y=300)
                               #.....................| Exit button function |.......................
                               def exit():

                                   MsgBox = messagebox.askquestion('Exit Application','Are you sure you want to exit the quiz',icon='warning')
                                   if MsgBox == 'yes':
                                       result.destroy()
                                   else:
                                       messagebox.showinfo('Return', 'You will now return to the quiz game')
                               #......................| back function for call again window subjects |.................................
                               # def back0():
                               #     result.destroy()
                               #     back()
                               # ...................| Exit and try again button and here |..............................
                               btn=Button(result, text="Exit", width=20, activebackground="red", command=exit,bg="powderblue").place(x=200, y=250)
                               # btn=Button(result, text="Try Again", width=20, activebackground="red", command=back0,bg="powderblue").place(x=200, y=300)
                               result.mainloop()
                                   # ..............................| here result window lock |..........................................
                               result.mainloop()

#.........................| Button in subject2 window |.........................
                       b1 = Button(subject2, text='Submit', command=Submit, fg='blue', bg="cadet blue", activebackground='red',
                                    font='Helvetica 10 bold', width=20).place(x=1150, y=650)

                       b2 = Button(subject2, text='Back', command=back1, fg='blue', bg="cadet blue", activebackground='sky blue',
                                    font='Helvetica 10 bold', width=20).place(x=900, y=650)

                        # .................| Q1 in subject2 window |...........................
                       Q1 = Label(subject2, text='1. ENIAC was ?', font='Helvetica 10 bold').place(x=10, y=60)
                        # .....................| storing data for applying condition on radio button |.........................
                       var = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text='An electronic computer', padx=5, variable=var, value=1, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=80)
                       Radiobutton(subject2, text='An engine', padx=5, variable=var, value=2, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=100)
                       Radiobutton(subject2, text='A memory device', padx=5, variable=var, value=3, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=120)
                        # .................| Q2 in subject2 window |...........................
                       Q2 = Label(subject2, text="2. The _ controls a client computer's resources ?", font='Helvetica 10 bold').place(x=10,
                                                                                                                                       y=180)
                        # .....................| storing data for applying condition on radio button |.........................
                       var1 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Application program", padx=5, variable=var1, value=1, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=200)
                       Radiobutton(subject2, text="Instruction set", padx=5, variable=var1, value=2, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=220)
                       Radiobutton(subject2, text="Server application", padx=5, variable=var1, value=3, cursor="hand2", fg='blue',
                                    activebackground='sky blue').place(x=10, y=240)
                        # .................| Q3 in subject2 window |...........................
                       Q3 = Label(subject2, text="3. 1024 bytes equal to?", font='Helvetica 10 bold').place(x=10, y=300)
                        # .....................| storing data fhor applying condition on radio button |.........................
                       var2 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="1 KB", padx=5, variable=var2, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=320)
                       Radiobutton(subject2, text="1 GB", padx=5, variable=var2, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=340)
                       Radiobutton(subject2, text="1 TB", padx=5, variable=var2, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=360)
                        # .................| Q4 in subject2 window |...........................
                       Q4 = Label(subject2, text="4. In a computer who is capable to store single binary bit?",
                                   font='Helvetica 10 bold').place(
                            x=10, y=420)
                        # .....................| storing data for applying condition on radio button |.........................
                       var3 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Capacitor", padx=5, variable=var3, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=440)
                       Radiobutton(subject2, text="Flip flop", padx=5, variable=var3, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=460)
                       Radiobutton(subject2, text="Register", padx=5, variable=var3, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=480)
                        # .................| Q5 in subject2 window |...........................
                       Q5 = Label(subject2, text="5. A parallel port is most often used by a?", font='Helvetica 10 bold').place(
                            x=10, y=540)
                        # .....................| storing data for applying condition on radio button |.........................
                       var4 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Mouse", padx=5, variable=var4, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=560)
                       Radiobutton(subject2, text="Monitor", padx=5, variable=var4, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=580)
                       Radiobutton(subject2, text="Printer", padx=5, variable=var4, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=10, y=600)
                        # .................| Q6 in subject2 window |...........................
                       Q6 = Label(subject2, text="6.Where are program and data to be used by the computer avialable?",
                                   font='Helvetica 10 bold').place(x=600, y=60)

                        # .....................| storing data for applying condition on radio button |.........................
                       var5 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Output", padx=5, variable=var5, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=80)
                       Radiobutton(subject2, text="Storage", padx=5, variable=var5, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=100)
                       Radiobutton(subject2, text="Processing unit", padx=5, variable=var5, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=120)
                        # .................| Q7 in subject2 window |...........................
                       Q7 = Label(subject2, text="7. What is the commonly used unit for measuring the sped od data transmission?",
                                   font='Helvetica 10 bold').place(x=600, y=180)
                        # .....................| storing data for applying condition on radio button |.........................
                       var6 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Bit per second", padx=5, variable=var6, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=200)
                       Radiobutton(subject2, text="Nano seconds", padx=5, variable=var6, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=220)
                       Radiobutton(subject2, text="Characters per second", padx=5, variable=var6, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=240)
                        # .................| Q8 in subject2 window |...........................
                       Q8 = Label(subject2, text="8. The main memory of a computer can also be called__?", font='Helvetica 10 bold').place(
                            x=600, y=300)
                        # .....................| storing data for applying condition on radio button |.........................
                       var7 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="Primary storage", padx=5, variable=var7, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=320)
                       Radiobutton(subject2, text="Internal memory", padx=5, variable=var7, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=340)
                       Radiobutton(subject2, text="Primary memory", padx=5, variable=var7, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=360)
                        # .................| Q9 in subject2 window |...........................
                       Q9 = Label(subject2, text="9. The primary purpose of an operating system is __?", font='Helvetica 10 bold').place(
                            x=600, y=420)
                        # .....................| storing data for applying condition on radio button |.........................
                       var8 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="To make the most efficient use of the computer hardware?", padx=5, variable=var8,
                                    value=1, cursor="hand2", fg='blue', activebackground='skyblue').place(x=600, y=440)
                       Radiobutton(subject2, text="To allow people to use the computer", padx=5, variable=var8, value=2, cursor="hand2",
                                    fg='blue', activebackground='skyblue').place(x=600, y=460)
                       Radiobutton(subject2, text="To keep system programmers employed", padx=5, variable=var8, value=3, cursor="hand2",
                                    fg='blue', activebackground='skyblue').place(x=600, y=480)
                        # .................| Q10 in subject2 window |...........................
                       Q10 = Label(subject2, text="10. Integrated circuits contained ? ", font='Helvetica 10 bold').place(x=600, y=540)
                        # .....................| storing data for applying condition on radio button |.........................
                       var9 = IntVar()
                        # ......................| option for Question in subject2 |..................................
                       Radiobutton(subject2, text="10 to 20 components", padx=5, variable=var9, value=1, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=560)
                       Radiobutton(subject2, text="20 to 30 components", padx=5, variable=var9, value=2, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=580)
                       Radiobutton(subject2, text="35 to 25 components", padx=5, variable=var9, value=3, cursor="hand2", fg='blue',
                                    activebackground='skyblue').place(x=600, y=600)

    # .....................................| subject2 window in Label |............................
                       Label(subject2, text="Welcome to ICT Quiz", font=("times new roman", 35)).place(x=380, y=0)  # here stop new window
                       subject2.mainloop()
    # .....................| Condition for third radio button |..........................
                   elif radSelected == 3:
    # ................................| New Window open click on first radio button (subject3)|............
                       subjects.destroy()
    # ...........................| subject3 window title, geometry and |.....................
                       subject3 = Tk()
                       subject3.title("English Quiz")
                       subject3.geometry("1360x760")
    # ............................| Here Quiz start in Subject 3 window|..............................

                       lbl = Label(subject3, text="Welcome To English Quiz",width=20, font=("times new roman", 35)).place(x=340, y=0)

#.......................| function for call back subjects window on click |.......................
                       def back1():
                           subject3.destroy()
                           back()

    # ...................| Function |......................
# ..........| Submit Function in subject3 window in this function on click result will be show |......................
                       def Submit():
                            # ......................| condiotion for Q1 in suhject3 window |...................
                           select1 = var.get()

                           if select1 == 1:
                               marks1 = 5

                           else:
                               marks1 = 0
                                # print(marks1)

                            # ......................| condiotion for Q2 in suhject3 window |...................
                           select2 = var1.get()

                           if select2 == 1:
                               marks2 = 5
                           else:
                               marks2 = 0
                                # print(marks2)
                            # ......................| condiotion for Q3 in suhject3 window |...................
                           select3 = var2.get()


                           if select3 == 2:
                               marks3 = 5

                           else:
                               marks3 = 0
                                # print(marks3)

                            # ......................| condiotion for Q4 in suhject3 window |...................
                           select4 = var3.get()

                           if select4 == 3:
                               marks4 = 5

                           else:
                               marks4 = 0
                                # print(marks4)
                            # ......................| condiotion for Q5 in suhject3 window |...................
                           select5 = var4.get()

                           if select5 == 2:
                                marks5 = 5

                           else:
                               marks5 = 0
                                # print(marks4)
                            # ......................| condiotion for Q6 in suhject3 window |...................
                           select6 = var5.get()

                           if select6 == 3:
                               marks6 = 5

                           else:
                               marks6 = 0
                                # print(marks4)
                            # ......................| condiotion for Q7 in suhject3 window |...................
                           select7 = var6.get()

                           if select7 == 1:
                               marks7 = 5

                                # print(marks4)
                           else:
                               marks7 = 0
                                # print(marks4)
                            # ......................| condiotion for Q8 in suhject3 window |...................
                           select8 = var7.get()

                           if select8 == 3:
                               marks8 = 5

                           else:
                               marks8 = 0
                                # print(marks4)
                            # ......................| condiotion for Q9 in suhject3 window |...................
                           select9 = var8.get()

                           if select9 == 2:
                               marks9 = 5

                           else:
                               marks9 = 0
                                # print(marks4)
                            # ......................| condiotion for Q10 in suhject3 window |...................
                           select10 = var9.get()

                           if select10 == 3:
                               marks10 = 5

                           else:
                               marks10 = 0
                                # print(marks4)
                           if select1 == 0 or select2 == 0 or select3 == 0 or select4 == 0 or select5 == 0 or select6 == 0 or select7 == 0 or select8 == 0 or select9 == 0 or select10 == 0:
                               messagebox.showerror("Error", "Please Attempt All Question \n Before Submitting")
                           else:
                               messagebox.showinfo("Info", "Your Quiz has been submitted")
                                   # ............................| here subject1 window destroy |..............................
                               subject3.destroy()
                                   # ............................| here new window create for show result |......................................
                               result = Tk()
                                   # ............................| Resuklt window title and geometry and confuguration |.....................................
                               result.title("Result Quiz")
                               result.geometry("500x400")
                               result.configure(background="darkgray")
                                   # ............................| Here calculation for totall marks |...............................................
                               marks0 = marks1 + marks2 + marks3 + marks4 + marks5 + marks6 + marks7 + marks8 + marks9 + marks10
                               print("Tootal Marks", marks0)
                               percentage = (marks0) * (100) / (50)
                               print("Your percentage", percentage, "%")

                                   # .............................| here label on top of the screen |.............................................
                               label1 = Label(result, text="Your Quiz Result", font=("times new roman", 15),
                                                  fg='black', bg="darkkhaki", width=45).place(x=0, y=0)
                               label3 = Label(result, text="Subject: -", width=20, fg="black").place(x=130, y=50)
                               label4 = Label(result, text="English", width=20, fg="red").place(x=270, y=50)
                                   # .............................,| here will show user marks and percentage|..........................................................
                               marks11 = "Your Marks: - " + str(marks0)
                               label5 = Label(result, text=marks11, width=20).place(x=200, y=100)
                               percentage_final = "Your Quiz Percentage: - " + str(percentage) + "%"
                               label6 = Label(result, text=percentage_final, width=40).place(x=130, y=150)
                               # .............................| here label on top of the screen |.............................................
                               label1 = Label(result, text="Your Quiz Result", font=("times new roman", 15), fg='black',
                                              bg="darkkhaki", width=45).place(x=0, y=0)
                               # label2=Label(result,text="Subject: -",width=20).place()
                               label3 = Label(result, text="Subject: -", width=20, fg="black").place(x=130, y=50)
                               label4 = Label(result, text="Python", width=20, fg="red").place(x=270, y=50)
                               # .............................,| here will show user marks and percentage|..........................................................
                               marks11 = "Your Marks: " + str(marks0)
                               label5 = Label(result, text=marks11, width=20).place(x=200, y=100)
                               percentage_final = "Your Quiz Percentage:  " + str(percentage) + "%"
                               label6 = Label(result, text=percentage_final, width=40).place(x=130, y=150)
                               # ...............................| Condition for grade in result window |.................................................
                               if percentage >= 90:
                                   Your_Grade = '"A+"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               elif percentage >= 80:
                                   Your_Grade = '"A+"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               elif percentage >= 70:
                                   Your_Grade = '"A"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               elif percentage >= 60:
                                   Your_Grade = '"B"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               elif percentage >= 50:
                                   Your_Grade = '"C"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               elif percentage >= 50:
                                   Your_Grade = '"C"'
                                   Grade = "Your Grade is: " + str(Your_Grade)
                                   Label(result, text=Grade, width=20).place(x=200, y=200)
                               else:
                                   Your_Grade = '"F'
                                   Grade = "Your Grade is: " + str(Your_Grade) + "\nYou Need to Hard Work"
                                   Label(result, text=Grade, width=20, bg="red").place(x=200, y=200)

                                   def back0():
                                       result.destroy()
                                       back()

                                   btn = Button(result, text="Try Again", width=20, activebackground="red",
                                                command=back0, bg="powderblue").place(x=200, y=300)
                               #................| Exit function for exit for all |.................................
                               def exit():

                                   MsgBox = messagebox.askquestion('Exit Application','Are you sure you want to exit the quiz',icon='warning')
                                   if MsgBox == 'yes':
                                       result.destroy()
                                   else:
                                       messagebox.showinfo('Return', 'You will now return to the quiz game')
                               #................| back function for call again subjects woindow |....................
                               # def back0():
                               #     result.destroy()
                               #     back()
                               # ...................| Exit and Trh Again buttons |..............................
                               btn=Button(result, text="Exit", width=20, activebackground="red", command=exit,bg="powderblue").place(x=200, y=250)
                               # btn=Button(result, text="Try Again", width=20, activebackground="red", command=back0,bg="powderblue").place(x=200, y=300)
                               result.mainloop()
                                   # ..............................| here result window lock |..........................................
                               result.mainloop()

    #.........................| Button in subjects3 window |.........................
                       b1 = Button(subject3, text='Submit',command=Submit, fg='blue', bg="cadet blue", activebackground='red', font='Helvetica 10 bold',width=20).place(x=1150, y=650)
                       b2 = Button(subject3, text='Back', command=back1,fg='blue',bg="cadet blue",activebackground='sky blue', font='Helvetica 10 bold',width=20).place(x=900, y=650)




    # ............................| Question 1 in subject3 |............................
                       Q1 = Label(subject3,text="1. Is the following sentence punctuated properly? --> Whenever I eat bananas, I feel like a monkey.",
                                  font=("italic", 9, 'bold')).place(
                           x=10, y=60)
                       # .....................| storing data for applying condition on radio button |.........................
                       var = IntVar()
                       # ......................| option for Question in subject3 |..................................
                       Radiobutton(subject3, text="Yes", padx=5, variable=var, value=1, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold'),
                                   activebackground='red').place(x=10, y=80)
                       Radiobutton(subject3, text="No", padx=5, variable=var, value=2, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold'),
                                   activebackground='red').place(x=10, y=100)
                       Radiobutton(subject3, text="No knowledge", padx=5, variable=var, value=3, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold'),
                                   activebackground='red').place(x=10, y=120)
                       # ............................| Question 2 in subject3 |............................
                       Q2 = Label(subject3, text="2. Which of the following name parts of speech?",
                                  font=("italic", 10, 'bold')).place(x=10, y=180)
                       # .....................| storing data for applying condition on radio button |.........................
                       var1 = IntVar()
                       # ...........................| Option for Question 2 in subject3 |.........................
                       Radiobutton(subject3, text="Adjectives", padx=5, variable=var1, value=1, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold')).place(x=10,
                                                                               y=200)
                       Radiobutton(subject3, text="Adverbs", padx=5, variable=var1, value=2, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold')).place(x=10,
                                                                               y=220)
                       Radiobutton(subject3, text="Subjects", padx=5, variable=var1, value=3, cursor="hand2", fg='blue',
                                   font=("times new roman", 10, 'bold')).place(x=10,
                                                                               y=240)
                       # ..........................| Question 3 in subject3 |...................................
                       Q3 = Label(subject3, text="3. Which sentence is correct?", font=("italic", 10, 'bold')).place(x=10,
                                                                                                                     y=300)
                       # .....................| storing data for applying condition on radio button |.........................
                       var2 = IntVar()
                       # ...........................| Option for Question 2 in subject3 |.........................
                       Radiobutton(subject3, text="I should of called my grandma", padx=5, variable=var2, value=1,
                                   font=("times new roman", 10, 'bold'),
                                   cursor="hand2", fg="blue").place(x=10, y=320)
                       Radiobutton(subject3, text="I should have called my grandma", padx=5, variable=var2, value=2,
                                   font=("times new roman", 10, 'bold'),
                                   cursor="hand2", fg="blue").place(x=10, y=340)
                       Radiobutton(subject3, text="I should having to called my grandma", padx=5, variable=var2, value=3,
                                   font=("times new roman", 10, 'bold'),
                                   cursor="hand2", fg="blue").place(x=10, y=360)
                       # ........................| Question 4 in subject3 |.........................................
                       Q4 = Label(subject3,
                                  text="4. Is the following group of words a phrase or a clause? --> must have jumped",
                                  font=("italic", 10, 'bold')).place(
                           x=10, y=420)
                       # .....................| storing data for applying condition on radio button |.........................
                       var3 = IntVar()
                       # .......................| Option for Question 4 in subject3 |........................................
                       Radiobutton(subject3, text="Clause", padx=5, variable=var3, value=1, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=10,
                                                                                          y=440)
                       Radiobutton(subject3, text="Clause", padx=5, variable=var3, value=2, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=10,
                                                                                          y=460)
                       Radiobutton(subject3, text="Phrase", padx=5, variable=var3, value=3, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=10,
                                                                                          y=480)
                       # .........................| Question 5 in subject3 |....................................
                       Q5 = Label(subject3, text="5. What two things does every sentence need?",
                                  font=("italic", 10, 'bold')).place(x=10, y=540)
                       # .....................| storing data for applying condition on radio button |.........................
                       var4 = IntVar()
                       # .......................| Option for Question 5 in subject3 |....................................
                       Radiobutton(subject3, text="Person", padx=5, variable=var4, value=1, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=10,
                                                                                          y=560)
                       Radiobutton(subject3, text="Verb/Predicate", padx=5, variable=var4, value=2, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(
                           x=10, y=580)
                       Radiobutton(subject3, text="Cat", padx=5, variable=var4, value=3, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=10, y=600)
                       # ........................| Question 6 in subject3 |....................................
                       Q6 = Label(subject3,
                                  text="6. Name the error in the following sentence. --> Spitting out hot lava, my friend took photos as the volcano erupted.",
                                  font=("italic", 10, 'bold')).place(
                           x=600, y=60)
                       # .....................| storing data for applying condition on radio button |.........................
                       var5 = IntVar()
                       # .......................| Option for Question in subject3 |.....................................
                       Radiobutton(subject3, text="Sentence Fragment", padx=5, variable=var5, value=1,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=80)
                       Radiobutton(subject3, text="placed Modifier", padx=5, variable=var5, value=2,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=100)
                       Radiobutton(subject3, text="Misplaced Modifier""placed Modifier", padx=5, variable=var5, value=3, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(
                           x=600, y=120)
                       # ........................| Question 7 in subject3 |...............................
                       Q7 = Label(subject3,
                                  text="7. Which sentence is punctuated properly? (You get bonus points if you know why.)",
                                  font=("italic", 10, 'bold')).place(
                           x=600, y=180)
                       # .....................| storing data for applying condition on radio button |.........................
                       var6 = IntVar()
                       # .......................| Option for Question 7 in subject3 |..............................
                       Radiobutton(subject3, text="The students wanted indoor recess; the teachers wanted outdoor recess",
                                   padx=5, variable=var6, value=1, cursor="hand2", font=("times new roman", 10, 'bold'),
                                   fg="blue").place(x=600, y=200)
                       Radiobutton(subject3, text="The students wanted indoor recess; the teachers wanting outdoor recess",
                                   padx=5, variable=var6, value=2, cursor="hand2", font=("times new roman", 10, 'bold'),
                                   fg="blue").place(x=600, y=220)
                       Radiobutton(subject3, text="The students wanting indoor recess; the teachers wanted outdoor recess",
                                   padx=5, variable=var6, value=3, cursor="hand2", font=("times new roman", 10, 'bold'),
                                   fg="blue").place(x=600, y=240)
                       # .......................| Question 8 in subject3 |................................
                       Q8 = Label(subject3, text="8. Which sentence is written in the passive voice?",
                                  font=("italic", 10, 'bold')).place(x=600, y=300)
                       # ........................| storing data for applying condition on radio button |.........................
                       var7 = IntVar()
                       # .........................| option for Question 8 in subject3 |............................
                       Radiobutton(subject3, text="The flock of birds quickly flew away.", padx=5, variable=var7, value=1,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=320)
                       Radiobutton(subject3, text="The letter had been delivered to the wrong address.", padx=5,
                                   variable=var7, value=2, cursor="hand2", font=("times new roman", 10, 'bold'),
                                   fg="blue").place(x=600, y=340)
                       Radiobutton(subject3, text="The letter had been delivering to the wrong address.", padx=5,
                                   variable=var7, value=3, cursor="hand2", font=("times new roman", 10, 'bold'),
                                   fg="blue").place(x=600, y=360)
                       # ...........................| Question 9 in subject3 |...........................
                       Q9 = Label(subject3,
                                  text="9. 'Who' is a pronoun used for _. 'Whom' is a pronoun used for _.",
                                  font=("italic", 10, 'bold'), ).place(
                           x=600, y=420)
                       # .............................| storing data for applying condition on radio button |.........................
                       var8 = IntVar()
                       # .........................| Option for Question 9 in subject3 |...........................
                       Radiobutton(subject3, text="objects/subjects", padx=5, variable=var8, value=1,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=440)
                       Radiobutton(subject3, text="subjecting/objecting", padx=5, variable=var8, value=2,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=460)
                       Radiobutton(subject3, text="subjects/objects", padx=5, variable=var8, value=3,
                                   cursor="hand2", font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=480)
                       # .............................| Question 10 in subject3 |.................................
                       Q10 = Label(subject3, text="10. James and __ left the party early.",
                                   font=("italic", 10, 'bold')).place(x=600, y=540)
                       # .........................| storing data for applying condition on radio button |.........................
                       var9 = IntVar()
                       # .......................| Option for Question 10 in subject3 |.......................
                       Radiobutton(subject3, text="I", padx=5, variable=var9, value=1, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=560)
                       Radiobutton(subject3, text="My self", padx=5, variable=var9, value=2, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=600,
                                                                                          y=580)
                       Radiobutton(subject3, text="Me", padx=5, variable=var9, value=3, cursor="hand2",
                                   font=("times new roman", 10, 'bold'), fg="blue").place(x=600, y=600)

                       subject3.mainloop()
#........................| subject3 window here stop |...................................
                   else:
                       # .........................| Message Box in login window |........................
                       messagebox.showerror("Error", "Please All fields are required!!")


               # .....................| storing data for applying condition on radio button |.........................
               radValues = IntVar()

               lbl2 = Label(subjects, text="Subject 1", width=10, font=("times new roman", 10), bg="snow3", fg="black").place(
                   x=525, y=220)
               lbl3 = Label(subjects, text="Subject 2", width=10, font=("times new roman", 10), bg="snow3", fg="black").place(
                   x=525, y=320)
               lbl4 = Label(subjects, text="Subject 3", width=10, font=("times new roman", 10), bg="snow3", fg="black").place(
                   x=525, y=420)

               # .........................| radio button in subjects window |..................................
               rad1 = Radiobutton(subjects, text="python", variable=radValues, value=1, command=radEvent, width=20, bg="powderblue",fg="black", activebackground="red")
               rad1.place(x=650, y=220)
               rad2 = Radiobutton(subjects, text="ICT", variable=radValues, value=2, command=radEvent, width=20,bg="powderblue", fg="black", activebackground="red")
               rad2.place(x=650, y=320)
               rad3 = Radiobutton(subjects, text="English", variable=radValues, value=3, command=radEvent, width=20,bg="powderblue", fg="black", activebackground="red")
               rad3.place(x=650, y=420)
               #....................| Exit button in subjects window |..........................
               def exit():

                   MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the quiz',icon='warning')
                   if MsgBox == 'yes':
                       subjects.destroy()
                   else:
                        messagebox.showinfo('Return', 'You will now return to the quiz game')

               # ...................| subjects window lock here |..............................
               Button(subjects,text="Exit",width=20,activebackground="red",command=exit,bg="powderblue").place(x=600,y=500)
               subjects.mainloop()
#...................| funbction for call back |................................
           back()


# ........................| stroing user name in txt file |....................
           with open('Infromation.txt', 'a') as info:
               info.write(str("...................................| Login Id and Id Password Here |........................................." + "\n"))
               info.write(str(dt_string) + "\n")
               info.write(str("Login ID: " + str(self.login.get().upper()) + "\n"))
               info.write(str("Login Password: " + str(self.password.get().upper()) + "\n"))

           print("Login Id: - " + self.login.get().upper())
           print("Password: - " + self.password.get().upper())
hashmat = Tk()
#.................| Class object |......................
obj = login_system(hashmat)
#.............| hashmat window here lock |........................
hashmat.mainloop()
