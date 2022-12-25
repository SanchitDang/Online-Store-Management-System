import mysql.connector as sqltor
from tabulate import tabulate


# Establishing connection
mycon = sqltor.connect(host='localhost', user='root', passwd='1234', database='store')
mycur = mycon.cursor()  # Defining name of the cursor


# Functions
def create_database():
    sqlusername = input('Enter SQL Username: ')
    sqlpassword = input('Enter SQL Password: ')

    myconn = sqltor.connect(host="localhost", user=sqlusername, password=sqlpassword)
    mycurr = myconn.cursor()

    mycurr.execute("CREATE DATABASE store")


def createtable_Admin_data():
    query = "CREATE TABLE Admin_data (Admin_ID int(11) " \
            "NOT Null PRIMARY KEY," \
            "Name varchar(100) NOT Null," \
            "Password varchar(100) NOT Null," \
            "Phone_Number int(11))"
    mycur.execute(query)


def createtable_Employee_data():
    query = "CREATE TABLE Employee_data (Admin_ID int(11) " \
            "NOT Null PRIMARY KEY," \
            "Name varchar(100) NOT Null," \
            "Password varchar(100) NOT Null," \
            "Phone_Number int(11))"
    mycur.execute(query)


def createtable_Customer_data():
    query = "CREATE TABLE Customer_data (Admin_ID int(11) " \
            "NOT Null PRIMARY KEY," \
            "Name varchar(100) NOT Null," \
            "Password varchar(100) NOT Null," \
            "Phone_Number int(11))"
    mycur.execute(query)


def create_admin():
    admin_id = int(input('Enter Admin Code: '))
    name = input('Enter Admin Name: ')
    passw = input('Enter Admin Password: ')
    phone = int(input('Enter Employee Phone Number: '))

    query = "INSERT INTO Admin_Data(Admin_ID, Name, Password, Phone_Number) " \
            "VALUES({}, '{}', '{}', {})".format(admin_id, name, passw, phone)


    mycur.execute(query)
    mycon.commit()
    print('Employee Created Successfully!')

def read_rec():
    mycur.execute('select * from data')  # Executes the sql command
    data = mycur.fetchall()  # Returns a list of tuples
    print(tabulate(data, headers=['Code', 'Name', 'Price', 'Quantity']))  # Make table with given heading


def create_rec():
    code = int(input('Enter item Code: '))
    name = input('Enter item Name: ')
    price = int(input('Enter item Price: '))
    quantity = int(input('Enter quantity of item: '))

    query = "INSERT INTO data(Item_Code, Item_Name, Item_Price, Item_Quantity) " \
            "VALUES({}, '{}', {}, {})".format(code, name, price, quantity)      # Sql statement to be executed
    
    mycur.execute(query)
    mycon.commit()  # To Commit the changes in table in sql database


def update_price():
    name = input('Enter name of the item whose amount to be changed: ')
    new_amount = input('Enter the new amount: ')

    query = " UPDATE data SET Item_Price = {} WHERE Item_Name = '{}' ".format(new_amount, name)


    mycur.execute(query)
    mycon.commit()


def update_quantity():
    name = input('Enter name of the item whose Quantity to be changed: ')
    new_quantity = input('Enter the new Quantity: ')

    query = " UPDATE data SET Item_Quantity = {} WHERE Item_Name = '{}' ".format(new_quantity, name)


    mycur.execute(query)
    mycon.commit()


def delete_rec():
    delete = input('Enter name of Product you want to delete: ')

    query = "DELETE FROM data WHERE Item_name = '{}' ".format(delete)


    mycur.execute(query)
    mycon.commit()
    print('Value Deleted')


def search_rec():
    search = input('Enter the Name of the Item you want to search: ')

    query = "SELECT * FROM data WHERE Item_Name = {}".format(search)


    mycur.execute(query)

    data = mycur.fetchall()
    print()
    print(tabulate(data, headers=['Code', 'Name', 'Price', 'Quantity']))  # Make table with given heading


def low_stock():
    mycur.execute('SELECT * FROM data WHERE Item_Quantity < 10')
    data = mycur.fetchall()  # Returns value in list

    if data == []:  # if list is empty ie all quantity are more than 10
        print('All Stock Sufficient')
    else:
        print('Stock Low for following:')
        print(tabulate(data, headers=['Code', 'Name', 'Price', 'Quantity']))


def add_employee():
    emp_id = int(input('Enter Employee Code: '))
    name = input('Enter Employee Name: ')
    passw = input('Enter Employee Password: ')
    phone = int(input('Enter Employee Phone Number: '))

    query = "INSERT INTO Employee_Data(Employee_ID, Name, Password, Phone_Number) " \
            "VALUES({}, '{}', '{}', {})".format(emp_id, name, passw, phone)


    mycur.execute(query)
    mycon.commit()
    print('Employee Created Successfully!')


def remove_employee():
    delete = input('Enter name of Employee you want to delete: ')

    query = " DELETE FROM Employee_Data WHERE Name = '{}' ".format(delete)


    mycur.execute(query)
    mycon.commit()  # Commit the changes in the table
    print('Employee Deleted Successfully')


def show_employee():
    mycur.execute('select * from Employee_data')  # Executes the sql command

    data = mycur.fetchall()
    for row in data:
        print(row)


def manage_employee():
    while True:
        print("Enter '1' To show Employees")
        print("Enter '2' To Add Employee")
        print("Enter '3' To Delete Employee")
        choice = int(input('--> '))
        print()

        if choice == 1:
            show_employee()
            break

        elif choice == 2:
            add_employee()
            break

        elif choice == 3:
            remove_employee()
            break

        else:
            input('Enter Valid Choice! \nPress Enter To Try Again')
            continue


def print_bill():
    print('The Following Items are In Stock:-')
    read_rec()
    print()
    table = []

    ans = 'y'
    while ans == 'y':
        item = input("Enter Name Of The 'Item' Customer Want's To Purchase: ")
        quan_chosen = int(input('Enter Quantity: '))

        query = " SELECT * FROM data WHERE Item_Name = '{}' ".format(item)
        mycur.execute(query)

        data = mycur.fetchone()  # Returns one row at a time in tuple format
        rec = list(data)  # Converts tuple to list
        # rec list will be like:-  [Item_Code, Item_Name, Item_Price, Item_Quantity]

        bill_row = [rec[1], rec[2], quan_chosen, rec[2] * quan_chosen]
        # Now bill_row will be like:-  [Name, Price, Quantity_Chosen, Price*Quantity_Chosen]

        table.append(bill_row)
        # On each iteration each bill row will be added to list named table

        ans = input("Enter 'y' to continue & 'n' to stop: ")
        # y to add more items in bill and n to stop

    price = 0  # Initial price
    print('\n*****************Bill*****************')
    for BillRow in table:
        price += BillRow[3]
    print(tabulate(table, headers=['Name', 'Price', 'Quantity', 'Total']))
    print('\nTOTAL PRICE: ', price)
    print('*****************Bill*****************')


# __main__
prog_end = False
while prog_end == False:  # while loop will be terminated by break or when some condition is given
    print('\n*********STORE MANAGEMENT SYSTEM*********')

    choice = int(input("Press '1' for ADMIN & '2'for CASHIER: "))

    if choice == 1:
        name = input('\nEnter your Name(Case Sensitive): ')
        passw = input('Enter your Password: ')

        mycur.execute('select * from Admin_Data')  # Executes the sql command
        data = mycur.fetchall()

        for row in data:
            if name != row[1] or passw != row[2]:  # Table Content: Admin_ID, Name, Password, PhoneNo.
                input('\nInvalid Username or Password!! \nPress Enter try again...')

            elif name == row[1] and passw == row[2]:
                while True:
                    print("\nEnter '1' to See Stock")
                    print("Enter '2' to Add New Item ")
                    print("Enter '3' to Update Price Of Item")
                    print("Enter '4' to Update Quantity Of Item ")
                    print("Enter '5' to Delete An Item")
                    print("Enter '6' to Search For An Item")
                    print("Enter '7' to See Items With Low Stock")
                    print("Enter '8' to Manage Employee")
                    print("Enter '9' to Stop The Program")

                    choice = int(input('--> '))
                    print()

                    if choice == 1:
                        read_rec()
                    elif choice == 2:
                        create_rec()
                    elif choice == 3:
                        update_price()
                    elif choice == 4:
                        update_quantity()
                    elif choice == 5:
                        delete_rec()
                    elif choice == 6:
                        search_rec()
                    elif choice == 7:
                        low_stock()
                    elif choice == 8:
                        manage_employee()
                    elif choice == 9:
                        mycon.close()  # If given in def then connection will be closed & further commands will not work
                        print('Program Ended...')
                        prog_end = True
                        break
                    else:
                        input("Enter a valid choice\nPress any key to continue")
                        continue
    elif choice == 2:
        name = input('\nEnter your Name(Case Sensitive): ')
        passw = input('Enter your Password: ')

        mycur.execute('select * from Employee_Data')  # Executes the sql command
        data = mycur.fetchall()
        for row in data:
            if name != row[1] or passw != row[2]:  # Table Content Emp_ID, Name, Password, PhoneNo.
                input('\nInvalid Username or Password!! \nPress Enter to try again...')

            elif name == row[1] and passw == row[2]:
                while True:
                    print("\nEnter '1' to See Stock")  # \n to leave a blank line after every loop (looks)
                    print("Enter '2' to Add New Item ")
                    print("Enter '3' to Update Quantity Of Item ")
                    print("Enter '4' to Search For An Item")
                    print("Enter '5' to See Items With Low Stock")
                    print("Enter '6' to Make Bill")
                    print("Enter '7' to Stop The Program")

                    choice = int(input('--> '))
                    print()

                    if choice == 1:
                        read_rec()
                    elif choice == 2:
                        create_rec()
                    elif choice == 3:
                        update_quantity()
                    elif choice == 4:
                        search_rec()
                    elif choice == 5:
                        low_stock()
                    elif choice == 6:
                        print_bill()
                    elif choice == 7:
                        mycon.close()
                        print('Program Ended...')
                        prog_end = True
                        break  # After breaking this loop it will move to previous while loop
                    else:
                        input("Enter a valid choice\nPress any key to continue")
                        continue

    else:
        input('\nInvalid Option! \nPress Any key to try again...')
        continue  # Continue will make the loop to go back to starting of loop i.e., First while
