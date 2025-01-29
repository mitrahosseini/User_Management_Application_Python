# from dataclasses import replace
# from tkinter import Tk, Button
# from tkinter import ttk
# from tkinter.ttk import Combobox
from ttkbootstrap import Window, Button,Combobox, SUCCESS,INFO,Style ,Label
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
# from PeresentationLayer.Frames.user_management import UserManagement
# from ttkbootstrap import Frame, Label, Entry, Treeview, BooleanVar, Checkbutton, \
#     DARK, SUCCESS, PRIMARY, OUTLINE, DANGER, SECONDARY, INFO, Style, font, TOGGLE, TOOLBUTTON, WARNING, DISABLED, \
#     Bootstyle

class ChangeRole(Window):
    def __init__(self,title,initialize_size,user_id,usermanagement):
        super().__init__()
        self.user_business_logic=UserBusinessLogic()
        self.grid_columnconfigure(0,weight=1)
        self.title(title)
        self.geometry(initialize_size)
        # self.style=Style()
        # self.style.configure('Custom.TCombobox',padding=5,width=20,font=("Helvetica",10,"bold"))
        # self.combobox= self.ttk.Combobox(self,values=(self.user_business_logic.role_list()))
        self.header =Label(self, text="Change Role Page",font=("Helvetica",12,"bold"))
        self.header.grid(row=0, column=0, pady=10)
        self.combobox=Combobox(self,values=(self.user_business_logic.role_list()),bootstyle=INFO)
        self.combobox.grid(row=1,column=0,padx=10,pady=10,sticky="ew")
        self.save_button=Button(self,text="Save",command=self.save_change_role,bootstyle=SUCCESS)
        self.save_button.grid(row=2,column=0,padx=10,pady=10,sticky="ew")
        self.user_id=user_id
        self.user_management=usermanagement
        self.mainloop()
    #
    # def set_current_user_id(self, user_id):
    #         self.user_id =  user_id
    def save_change_role(self):
        if self.combobox.winfo_exists():
           new_role_title=self.combobox.get()
           if new_role_title:
             new_role_id= self.user_business_logic.role_id(new_role_title)
             self.user_business_logic.change_role(self.user_id, new_role_id)
             self.user_management.load_current_page()
           self.destroy()


