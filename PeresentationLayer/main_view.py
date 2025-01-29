from PeresentationLayer.Frames.user_management import UserManagement
from PeresentationLayer.window import Window
from PeresentationLayer.Frames.Login import LoginFrame
from PeresentationLayer.window import Window
from PeresentationLayer.Frames.home import HomeFrame
from PeresentationLayer.Frames.register import RegisterFrame
from PeresentationLayer.change_role import ChangeRole
from ttkbootstrap import Frame, INFO, DARK, Bootstyle, PRIMARY,LIGHT,SECONDARY


class MainView:
    def __init__(self):
        self.frames={}
        self.window=Window("User Management Application","500x300")
        # self.window.configure(themename="yeti")
        self.add_frame("user management",UserManagement(self.window,self))
        self.add_frame("register", RegisterFrame(self.window, self))
        self.add_frame("home", HomeFrame(self.window,self))
        self.add_frame("Login",LoginFrame(self.window,self))
        self.window.mainloop()

    def add_frame(self,name,frame):
        self.frames[name]=frame
        self.frames[name].grid(row=0,column=0,sticky="nsew")
        self.frames[name].configure(bootstyle=LIGHT)
        # self.frames[name].configure(iconphoto="1.png")

    def switch_frame(self,frame_name):
        frame=self.frames[frame_name]
        frame.tkraise()
        return frame

    def change_role_form(self,user_id,usermanagement):
        return  ChangeRole("Change Role Page","500x300",user_id,usermanagement)

