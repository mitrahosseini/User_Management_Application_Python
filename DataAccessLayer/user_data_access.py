import sqlite3
from . import sqlite_database_name
from Common.Entities.user import User
from Common.Model.response import Response
from  Common.Entities.role import Role
class UserDataAccess:
    def get_user(self, username, hash_password):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role
            FROM User
            Where username='{username}'
            AND password ='{hash_password}'""")
            data = cursor.fetchone()
            if data:
                return User(data[0], data[1], data[2], data[3], None,data[4],data[5])
    # def search_user(self, username):
    #     with sqlite3.connect(sqlite_database_name) as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(f"""
    #         SELECT id,
    #                first_name,
    #                last_name,
    #                username,
    #                status,
    #                role
    #         FROM User
    #         Where username='{username}'""")
    #         data = cursor.fetchone()
    #         if data:
    #             return User(data[0], data[1], data[2], data[3], None,data[4],data[5])


    def insert_user(self, first_name,last_name,username,hash_password,status,role):
      with sqlite3.connect(sqlite_database_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
INSERT INTO User (
          first_name,
          last_name,
          username,
          password,
          status,
          role
          )
VALUES (
         '{first_name}',
         '{last_name}',
         '{username}',
         '{hash_password}',
          {status},
          {role}
        );""")
        connection.commit()

    # def get_user_list(self):
    #     user_list=[]
    #     with sqlite3.connect(sqlite_database_name) as connection:
    #         cursor=connection.cursor()
    #         cursor.execute(f"""
    #         SELECT id,
    #                first_name,
    #                last_name,
    #                username,
    #                status,
    #                role
    #           FROM User
    #           Where role != 1 """)
    #         data_list=cursor.fetchall()
    #         for data in data_list:
    #             user=User(data[0],data[1],data[2],data[3],None,data[4],data[5])
    #             user_list.append(user)
    #         return user_list

    def update_status(self,user_id,new_status):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor=connection.cursor()
            cursor.execute(f"""
            UPDATE User
               SET status = {new_status}
             WHERE id ={user_id};""")
            connection.commit()

    def update_role(self,user_id,new_role_id):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor=connection.cursor()
            cursor.execute(f"""
              UPDATE User
               SET 
                   role = {new_role_id}
             WHERE id ={user_id};""")

            connection.commit()
    def get_role_list(self):
        role_list = []
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   title
            FROM   Role""")
            data_list = cursor.fetchall()

            for data in data_list:
                role = Role(data[0], data[1])
                role_list.append(role)

        return role_list


    def search_list(self,term):
        user_list=[]
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor=connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role
              FROM User
              Where first_name LIKE '%{term}%'
                OR  last_name  LIKE  '%{term}%'
                OR  username   LIKE  '%{term}%'""")
            data_list=cursor.fetchall()
            for data in data_list:
                user=User(data[0],data[1],data[2],data[3],None,data[4],data[5])
                user_list.append(user)
            return user_list

    def get_total_user_count(self):
        try:
            with sqlite3.connect(sqlite_database_name) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                   SELECT COUNT(*)
                     FROM User""")
                total_users = cursor.fetchone()[0]
                return  total_users
        except sqlite3.Error as error:
            return  0


    def   get_paginated_users(self,current_user_id,limit,offset):
        user_list=[]
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role
              FROM User
              WHERE id != {current_user_id}
              LIMIT {limit} 
              OFFSET {offset}""")
            data_list = cursor.fetchall()
            for data in data_list:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5])
                user_list.append(user)

        return user_list

