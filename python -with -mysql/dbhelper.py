import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', 
                        port='3306', 
                        user='root', 
                        password='root', 
                        databse='pythontest')
        query = 'create table if not exits user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    #Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userId, userName, phone)values({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user save to db")

    #Fetch All
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User name : ", row[1])
            print("User Phone : ", row[2])
            print()
            print()

    #Delete User
    def delete_user(self, userId):
        query = "delete from user where userId = {}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #Update
    def update_user(self, userId, newName, newPhone):
        query = "update user set userName = '{}', phone = '{}', where userId = {}".format(newName, newPhone, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")


# #main coding
# helper = DBHelper()
# # helper.insert_user(123, "Rahat", "232425")
# # helper.insert_user(124, "Shakil", "234525")
# # helper.insert_user(125, "Ashik", "332425")
# # helper.insert_user(126, "Badhon", "567425")
# # helper.fetch_all()
# # helper.delete_user(124)
# # helper.fetch_all()
# helper.update_user(127, "Robel", "132459")
# helper.fetch_all(0)

