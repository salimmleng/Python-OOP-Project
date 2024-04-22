from food_item import FoodItem
from menu import Menu
from order import Order
from restaurant import Restaurant
from users import Customer,Admin,Employee

res = Restaurant('KFC')

def customer_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    address = input('Enter your Address: ')
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name}')
        print('1. View menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. PayBill')
        print('5. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            customer.add_to_cart(res,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print('Invalid input')


def admin_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    address = input('Enter your Address: ')
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {admin.name}')
        print('1. Add new Item')
        print('2. Add new Employee')
        print('3. View Employee')
        print('4. View items')
        print('5. Delete item')
        print('6. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            item_name = input('Enter item name: ')
            item_price =int(input('Enter item price: '))
            item_quantity = int(input('Enter item quantity: '))
            item = FoodItem(item_name,item_price,item_quantity) 
            admin.add_new_item(res,item)
        elif choice == 2:
            name = input('Enter employee name: ')
            email = input('Enter employee email: ')
            phone = int(input('Enter employee phone number: '))
            address = input('Enter employee address: ')
            age = int(input('Enter employee age: '))
            designation = input('Enter employee designation: ')
            salary = int(input('Enter employee salary: '))
            employee = Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(res,employee)
        elif choice == 3:
            admin.view_employee(res)

        elif choice == 4:
            admin.view_menu(res)
        elif choice == 5:
            item_name = input('Enter item that you want to remove: ')
            admin.remove_item(res,item_name)
        elif choice == 6:
            break
        else:
            print('Invalid input')


while True:
    print('Welcome !! ')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')

    ch = int(input('Enter your choice: '))
    if ch == 1:
        customer_menu()
    elif ch == 2:
        admin_menu()
    elif ch == 3:
        break
    else:
        print('Invalid input')