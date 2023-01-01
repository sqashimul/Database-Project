from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("*** Welcome to Database Project ***")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user ")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit Program")
        print()
        try:
            choice = int(input())
            if(choice == 1):
                #insert user
                uid = int(input("Enter user id: "))
                username = input("Enter user name: ")
                userphone = input("Enter user phone: ")
                db.insert_user(uid, username, userphone)
                
            elif choice == 2:
                #display user
                db.fetch_all()
                pass
            elif choice == 3:
                #delete user
                userid = int(input("Enter user id to which you want to delete "))
                db.delete_user(userid)
                pass
            elif choice == 4:
                #update user
                uid = int(input("Enter id of user: "))
                username = input("New name: ")
                userphone = input("New phone: ")
                db.update_user(uid, username, userphone)

            elif choice == 5:
                break
            else:
                print("Invalid Input ! Try Again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try Again")

if __name__ == "__main__":
    main()




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


