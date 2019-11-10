import Tkinter
import os
import shutil

global subject_array
subject_array = os.listdir("Subjects")
global class_array
class_array = []
for files in subject_array:
    class_array += [files[0:files.find(".")]]
print class_array
class login(): #login window


    def __init__(self, master):
        self.new_user = open("newuser.txt","r")
        self.temp = self.new_user.read()
        if self.temp == "false": #if old user
            self.master = master
            self.master.title("Login!")
            self.username = Tkinter.Label(self.master, text="Username:")
            self.password = Tkinter.Label(self.master, text="Password:")
            self.username.grid(row=0, column=0)
            self.password.grid(row=1, column=0)
            self.u = Tkinter.Entry(self.master)
            self.p = Tkinter.Entry(self.master, show="*")
            self.u.grid(row=0, column=1)
            self.p.grid(row=1, column=1)
            self.login = Tkinter.Button(self.master, text = "Login!", command=self.login_button)
            self.login.grid(row=2, column=1)

        elif self.temp == "true": #if new user
            self.master = master
            self.master.geometry("250x50")
            self.master.title("Register!")
            self.register = Tkinter.Button(self.master, text = "Register!", command=self.register_button)
            self.register.pack()

    def login_button(self): #login button
        username_1 = self.u.get()
        password_1 = self.p.get()
        credents = open("Credentials.txt","r")
        arr = credents.read().split("\n")
        if username_1 == arr[0] and password_1 == arr[1]: #if credential match
            home_screen()
            self.master.destroy()
        else:
            self.username.grid(row=0, column=0, sticky="W")
            self.password.grid(row=1, column=0, sticky="W")
            self.u.grid(row=0, column=1, sticky="W")
            self.p.grid(row=1, column=1, sticky="W")
            self.login.grid(row=2, column=1)
            self.message = Tkinter.Label(self.master, text="Incorrect Username or Password.")
            self.message.grid(row=3, column=0, columnspan=3)

    def register_button(self): #if new user
        self.master.destroy()
        reg_window = Tkinter.Tk()

        Uregister = Tkinter.Entry(reg_window)
        Pregister = Tkinter.Entry(reg_window, show="*")
        Ulabel = Tkinter.Label(reg_window, text="Username:")
        Plabel = Tkinter.Label(reg_window, text="Password:")
        Ulabel.grid(row=0, column=0)
        Plabel.grid(row=1, column=0)
        Uregister.grid(row=0, column=1)
        Pregister.grid(row=1, column=1)

        def register_button_2(): #confirming credentials
            Registered_Username = Uregister.get()
            Registered_Password = Pregister.get()
            if Registered_Username != "" or Registered_Password != "":
                credentials = open("Credentials.txt", "w+")
                credentials.write(Registered_Username + "\n" + Registered_Password)
                open("newuser.txt","w").write("false")
                reg_window.destroy()

        r = Tkinter.Button(reg_window, text="Register!", command=register_button_2)
        r.grid(row=2, column=1)


class home_screen: #home screen
    def __init__(self):
        self.home_screen = Tkinter.Tk()
        self.home_screen.geometry("767x767")
        self.name = open("Credentials.txt","r").read().split("\n")[0]
        self.welcome_message = Tkinter.Label(self.home_screen, text="Welcome " + self.name + "!")
        self.welcome_message.config(font=("",44))
        self.welcome_message.place(x=170, y=191)
        self.settings_button = Tkinter.Button(self.home_screen, text="Settings", height=2, command=self.settings)
        self.settings_button.place(x=630, y=606)
        self.grades_button = Tkinter.Button(self.home_screen, text="Subjects", height=2, command=self.classes)
        self.grades_button.place(x=100, y=606)
        self.home_screen.protocol("WM_DELETE_WINDOW", self.on_closing_home_screen)

    def on_closing_home_screen(self):
        def terminate():
            quit_message.destroy()
            self.home_screen.destroy()

        def terminate_quit_message():
            quit_message.destroy()
            self.home_screen.deiconify()

        def on_closing_quit_message():
            quit_message.destroy()
            self.home_screen.deiconify()

        self.home_screen.withdraw()
        quit_message = Tkinter.Tk()

        quit_label = Tkinter.Label(quit_message, text="Are you sure you want to quit ReGrade?")
        yes_button = Tkinter.Button(quit_message, text="Yes", command=terminate)
        no_button = Tkinter.Button(quit_message, text="No", command=terminate_quit_message)
        quit_label.grid(row=0, column=0, columnspan=2)
        yes_button.grid(row=1, column=1, sticky="W")
        no_button.grid(row=1, column=0, sticky="E")
        quit_message.protocol("WM_DELETE_WINDOW", on_closing_quit_message)

    def settings(self): # opens settings screen
        self.home_screen.withdraw()
        settings_screen = Tkinter.Tk()

        def on_closing(): #if settings screen is closed
            settings_screen.destroy()
            self.home_screen.deiconify()

        def change_username(): #changing username
            settings_screen.destroy()
            change_username_window = Tkinter.Tk()
            new_username = Tkinter.Label(change_username_window, text="New Username:")
            confirm_username = Tkinter.Label(change_username_window, text="Confirm Username:")
            new_username.grid(row=0, column=0)
            confirm_username.grid(row=1, column=0)
            nu = Tkinter.Entry(change_username_window)
            cu = Tkinter.Entry(change_username_window)
            nu.grid(row=0, column=1)
            cu.grid(row=1, column=1)

            def confirm_button():
                new_username_1 = nu.get()
                confirm_username_1 = cu.get()

                if new_username_1 == confirm_username_1:
                    change_username_window.destroy()
                    arr1 = open("Credentials.txt","r").read().split("\n")
                    open("Credentials.txt","w").write(new_username_1 + "\n" + arr1[1])
                    success = Tkinter.Tk()

                    success_message = Tkinter.Label(success, text="Username changed successfully!")
                    success_message.pack()
                    def ok_button():
                        success.destroy()
                        self.settings()
                    ok = Tkinter.Button(success, text="OK", command=ok_button)
                    ok.pack()
                else:
                    new_username.grid(row=0, column=0, sticky="W")
                    confirm_username.grid(row=1, column=0, sticky="W")
                    nu.grid(row=0, column=1, sticky="W")
                    cu.grid(row=1, column=1, sticky="W")
                    confirm.grid(row=2, column=1)
                    message1 = Tkinter.Label(change_username_window, text="Usernames don't match.")
                    message1.grid(row=3, column=0, columnspan=3)

            confirm = Tkinter.Button(change_username_window, text = "Confirm", command=confirm_button)
            confirm.grid(row=2, column=1)

            def on_closing_change_username_window():
                change_username_window.destroy()
                self.settings()
            change_username_window.protocol("WM_DELETE_WINDOW", on_closing_change_username_window)

        def change_password():
            settings_screen.destroy()
            change_password_window = Tkinter.Tk()
            old_password = Tkinter.Label(change_password_window, text="Old password:")
            new_password = Tkinter.Label(change_password_window, text="New password:")
            confirm_password = Tkinter.Label(change_password_window, text="Confirm password:")
            old_password.grid(row=0, column=0)
            new_password.grid(row=1, column=0)
            confirm_password.grid(row=2, column=0)
            op = Tkinter.Entry(change_password_window, show="*")
            np = Tkinter.Entry(change_password_window, show="*")
            cp = Tkinter.Entry(change_password_window, show="*")
            op.grid(row=0, column=1)
            np.grid(row=1, column=1)
            cp.grid(row=2, column=1)

            def confirm1_button():
                old_password_1 = op.get()
                new_password_1 = np.get()
                confirm_password_1 = cp.get()
                arr2 = open("Credentials.txt","r").read().split("\n")
                if old_password_1 == arr2[1]:
                    if new_password_1 == confirm_password_1:
                        change_password_window.destroy()
                        open("Credentials.txt","w").write(arr2[0] + "\n" + new_password_1)
                        success1 = Tkinter.Tk()
                        success1_message = Tkinter.Label(success1, text="Password changed successfully!")
                        success1_message.pack()
                        def ok_button():
                            success1.destroy()
                            self.settings()
                        ok = Tkinter.Button(success1, text="OK", command=ok_button)
                        ok.pack()
                    else:
                        old_password.grid(row=0, column=0, sticky="W")
                        new_password.grid(row=1, column=0, sticky="W")
                        confirm_password.grid(row=2, column=0, sticky="W")
                        op.grid(row=0, column=1, sticky="W")
                        np.grid(row=1, column=1, sticky="W")
                        cp.grid(row=2, column=1, sticky="W")
                        confirm1.grid(row=3, column=1)
                        message2 = Tkinter.Label(change_password_window, text="Passwords don't match.")
                        message2.grid(row=4, column=0, columnspan=3)
                else:
                    old_password.grid(row=0, column=0, sticky="W")
                    new_password.grid(row=1, column=0, sticky="W")
                    confirm_password.grid(row=2, column=0, sticky="W")
                    op.grid(row=0, column=1, sticky="W")
                    np.grid(row=1, column=1, sticky="W")
                    cp.grid(row=2, column=1, sticky="W")
                    confirm1.grid(row=3, column=1)
                    message3 = Tkinter.Label(change_password_window, text="Check old password.")
                    message3.grid(row=4, column=0, columnspan=3)

            confirm1 = Tkinter.Button(change_password_window, text = "Confirm", command=confirm1_button)
            confirm1.grid(row=3, column=1)

            def on_closing_change_password_window():
                change_password_window.destroy()
                self.settings()
            change_password_window.protocol("WM_DELETE_WINDOW", on_closing_change_password_window)

        settings_screen.protocol("WM_DELETE_WINDOW", on_closing)
        settings_screen.geometry("100x60")
        change_username_button = Tkinter.Button(settings_screen, text="Change username", command=change_username)
        change_username_button.pack()
        change_password_button = Tkinter.Button(settings_screen, text="Change password", command=change_password)
        change_password_button.pack()

    def classes(self):
        self.home_screen.withdraw()
        pre_grades = Tkinter.Tk()

        def add_new_class():
            pre_grades.withdraw()
            add_new_class_window = Tkinter.Tk()
            class_name = Tkinter.Label(add_new_class_window, text="Class name: ")
            class_name.grid(row=0, column=0)
            enter_class_name = Tkinter.Entry(add_new_class_window)
            enter_class_name.grid(row=0, column=1)

            def confirm_new_class():
                global class_array
                if enter_class_name.get != "" and enter_class_name.get() not in class_array:
                    file_name = enter_class_name.get() + ".txt"
                    open(file_name, "w+")
                    shutil.move(file_name, "Subjects")
                    class_array += [enter_class_name.get()]
                    add_new_class_window.destroy()
                    success_message2 = Tkinter.Tk()
                    message4 = Tkinter.Label(success_message2, text="Class added sucessfully!")
                    message4.pack()

                    def on_closing_success_message2():
                        success_message2.destroy()
                        pre_grades.deiconify()

                    success_message2.protocol("WM_DELETE_WINDOW", on_closing_success_message2)

                else:
                    please_enter_name = Tkinter.Label(add_new_class_window, text="Please enter a valid class name.")
                    please_enter_name.grid(row=2, column=0, columnspan=2)

            def on_closing_adding_new_class():
                add_new_class_window.destroy()
                pre_grades.deiconify()

            add_new_class_window.protocol("WM_DELETE_WINDOW", on_closing_adding_new_class)
            confirm_new_class_button = Tkinter.Button(add_new_class_window, text="Confirm", command=confirm_new_class)
            confirm_new_class_button.grid(row=1, column=0, columnspan=2)


        def open_classes():
            pre_grades.withdraw()
            grades_window = Tkinter.Tk()
            functions={}

            for s in class_array:
                functions[s] = open("Subjects/" + s + ".txt", "r").read()

            subject_list = Tkinter.Listbox(grades_window)
            subject_list.pack()

            for i in class_array:
                subject_list.insert(0,i)
            
            def opening_data():
                grades_window.withdraw()
                data_window = Tkinter.Tk()
                arr=[]
                for i in functions:
                    arr.append(i)
                data = functions.get(arr[subject_list.curselection()[0]])
                Tkinter.Label(data_window, text=data).pack()

                def on_closing_opening_data():
                    data_window.destroy()
                    grades_window.deiconify()
                
                data_window.protocol("WM_DELETE_WINDOW",on_closing_opening_data)

            def on_closing_open_classes():
                grades_window.destroy()
                pre_grades.deiconify()


            grades_window.protocol("WM_DELETE_WINDOW",on_closing_open_classes)
            choose_button = Tkinter.Button(grades_window, text="Choose!", command=opening_data)
            choose_button.pack()

        add_new_class_button = Tkinter.Button(pre_grades, text="Add New class", command=add_new_class)
        add_new_class_button.pack()
        classes = Tkinter.Button(pre_grades, text="Classes", command=open_classes)
        classes.pack()

        def on_closing_classes():
            pre_grades.destroy()
            self.home_screen.deiconify()

        pre_grades.protocol("WM_DELETE_WINDOW", on_closing_classes)

if __name__ == "__main__":
    main = Tkinter.Tk()
    start = login(main)
    main.mainloop()
