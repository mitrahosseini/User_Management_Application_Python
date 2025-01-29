
from tkinter import messagebox
from ttkbootstrap import Frame, Label, Entry, Button, Treeview, BooleanVar, Checkbutton, \
    DARK, SUCCESS, PRIMARY, OUTLINE, DANGER, SECONDARY, INFO, Style, font, TOGGLE, TOOLBUTTON, WARNING, DISABLED, \
    Bootstyle

from tkinter.constants import CENTER
# from tkinter.ttk import Treeview
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from PeresentationLayer.change_role import ChangeRole
class UserManagement(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)
        self.user_business_logic=UserBusinessLogic()
        self.main_view=main_view
        self.style=Style()
        self.style.configure("TButton",font=("Helvetica",10,"bold"))
        self.style.configure("Treeview.Heading",font=("Helvetica",12,"bold"))
        self.style.configure("Treeview", font=("Helvetica", 10))
        self.btn_font=font.Font(family="Arial",size=12,weight="bold")
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.header=Label(self,text="User Management Frame",bootstyle=INFO,font=("Helvetica",12,"bold"))
        self.header.grid(row=0,column=0,columnspan=4,pady=10)
        self.search_entry=Entry(self,bootstyle=SUCCESS)
        self.search_entry.grid(row=1,column=0,columnspan=3,pady=(0,10),padx=20,sticky="ew")
        self.search_button=Button(self,text="Search",command=self.search,bootstyle=SUCCESS)
        self.search_button.grid(row=1,column=3,pady=(0,10),padx=(0,10))
        self.active_button=Button(self,text="Active",command=self.active_user,bootstyle=SUCCESS)
        self.active_button.grid(row=2,column=0,pady=(0,10),padx=10)
        self.active_button.config(state="disabled")
        self.pending_button=Button(self,text="Pending",command=self.pending_user,bootstyle=WARNING)
        self.pending_button.grid(row=2,column=1,pady=(0,10),padx=10)
        self.pending_button.config(state="disabled")
        self.deactive_button=Button(self,text="Deactive",command=self.deactive_user,bootstyle=DANGER)
        self.deactive_button.grid(row=2,column=2,pady=(0,10),padx=10)
        self.deactive_button.config(state="disabled")
        self.change_role_button = Button(self, text="Change Role",command=self.go_to_change_role_form,bootstyle=PRIMARY)
        self.change_role_button.grid(row=2, column=3, pady=(0, 10), padx=10)
        self.change_role_button.config(state="disabled")
        self.user_treeview=Treeview(self,columns=("firstname","lastname","username","status","role"))
        self.user_treeview.grid(row=3,column=0,columnspan=4,pady=(0,10),padx=20,sticky="nsew")
        self.user_treeview.configure(bootstyle=PRIMARY)
        self.user_treeview.heading("#0",text="No")
        self.user_treeview.heading("#1",text="First Name")
        self.user_treeview.heading("#2",text="Last Name")
        self.user_treeview.heading("#3",text="User Name")
        self.user_treeview.heading("#4",text="Status")
        self.user_treeview.heading("#5",text="Role")
        self.user_treeview.column("#0",width=70,anchor=CENTER)
        self.user_treeview.column("#1",anchor=CENTER)
        self.user_treeview.column("#2",anchor=CENTER)
        self.user_treeview.column("#3",anchor=CENTER)
        self.user_treeview.column("#4",anchor=CENTER)
        self.user_treeview.column("#5",anchor=CENTER)
        self.current_user=None
        self.row_list=[]
        self.page_number=1
        self.page_size=10
        self.total_page=1
        self.previuse_page_button = Button(self,text="PreviusePage",command=self.prev_page)
        self.previuse_page_button.grid(row=4,column=2,pady=(0,10),padx=10,sticky="e")
        self.page_lable=Label(self,text=self.page_number,font=("Helvetica",12,"bold"))
        self.page_lable.grid(row=4,column=1,pady=(0,10),padx=10)
        self.next_page_button = Button(self,text="NextPage",command=self.next_page,style="TButton")
        self.next_page_button.grid(row=4,column=0,pady=(0,10),padx=20,sticky="w")
        self.home_page_button = Button(self,text="HomePage",command=self.go_to_home_page,bootstyle=INFO)
        self.home_page_button.grid(row=4,column=3,pady=(0,10),padx=20,sticky="e")
        self.user_treeview.bind("<<TreeviewSelect>>",self.manage_button)
        # self.user_treeview.tag_configure("First Name",background="green",foreground="white")
        # self.user_treeview.tag_configure("Default User", background="blue", foreground="white",padding=(5,5))
    def go_to_home_page(self):
       self.main_view.switch_frame("home")

    def set_current_user(self,user):
        self.current_user=user
        self.page_number=1
        self.load_current_page()
        # response=self.user_business_logic.get_user_management_list(user)
        # if response.Success:
        #    # self.load_current_page()
        #    user_list=response.Data
        #    self.load_data_treeview(user_list)
        # else:
        #     messagebox.showerror(title="Error",message=response.Message)
        #     self.main_view.switch_frame("Login")

    def load_data_treeview(self,user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)
        self.row_list.clear()
        row_number=1
        for user in user_list:
            row=self.user_treeview.insert("","end",iid=user.id,text=str(row_number),values=(user.first_name,user.last_name,user.username,user.get_status(),user.get_role()))
            self.row_list.append(row)
            row_number +=1

    def active_user(self):
       id_list= self.user_treeview.selection()
       self.user_business_logic.active_user(id_list)
       response=self.user_business_logic.get_paginated_users(self.current_user, self.page_number, self.page_size)
       if response.Success:
           user_list=response.Data
           self.load_data_treeview(user_list)
       else:
           messagebox.showerror(title="Error",message=response.Message)
           self.main_view.switch_frame("Login")

    def pending_user(self):
        id_list=self.user_treeview.selection()
        self.user_business_logic.pending_user(id_list)
        response=self.user_business_logic.get_paginated_users(self.current_user, self.page_number, self.page_size)
        if response.Success:
            user_list = response.Data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error", message=response.Message)
            self.main_view.switch_frame("Login")


    def deactive_user(self):
        id_list=self.user_treeview.selection()
        self.user_business_logic.deactive_user(id_list)
        response=self.user_business_logic.get_paginated_users(self.current_user, self.page_number, self.page_size)
        if response.Success:
            user_list=response.Data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error",message=response.Message)
            self.main_view.switch_frame("Login")

    def go_to_change_role_form(self):
        user_id = int(self.user_treeview.selection()[0])
        change_role_form=self.main_view.change_role_form(user_id,self)
        change_role_form.save_change_role()
        #
        # response = self.user_business_logic.get_paginated_users(self.current_user,self.page_number,self.page_size)
        # if response.Success:
        #     user_list = response.Data
        #     self.load_data_treeview(user_list)
        # else:
        #     messagebox.showerror(title="Error", message=response.Message)
        #     self.main_view.switch_frame("Login")
    def search(self):
        term=self.search_entry.get()
        if len(term)>0:
            user_list= self.user_business_logic.search(term)
            self.load_data_treeview(user_list)
        else:
            response = self.user_business_logic.get_paginated_users(self.current_user, self.page_number, self.page_size)
            if response.Success:
                user_list = response.Data
                self.load_data_treeview(user_list)
            else:
                messagebox.showerror(title="Error", message=response.Message)
                self.main_view.switch_frame("Login")


    def load_current_page(self):
        response=self.user_business_logic.get_paginated_users(self.current_user,self.page_number,self.page_size)
        if response.Success:
            user_list=response.Data
            total_page=self.user_business_logic.get_total_pages(self.page_size)
            self.load_data_treeview(user_list)
            self.update_pagination_button(total_page)
        else:
            messagebox.showerror(title="Error", message=response.Message)
            self.main_view.switch_frame("Login")


    def next_page(self):
        self.page_number+=1
        self.page_lable.config(text=self.page_number)
        self.load_current_page()

    def prev_page(self):
        if self.page_number>1:
            self.page_number-=1
            self.page_lable.config(text=self.page_number)
            self.load_current_page()
    def update_pagination_button(self,total_pages):
        if self.page_number==1:
            self.previuse_page_button.config(state="disabled")
        else:
            self.previuse_page_button.config(state="normal")
        if self.page_number>=total_pages:
            self.next_page_button.config(state="disabled")
        else:
            self.next_page_button.config(state="normal")

    def manage_button(self,event):
        select_count=len(self.user_treeview.selection())
        if select_count==1:
            self.active_button.config(state="normal")
            self.pending_button.config(state="normal")
            self.deactive_button.config(state="normal")
            self.change_role_button.config(state="normal")
        elif select_count>1:
            self.active_button.config(state="normal")
            self.pending_button.config(state="normal")
            self.deactive_button.config(state="normal")
            self.change_role_button.config(state="disabled")
        else:
            self.active_button.config(state="disabled")
            self.pending_button.config(state="disabled")
            self.deactive_button.config(state="disabled")
            self.change_role_button.config(state="disabled")



