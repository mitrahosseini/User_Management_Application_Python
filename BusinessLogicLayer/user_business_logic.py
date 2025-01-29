import hashlib
from Common.Model.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
import sqlite3
from Common.Entities.role import Role
from Common.Entities.user import User


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def hashing(self, password):
        hash_password = hashlib.md5(password.encode()).hexdigest()
        return hash_password

    def Login(self, username, password):

        if len(username) < 3 or len(password) < 6:
            return Response(False, None, "Invalid Username or Password.")
        hash_password = self.hashing(password)

        user = self.user_data_access.get_user(username, hash_password)
        if user:
            match user.status:
                case 0:
                    return Response(False, None, "your account is Deactived")
                case 1:
                    return Response(True, user, None)
                case 2:
                    return Response(False, None, "your account is pending")
        else:
            return Response(False, None, "Invalid Username or Password(not found).")

    def Register(self, first_name, last_name, username, password):
        if len(first_name) < 3:
            return Response(False, None, "Error:Invalid FirstName.")
        if len(last_name) < 3:
            return Response(False, None, "Error:Invalid LastName.")
        if len(username) < 3:
            return Response(False, None, "Error:Invalid UserName.")
        if len(password) < 6:
            return Response(False, None, "Error:Invalid Password.")
        if not first_name.isalpha():
            return Response(False, None, "Error: Invalid FirstName.")
        if not last_name.isalpha():
            return Response(False, None, "Error: Invalid LastName.")
        if not username.isalpha():
            return Response(False, None, "Error: Invalid UserName.")
        hash_password = self.hashing(password)
        try:
            self.user_data_access.insert_user(first_name, last_name, username, hash_password, 2, 2)
        except sqlite3.IntegrityError as error:
            # if username in error.args[0]:
            return Response(False, None, "Username exist.")
        else:
            return Response(True, None, "Register successfully.")

        # user = self.user_data_access.search_user(username)
        # if user:
        #     return Response(False, user, "Error: Username already exist.")
        # else:
        #     self.user_data_access.insert_user(first_name,last_name,username,password,1,1)
        #     return Response(True,None,None)

    # def get_user_management_list(self, current_user):
    #     if current_user.role == 1:
    #         user_list = self.user_data_access.get_user_list()
    #         return Response(True, user_list, None)
    #     else:
    #         return Response(False, None, "Access Denied")

    def active_user(self, id_list):
        for id in id_list:
            self.user_data_access.update_status(id, 1)

    def pending_user(self, id_list):
        for id in id_list:
            self.user_data_access.update_status(id, 2)

    def deactive_user(self, id_list):
        for id in id_list:
            self.user_data_access.update_status(id, 0)

    def role_list(self):
        role_title_list = []
        role_list = self.user_data_access.get_role_list()
        for role in role_list:
            role_title_list.append(role.title)
        return role_title_list

    def change_role(self, user_id, new_role_id):
        self.user_data_access.update_role(user_id, new_role_id)

    def role_id(self, role_title):
        role_list = self.user_data_access.get_role_list()
        for role in role_list:
            if role.title == role_title:
                role_id = int(role.id)
        return role_id

    def search(self, term):
        user_list = self.user_data_access.search_list(term)
        return user_list


    def get_paginated_users(self, current_user, page_number, page_size):
        if current_user.role == 1:
            offset = (page_number - 1) * page_size
            user_list = self.user_data_access.get_paginated_users(current_user.id,page_size, offset)
            return Response(True, user_list, None)
        else:
            return Response(False, None, "Access Denied")

    def get_total_pages(self, page_size):
        total_users = self.user_data_access.get_total_user_count()
        total_pages = (total_users + page_size - 1) // page_size
        return total_pages
