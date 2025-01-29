class User:
    def __init__(self, id, firstname, lastname, username, password,status,role):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.status=status
        self.role=role

    def Update(self, new_firstname, new_lastname, new_username, new_password,new_status,new_role):
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.username = new_username
        self.password = new_password
        self.status=new_status
        self.role=new_role

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        if self.role==1:
            return "Admin"
        elif self.role==2:
            return "Default User"

    def get_status(self):
        if self.status==0:
            return "Deactive"
        elif self.status==1:
            return "Active"
        elif self.status==2:
            return "Pending"