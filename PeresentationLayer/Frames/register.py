from tkinter import messagebox
from ttkbootstrap import Frame, Label, Entry, Button, BooleanVar, Checkbutton, DARK,SUCCESS,PRIMARY,OUTLINE,INFO
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
class RegisterFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)
        self.main_view=main_view
        self.user_business_logic = UserBusinessLogic()
        self.grid_columnconfigure(1,weight=1)
        self.header=Label(self,text="Register Page",bootstyle=INFO,font=("Helvetica",12,"bold"))
        self.header.grid(row=0,column=1,padx=10,pady=10)
        self.firstname_lable=Label(self,text="First Name :",font=("Helvetica",9,"bold"))
        self.firstname_lable.grid(row=1,column=0,padx=10,pady=10,sticky="e")
        self.firstname_entry=Entry(self,bootstyle=PRIMARY)
        self.firstname_entry.grid(row=1,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.lastname_lable=Label(self,text="Last Name :",font=("Helvetica",9,"bold"))
        self.lastname_lable.grid(row=2,column=0,padx=(0,10),pady=(0,10),sticky="e")
        self.lastname_entry=Entry(self,bootstyle=PRIMARY)
        self.lastname_entry.grid(row=2,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.username_lable=Label(self,text="User Name :",font=("Helvetica",9,"bold"))
        self.username_lable.grid(row=3,column=0,padx=(0,10),pady=(0,10),sticky="e")
        self.username_entry=Entry(self,bootstyle=PRIMARY)
        self.username_entry.grid(row=3,column=1,padx=(0,10),pady=(0,10),sticky="ew")


        self.password_lable=Label(self,text="Password :",font=("Helvetica",9,"bold"))
        self.password_lable.grid(row=4,column=0,padx=(0,10),pady=(0,10),sticky="e")
        self.password_entry=Entry(self,bootstyle=PRIMARY)
        self.password_entry.grid(row=4,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.register_button=Button(self,text="Save Data",command=self.save_register_data,bootstyle=SUCCESS)
        self.register_button.grid(row=5,column=1,padx=(0,10),pady=(0,10),sticky="w")

        self.back_button = Button(self, text="Back", command=self.go_to_login,bootstyle=INFO)
        self.back_button.grid(row=6, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

    def save_register_data(self):
        first_name=self.firstname_entry.get()
        last_name=self.lastname_entry.get()
        username=self.username_entry.get()
        password=self.password_entry.get()
        response=self.user_business_logic.Register(first_name,last_name,username,password)
        if response.Success:
            messagebox.showinfo(title="Info",message=response.Message)
        else:
            messagebox.showerror(title="Error", message=response.Message)
            self.username_entry.delete(0,"end")
            self.password_entry.delete(0,"end")
        self.main_view.switch_frame("Login")

    def go_to_login(self):
        self.main_view.switch_frame("Login")