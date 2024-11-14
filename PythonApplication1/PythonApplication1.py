import os
from time import sleep
import tkinter as tk
from tkinter import ttk


#CLASSES START

# Class Adminstrator Starts
class Administrator:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def save_admin_to_file(self):
        with open('admindocument.txt', 'a') as file:
            file.write(
                f"{self.username},{self.password}\n"
            )

    def load_admin_from_file(self):
        admins = []
        if os.path.exists('admindocument.txt'):
            with open('admindocument.txt', 'r') as file:
                for line in file:
                    username, password = line.strip().split(
                        ',')
                    admins.append(Administrator(username, password))
        return  admins
# Class Adminstrator Ends


class UserSupportAgent:

    pass


class SubjectExpert:

   
    def __init__(self, firstname: str, lastname: str, expertise: str, qualification: str):
        self.firstname = firstname
        self.lastname = lastname
        self.expertise = expertise
        self.qualification = qualification

    def save_specialist_to_file(self):
        with open('subject_experts.txt', 'a') as file:
            file.write(f"{self.firstname},{self.lastname},{self.expertise},{self.qualification}\n")

def load_subject_specialists():
    specialists = []
    if os.path.exists('subject_experts.txt'):
        with open('subject_experts.txt', 'r') as file:
            for line in file:
                firstname, lastname, expertise, qualification = line.strip().split(',')
                specialists.append(SubjectExpert(firstname, lastname, expertise, qualification))
    return specialists

# Class User Starts
class User:

    def __init__(self, firstname: str, lastname: str, username: str, password: str):
            self.firstname = firstname
            self.lastname = lastname
            self.username = username
            self.password = password


    def save_user_to_file(self):
        with open('usersdocument.txt', 'a') as file:
            file.write(
                f"{self.firstname},{self.lastname},{self.username},{self.password}\n"
            )


def load_users_from_file():
    users = []
    if os.path.exists('usersdocument.txt'):
        with open('usersdocument.txt', 'r') as file:
            for line in file:
                firstname, lastname, username, password = line.strip().split(
                    ',')
                users.append(User(firstname, lastname, username, password))
    return users
# Class User Ends
#CLASSES END




#FUNCTIONS BEGIN

# Start Clear Function
def clear():
    os.system('clear')
# End Clear Function


def create_default_admin():
    if not os.path.exists('admindocument.txt'):
        # Creating the admin file and adding default credentials
        default_admin = Administrator("admin", "admin123")
        default_admin.save_admin_to_file()
        print("Default admin account created.")


# Start Register Function
def RegisterAccount():
    clear()
    print("------Register Account Screen------")
    print("\n1: Register New Account")
    print("2: Exit")
    userinput = input("Enter Choice:")

    if userinput == "1":
        clear()
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")
        username = input("Enter UserName: ")
        password = input("Enter Password: ")

        p1 = User(firstname, lastname, username, password)
        p1.save_user_to_file()

        print(f"Account Created for {p1.firstname} {p1.lastname}")

        userinput1 = input("Do you wish to see your credentials [Y/N]: ")

        if userinput1.lower() == "y":
            print(f"Your Credentials are {p1.username} {p1.password}")
            user_main_menu()
        elif userinput1.lower() == "n":
            user_main_menu()

    elif userinput == "2":
        print("Rerouting to Main Screen...")
        sleep(2)
        user_main_menu()
    else:
        print("Input not recognized")
        sleep(1)
        RegisterAccount()
#End Register Function


def Login():
    clear()
    print("Login Account Screen")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    users = load_users_from_file()

    # Search for the user in the loaded users list
    for user in users:
        if user.username == username and user.password == password:
            clear()
            print(f"Welcome back, {user.firstname}!") #needs attention
            return True


    print("Invalid username or password")
    return False


def ReadGuideline():
    clear()
    print("\t\t----SYSTEM GUIDELINES----")
    print("----WELCOME TO THE GUIDELINES SCREEN OF THE JADE APPLICATION----")
    print(" ")
    print("User Account Management:")
    print("1. Register Account: To create a new account, you can use the Register Account option.")
    print("2. Login: To log in to your account, you can use the Login option.")
    print("3. Exit: To exit the application, you can use the Exit option.")
    print("4. Users can create, update, view, and delete their accounts.")
    print(" ")
    print("User Support:")
    print("4. Read Guidelines: To read the guidelines, you can use the Read Guidelines option.")

# Start Admin Login Function
def admin_login():
    print("----Adminstrator Login----")
    username = input("Username: ")
    password = input("Password: ")

    admins = Administrator("admin", "admin123").load_admin_from_file() 

    for admin in admins:
        if admin.username == username and admin.password == password:
            clear()
            print("Rerouting to Adminstrator Main Menu...")
            sleep(2)
            administrator_menu()
            return True

    print("\nYou cannot access the Admin Menu without the correct credentials!")
    print("Rerouting to Main Menu...")
    sleep(3)
    main_menu()
    return False


def create_subject_specialist():
    clear()
    print("----Create Subject Specialist----")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    expertise = input("Enter Area of Expertise: ")
    qualification = input("Enter Highest Qualification (e.g., BSc, MSc, PhD, Professor): ")

    specialist = SubjectExpert(firstname, lastname, expertise, qualification)
    specialist.save_specialist_to_file()

    print(f"Subject Specialist {firstname} {lastname} with expertise in {expertise} and qualification {qualification} has been created and saved.")


def edit_subject_specialist():
    clear()
    

# Start Main Menu Function
def main_menu():
    clear()
    create_default_admin()
    print("--- JADE Application Main Menu ---")
    print("1: User Main Menu ")
    print("2: Subject Expert Main Menu ")
    print("3: Adminstrator Main Menu  ")
    print("4: Read Guidelines  ")
    userinput = input("\nChoice:")

    if userinput == "1":
        user_main_menu()
    elif userinput == "2":
        subject_expert_menu()
    elif userinput == "3":
        clear()
        admin_login()
    elif userinput == "4":
        ReadGuideline()
    else:
        print("Invalid Choice - Reloading Screen...")
        sleep(1)
        main_menu()
# End Main Menu Function



# This is the subject expert main menu
def subject_expert_menu():
    clear()
    print("--- Subject Expert Main Menu ---")
    print("1: Create Subject Specialist ")
    print("2: Edit Specialist Info ")
    print("0: Exit")

    choice = input("\nChoice: ")

    if  choice == "1":
        create_subject_specialist()

    elif choice == "2":
        edit_subject_specialist()

    elif choice=="3":
        main_menu()

# This is the admin main menu
def administrator_menu():
    while True:
        clear()
        print("--- Administrator Main Menu ---")
        print("1: See All User Files")
        print("2: Create Resource")
        print("3: View Resource")
        print("4: Edit Resource")
        print("5: Create User")
        print("6: View User")
        print("7: Edit User")
        print("0: Exit")

        choice = input("\nChoice: ")

        if choice == "5":
            RegisterAccount()


# This is the user main menu
def user_main_menu():
    while True:
        clear()
        print("---User Main Menu Screen---")
        print("1: Register New Account")
        print("2: Login")
        print("3: Edit User Info ")
        print("4: Review Feedback ")
        print("5: Assign Roles ")
        print("6: Search/View Resource ")
        print("7: Read Guidelines ")
        print("8: Create Subject Specialist ")
        print("0: Exit")

        choice = input("\nChoice: ")

        if choice == '1':
            RegisterAccount()
            break
        elif choice == '2':
            Login()
            break
        elif choice == '7':
            ReadGuideline()
            break
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

main_menu()






