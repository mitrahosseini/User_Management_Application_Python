
from ttkbootstrap import Frame, Label, Button,\
    DARK,SUCCESS,PRIMARY,INFO,Style
class HomeFrame(Frame):
    def __init__(self,window,main_view):
        super(). __init__(window)
        self.main_view=main_view
        self.grid_columnconfigure(0,weight=1)
        self.header=Label(self,bootstyle=INFO,font=("Helvetica",12,"bold"))
        self.header.grid(row=0,column=0,pady=10,padx=10)
        self.style = Style()
        self.style.configure("TButton",font=("Helvetica",10,"bold"))
        self.logout_button=Button(self,text="Logout",command=self.logout,bootstyle=INFO)
        self.logout_button.grid(row=1,column=0,pady=20,padx=20,sticky="ew")
        self.user_management_button=Button(self,text="User Management",command=self.go_to_user_management,bootstyle=SUCCESS)
        self.current_user=None
    def set_current_user(self,user):
        self.current_user=user
        welcome_message=f"welcome {user.get_fullname()} ({user.get_role()})"
        self.header.config(text=welcome_message)
        if user.role==1:
            self.user_management_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

    def logout(self):
      self.main_view.switch_frame("Login")
    def go_to_user_management(self):
       usermanagement_frame= self.main_view.switch_frame("user management")
       usermanagement_frame.set_current_user(self.current_user)


