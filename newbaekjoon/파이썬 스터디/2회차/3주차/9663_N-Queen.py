# Corrected passenger list
passenger_list = [
    ['1', 'John, Mr. Henry', 'A2'],
    ['2', 'Allen, Mr. Marti', 'C4'],
    ['3', 'Patrick', 'B2'],
    ['4', 'Graham, Ms. Catherine', 'C17'],
    ['5', 'Peter, Mrs. Emile', 'A1'],
    ['6', ' ', 'B3'],
    ['7', 'John, Mr. Kim', 'A'],
    ['8', 'Wang, Mrs. Olivia', 'B'],
    ['9', ' , Mr', 'B'],
    ['10', ' ', 'C23']
]

# Function to count the number of females
def func1():
    female = 0
    for line in passenger_list:
        if "Mrs." in line[1] or "Ms." in line[1]:
            female += 1
    print("female: %d" % female)

# Function to count the number of passengers in each class
def func2():
    a_class = 0
    b_class = 0
    c_class = 0
    for line in passenger_list:
        if "A" in line[2]:
            a_class += 1
        elif "B" in line[2]:
            b_class += 1
        elif "C" in line[2]:
            c_class += 1
    print("A Class: %d" % a_class)
    print("B Class: %d" % b_class)
    print("C Class: %d" % c_class)

# Function to count the number of males
def func3():
    import re
    male = 0
    mr = re.compile(r'.*Mr.*')
    for line in passenger_list:
        if mr.search(line[1]):
            male += 1
    print("male: %d" % male)

# Function to remove digits from the class column
def func4():
    for line in passenger_list:
        line[2] = ''.join(i for i in line[2] if not i.isdigit())
    print("Updated passenger list with digits removed from class column:")
    print(passenger_list)

# Function to remove numbers and spaces from names
def func5():
    for line in passenger_list:
        line[1] = ''.join(line[1].split())
    print("Updated passenger list with names corrected:")
    print(passenger_list)

# Running the functions to check the output
func1()
func2()
func3()
func4()
func5()

