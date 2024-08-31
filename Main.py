from Employees import EmployeeNode,EmployeeBST
from ProductInventory import CategoryBST,BrandLinkedList, ProductInventory, SalesLogQueue

employee_tree = EmployeeBST()
category_tree = CategoryBST()
brand_list = BrandLinkedList()
product_inventory= ProductInventory()
sales_log = SalesLogQueue()

def build_employee_tree():
    with open("Employees.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            employee_data = line.strip().split(", ")
            name = employee_data[0]
            position = employee_data[1]
            age = employee_data[2]
            salary = employee_data[3]
            age = int(age)
            salary = int(salary)
            employee = EmployeeNode(name,position,age,salary)
            employee_tree.add_employee(employee)

    print("Employee Tree Built  successfully.")

build_employee_tree()

def build_product_inventory():
    with open("Products.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            product_data = line.strip().split(", ")

        # Check if product_data has enough elements before accessing
            if len(product_data) >= 5:
                name = product_data[0]
                category = product_data[1]
                brand = product_data[2]
                price = product_data[3]
                quantity = product_data[4]
                
                price = float(price)
                quantity = int(quantity)
                category_tree.insert_category(category)
                brand_list.insert_brand(brand)
                product_inventory.insert_product(name, category, brand, price, quantity)
                
    print("Product Inventory Built  successfully.")
        

build_product_inventory()

def show_main_menu():
    print("Menu:")
    print("1. Employees")
    print("2. Product Inventory")
    print("0.Exit")

def show_employees_menu():
    print("Employees Menu:")
    print("1. Add Employee")
    print("2. Search for an Employee")
    print("3. Remove an Employee")
    print("4. Edit Employee Data") 
    print("5. Print all Employees") 
    print("0.Exit")

def show_inventory_menu():
    print("Product Inventory Menu:")
    print("1. Insert Product")
    print("2. Search for a Product")
    print("3. Sell Product")
    print("4. Show Sales Log")
    print("5. Print all Categories")
    print("6. Print all Brands for a Category")
    print("0.Exit")

while True:
    show_main_menu()

    option = input("Choose one option (0, 1, or 2): ")

    if option == "1":
        while True:
            show_employees_menu()
            employee_option = input("Choose another option (1-5 or 0 to exit): ")

            if employee_option == "1":
                name = input("Enter employee's full name: ").lower() 
                position = input("Enter employee's position: ").lower() 
                age = int(input("Enter employee's age: "))
                salary = int(input("Enter employee's salary: "))
                employee = EmployeeNode(name, position, age, salary)
                employee_tree.add_employee(employee)
                print("Employee added successfully.")

            elif employee_option == "2":
                name = input("Enter the full name of the employee to search for: ").lower()
                employee = employee_tree.search_employee(name)
                if employee:
                    print("Employee found:", employee)
                else:
                    print("Employee not found.")

            elif employee_option == "3":
                name = input("Enter employee's full name to remove: ").lower()
                employee_tree.remove_employee(name)
                print("Employee removed successfully.")

            elif employee_option == "4":
                name = input("Enter employee full name to edit: ").lower()
                employee = employee_tree.search_employee(name)
                if employee:
                    print("Current employee data:", employee)
                    property_name = input("Choose a property to edit (name/position/age/salary): ").lower()
                    new_value = input("Enter its new value: ")
                    setattr(employee, property_name, new_value)
                    print("Employee data edited successfully.")
                
            elif employee_option == "5":
                 print("All Employees:")
                 employee_tree.traverse_inorder()

            elif employee_option=="0":
                break
            else:
                print("Invalid option. Please try again.")


    elif option == "2":
        while True:
            show_inventory_menu()
            inventory_option = input("Choose another option (1-6): ")

            if inventory_option == "1":
                name = input("Enter product name: ").strip()
                category = input("Enter product category: ").strip()
                brand = input("Enter product brand: ").strip()
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                product_inventory.insert_product(name, category, brand, price, quantity)
                print("Product inserted successfully.")

            elif inventory_option == "2":
                category = input("Enter product category: ").strip()
                brand = input("Enter product brand: ").strip()
                name = input("Enter product name: ").strip()
                product_inventory.search_product(category, brand, name)
                
            elif inventory_option== "3":
                category = input("Enter product category: ").strip()
                brand = input("Enter product brand: ").strip()
                name = input("Enter product name: ").strip()
                quantity = int(input("Enter quantity to sell: "))
                product_inventory.sell_product(category, brand, name, quantity)
                sales_log.enqueue_sale(name, category, brand, product_inventory.get_product_price(category, brand, name))
                print("Product sold successfully.")

            elif inventory_option == "4":
                print("Sales Log:")
                sales_log.print_sales_log()

            elif inventory_option == "5":
                print("All Categories:")
                category_tree.print_all_categories()
               
            elif inventory_option == "6":
                category = input("Enter category name: ")
                print("All Brands for Category:", category)
                product_inventory.print_all_brands(category)

            elif inventory_option=="0":
                break

            else:
                print("Invalid option. Please try again.")
        
    elif option=="0":
        break
    
    else:
        print("Invalid option. Please try again.")
        







