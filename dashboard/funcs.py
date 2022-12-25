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
