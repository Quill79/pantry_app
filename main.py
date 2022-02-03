import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port="3306",
    database="pantry"
)

mycursor = mydb.cursor()


def register():
    username = input("Create Username:")
    # password = input("Create Password:")
    # password2 = input("Confirm Password:")

    # Accessing user table and checking to see if username in use
    users = mycursor.fetchall()
    print(users)


    # This is password checker function
    # if password != password2:
    #     print("Passwords do not match.")
    #     register()
    # elif len(password) <= 7:
    #     print("Password too short.")
    # else:
    #     pass


register()


def access():
    db = open("database.txt", "r")
    username = input("Enter Username:")
    password = input("Enter Password:")
    if not len(username or password) <= 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Success\n")
                        print("Hi,", username)
                    else:
                        print("Username/Password Incorrect.")
                        access()
                except:
                    print("Incorrect Password/Username.")
                    access()
            else:
                print("Username doesn't exist.")
                access()
        except:
            print("Login Error")
            access()
    else:
        print("Please enter a value.")
        access()


def home(option=None):
    typo = input("Login | Signup:")
    option = typo.lower()
    if option == "login":
        access()
    elif option == "signup":
        register()
    else:
        print("Please enter an option.")
        home()


#home()


def pantry_item_menu():
    print("**********Pantry Menu**********")
    print("1. List Ingredients")
    print("2. Add Ingredient")
    print("3. Remove Ingredient")
    print("4. Back to Main")
    choice = int(input("Make a selection: "))
    return choice


def pantry_item(p_item):
    print("What would you like to do in the {item} pantry.".format(item=p_item))
    choice = 0
    while choice != 4:
        choice = pantry_item_menu()
        if choice == 1:
            with open("meat.txt".format(p_item)) as item:
                for line in item:
                    print(line)
        elif choice == 2:
            new = input("Enter name of ingredient you would like to add: ")
            choice = input("You entered" + new + ". Is this correct (Y or N)?")
            checked = choice.upper()
            if checked == "Y":
                with open("meat.txt".format(p_item), "w") as item:
                    item.write(new + " Y")
            elif checked == "N":
                print("No")
            else:
                print("Invalid Input")


# //// Defining Main Functions ////

def check_pantry():
    category = 6
    while category != 0:
        print("""
        1. Dairy
        2. Meat
        3. Vegetables
        4. Fruits
        5. Snacks
        0. Exit
        """)
        category = int(input("What category would you like to check?"))
        if category == 1:
            print(pantry_item("dairy"))
        elif category == 2:
            pantry_item("meat")
        elif category == 3:
            pantry_item("vegetables")
        elif category == 4:
            pantry_item("fruits")
        elif category == 5:
            pantry_item("snacks")
        elif category == 0:
            return
        else:
            print("Invalid Entry!")


def plan_meals():
    print("meals")


def shopping_list():
    print("shopping_list")


def plan_meals():
    print("plan em")


def make_check():
    print("can you make it?")


# //// Main Menu Functions ////
def menu():
    print("1. Check Pantry")
    print("2. Plan Meals")
    print("3. Generate Shopping List")
    print("4. Plan Meals")
    print("5. What can I make?")
    print("0. Exit")


#menu()
# ch = int(input("Make a choice: "))
#
# while ch != 0:
#     if ch == 1:
#         check_pantry()
#     elif ch == 2:
#         plan_meals()
#     elif ch == 3:
#         shopping_list()
#     elif ch == 4:
#         plan_meals()
#     elif ch == 5:
#         make_check()
#     else:
#         print("Invalid Input")
#
#     menu()
#     ch = int(input("Make a choice: "))
