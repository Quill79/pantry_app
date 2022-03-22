import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port="3306",
    database="pantry"
)

my_cursor = mydb.cursor(buffered=True)

# Accessing user table and checking to see if username in use


def register():
    should_restart = True
    while should_restart:
        my_cursor.execute("SELECT * FROM users")
        user_name = input("Create Username:")
        should_restart = False
        for user in my_cursor:
            if user_name != user[1]:
                continue
            else:
                print(f"Username {user_name} Unavailable.")
                should_restart = True

    password = "placeholder"
    password2 = "placeholder2"
    while password != password2:
        password = input("Create Password: ")
        password2 = input("Confirm Password: ")

    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"  # Inserting new user into user table
    val = (user_name, password)
    my_cursor.execute(sql, val)
    mydb.commit()


def access():
    should_restart = True
    while should_restart:
        should_restart = False
        # user_name = input("Enter Username: ")
        # password = input("Enter Password: ")
        user_name = "nathan"
        password = "password"
        my_cursor.execute("SELECT * FROM users")

        for user in my_cursor:
            if user_name == user[1] and password == user[2]:
                print("Login Successful")
                print(f"Welcome {user[1]}!")
                should_restart = False
                return user[0]
            else:
                should_restart = True


def home(option=None):
    typo = input("Login | Signup:")
    option = typo.lower()
    if option == "login":
        return access()
    elif option == "signup":
        register()
    else:
        print("Please enter an option.")
        home()


userid = home()  # Assigning userid


def pantry_item_menu(p_item):
    print(f"\n**********{p_item} Menu**********")
    print("1. List Ingredients")
    print("2. Alter Inventory")
    print("3. Add New Ingredient")
    print("4. Back to Main")
    choice = int(input("Make a selection: "))
    return choice


def pantry_item(p_item):
    my_cursor.execute(f"SELECT * FROM {p_item} WHERE user_id = {userid}")
    columns = dict(zip(my_cursor.column_names, my_cursor.fetchone()))
    choice = 0
    while choice != 4:
        choice = pantry_item_menu(p_item)
        if choice == 1:
            print(f"\n********** {p_item} Inventory **********")
            for key, value in columns.items():
                if value == 1:
                    value = "In Stock"
                elif value == 0:
                    value = "Out of Stock"
                else:
                    pass

                if key != "user_id" and key != "user_id_fk":
                    print(f"{key : <15}:{value : <18}")

        elif choice == 2:
            print(f"\n********** {p_item} Inventory **********")
            for key, value in columns.items():
                if value == 1:
                    value = "In Stock"
                elif value == 0:
                    value = "Out of Stock"
                else:
                    pass

                if key != "user_id" and key != "user_id_fk":
                    print(f"{key : <16}:{value : <18}")

            item = input("What item you like to alter?: ")
            stock = int(input("Would you like to add or remove an ingredient? \
                               \n[1] Add \
                               \n[2] Remove\n"))
            if stock == 1:
                my_cursor.execute(f"UPDATE {p_item} \
                                   SET {item} = 1 \
                                   WHERE user_id = {userid}")
            elif stock == 2:
                my_cursor.execute(f"UPDATE {p_item} \
                                    SET {item} = 0 \
                                    WHERE user_id = {userid}")

        elif choice == 3:
            new = input("Enter name of ingredient you would like to add: ")
            choice = input("You entered " + new + ". Is this correct (Y or N)?")
            checked = choice.upper()
            if checked == "Y":
                my_cursor.execute(f"ALTER TABLE {p_item} \
                                    ADD COLUMN {new} INT DEFAULT 0;")
                print("Please restart app for changes to take effect.")
            else:
                print("Invalid Input")
    mydb.commit()


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
            pantry_item("Dairy")
        elif category == 2:
            pantry_item("Meat")
        elif category == 3:
            pantry_item("Vegetable")
        elif category == 4:
            pantry_item("Fruit")
        elif category == 5:
            pantry_item("Snack")
        elif category == 0:
            return
        else:
            print("Invalid Entry!")


def plan_meals():
    print("meals")


def shopping_list():
    first = input("Would you like to generate a shopping list (Y or N)?   ")
    final = first.lower()
    if final == "y":
        print("""****** Shopping List ******
                 [1] Full List
                 [2] One Category
                 [3] Custom""")
        choice = int(input("Make a selection: "))
        if choice == 1:
            my_cursor.execute(f"SELECT * FROM {p_item} WHERE user_id = {userid}")
            columns = dict(zip(my_cursor.column_names, my_cursor.fetchone()))
            choice = 0
            while choice != 4:
                choice = pantry_item_menu(p_item)
                if choice == 1:
                    print(f"\n********** {p_item} Inventory **********")
                    for key, value in columns.items():
                        if value == 1:
                            value = "In Stock"
                        elif value == 0:
                            value = "Out of Stock"
                        else:
                            pass
            my_cursor.execute("")
    elif final == "n":
        pass
    else:
        print("Invalid Input")


def plan_meals():
    print("plan em")


def recipes():
    print("It's recipes")


def make_check():
    print("can you make it?")


# //// Main Menu Functions ////

def menu():
    print("1. Check Pantry")
    print("2. Plan Meals")
    print("3. Generate Shopping List")
    print("4. Plan Meals")
    print("5. Recipes")
    print("6. What can I make?")
    print("0. Exit")


menu()
ch = int(input("Make a choice: "))
while ch != 0:
    if ch == 1:
        check_pantry()
    elif ch == 2:
        plan_meals()
    elif ch == 3:
        shopping_list()
    elif ch == 4:
        plan_meals()
    elif ch == 5:
        recipes()
    elif ch == 6:
        make_check()
    elif ch == 0:
        exit()
    else:
        print("Invalid Input")
    menu()
    ch = int(input("Make a choice: "))
