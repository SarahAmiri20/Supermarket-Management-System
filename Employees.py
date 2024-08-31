class EmployeeNode:
    def __init__(self, name, position, age, salary):
        self.name = name.lower()
        self.position = position
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Age: {self.age}, Salary: {self.salary}"

    def from_string(cls, string):
        name, position, age, salary = string.strip().split(',')
        age = int(age)
        salary = int(salary)
        return cls(name, position, age, salary)


class Node:
    def __init__(self, employee):
        self.employee = employee
        self.left = None
        self.right = None


class EmployeeBST:
    def __init__(self):
        self.root = None

    def add_employee(self, employee):
        if not self.root:
            self.root = Node(employee)
        else:
            employee_node = Node(employee)
            self.add_employee_recursive(self.root, employee_node)

    def add_employee_recursive(self, node, employee_node):
        if employee_node.employee.name < node.employee.name:
            if node.left:
                self.add_employee_recursive(node.left, employee_node)
            else:
                node.left = employee_node
        else:
            if node.right:
                self.add_employee_recursive(node.right, employee_node)
            else:
                node.right = employee_node

    def remove_employee(self, name):
        self.root = self.remove_employee_recursive(self.root, name)

    def remove_employee_recursive(self, node, name):
        if not node:
            return None 
        elif name < node.employee.name:
            node.left = self.remove_employee_recursive(node.left, name)
        elif name > node.employee.name:
            node.right = self.remove_employee_recursive(node.right, name)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.employee = min_node.employee
                node.right = self._remove_min(node.right)

        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _remove_min(self, node):
        if node.left:
            node.left = self._remove_min(node.left)
            return node
        else:
            return node.right


    def search_employee(self, name):
        node = self.search_employee_recursive(self.root, name)
        if node:
            return node.employee
        else:
            return None


    def search_employee_recursive(self, node, name):
        if not node or node.employee.name == name:
            return node

        if name < node.employee.name:
            return self.search_employee_recursive(node.left, name)
        
        else:
            return self.search_employee_recursive(node.right, name)

    def edit_employee(self, name, property_name, new_value):
        employee = self.search_employee(name)
        if employee:
            setattr(employee, property_name, new_value)

    def traverse_inorder(self):
        self.traverse_inorder_recursive(self.root)

    def traverse_inorder_recursive(self, node):
        if node:
            self.traverse_inorder_recursive(node.left)
            print(node.employee)
            self.traverse_inorder_recursive(node.right)
