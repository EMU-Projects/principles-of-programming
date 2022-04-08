import numpy as np

# Functions to manipulate arrays
def insert(arr, element):
    for i in range(len(arr)):
        if not arr[i]:
            arr[i] = element
            return True
    return False
            
def delete(arr, index):
    arr[index] = None

# Creating student class
class Student:
    def __init__(self, F_Name, L_Name, Age, Sex, Major):
        self.__F_Name = F_Name
        self.__L_Name = L_Name
        self.__Age = Age
        self.__Sex = Sex
        self.__Major = Major

    def getfname(self):
        return self._Student__F_Name

    def getlname(self):
        return self._Student__L_Name

    def getage(self):
        return self._Student__Age

    def getsex(self):
        return self._Student__Sex

    def getmaj(self):
        return self.__Major
    
    def printstud(self):
        print('First name: ', self.__F_Name,'\n', 'Last name: ', self.__L_Name,'\n','Age: ', self.__Age,'\n','Sex: ', self.__Sex,'\n','Major: ', self.__Major,'\n',)

    def setfname(self, fname):
        self._Student__F_Name = fname

    def setlname(self, lname):
        self._Student__L_Name = lname

    def setage(self, age):
        self._Student__Age = age

    def setsex(self, sex):
        self._Student__Sex = sex

    def setmaj(self, maj):
        self._Student__Major = maj

    def setstud(self):
        self._Student__F_Name = input('Enter first name: ')
        self._Student__L_Name = input('Enter last name: ')
        self._Student__Age = int(input('Enter age: '))
        self._Student__Sex = input('Enter Sex: ')
        self._Student__Major = input("Enter student's Major: ")


# Initializing student array with 100 elements
a = np.empty(100, dtype=Student)

# Adding 10 students
insert(a, Student("John", "Smith", 19, "M", "Economics"))
insert(a, Student("Mia", "Jones", 20, "F", "Computer Science"))
insert(a, Student("Konan", "Smith", 18, "F", "Economics"))
insert(a, Student("James", "Rich", 20, "M", "English Language"))
insert(a, Student("Jen", "Patrick", 21, "F", "Communications"))
insert(a, Student("Light", "Burns", 18, "M", "Business"))
insert(a, Student("Jean", "Marshall", 19, "M", "Computer Science"))
insert(a, Student("Vanessa", "Cole", 19, "F", "English Language"))
insert(a, Student("Jordan", "Duke", 20, "M", "Psychology"))
insert(a, Student("Todd", "Brady", 22, "M", "Computer Science"))

# Function to find a subset of students based on criteria
def find(arr, criteria):
    temp_arr = []
    for i in range(len(arr)):
        if arr[i]:
            fname = None or "fname" in list(criteria.keys()) and criteria["fname"]
            lname = None or "lname" in list(criteria.keys()) and criteria["lname"]
            age = None or "age" in list(criteria.keys()) and criteria["age"]
            sex = None or "sex" in list(criteria.keys()) and criteria["sex"]
            major = None or "major" in list(criteria.keys()) and criteria["major"]
            if fname and arr[i].getfname() != fname:
                continue
            if lname and arr[i].getlname() != lname:
                continue
            if age and arr[i].getage() != age:
                continue
            if sex and arr[i].getsex() != sex:
                continue
            if major and arr[i].getmaj() != major:
                continue
            temp_arr.append(arr[i])
    return temp_arr

x = "1"
while x != "0":
    input("Press enter to continue...")
    print('WELCOME! \n 1) Add a new student \n 2) Find a student by first name and last name \n 3) Show all students \n 4) Show all students in a given age range \n 5) Modify a student record \n 6) Delete a student \n 7) Write content to file \n 8) Read student data from a file into list  \n 9) Search students by criteria \n 0) Exit \n')
    x = input('Enter a digit: ')
    
    # Add a student if they don't exist in the list
    if x == '1':
        i = 0
        temp = Student('', '', 0,'' , '')
        temp.setstud()
        students = find(a, {"fname": temp.getfname(),"lname":temp.getlname()})
        if students:
            print("A student by that name already exists!")
        
        elif insert(a,temp):
            print("Student is inserted into the list")
        else:
            print("List is full")
    
    # Find a student using first and last name criteria
    elif x == "2":
        temp1 = input('Enter first name: ')
        temp2 = input('Enter last name: ')
        students = find(a, {"fname": temp1,"lname":temp2})
        if not students:
            print('Student not found :(')
        else:
            students[0].printstud()
            
    # Display all students in the array
    elif x == "3":
        for student in a:
            if student:
                student.printstud()
    
    # Print students within a given age range
    elif x == "4":
        print("Provide age range:")
        min_age = int(input("Enter minimum age:"))
        max_age = int(input("Enter maximum age:"))
        for student in a:
            if (student and student.getage() >= min_age and student.getage() <= max_age):
                student.printstud()
    
    # Find a student and change their info
    elif x == "5":
        i = 0
        temp1 = input('Enter first name: ')
        temp2 = input('Enter last name: ')
        found = False
        while i < len(a):
            if a[i]:
                tempfname = a[i].getfname()
                templname = a[i].getlname()
                if tempfname == temp1 and templname == temp2:
                    age_inp = input("Enter new age (leave empty if you don't want to change'):")
                    sex_inp = input("Enter new sex (leave empty if you don't want to change'):")
                    major_inp = input("Enter new major (leave empty if you don't want to change'):")
                    if (age_inp):
                        a[i].setage(int(age_inp))
                    if(sex_inp):
                        a[i].setsex(sex_inp)
                    if(major_inp):
                        a[i].setmaj(major_inp)
                    found = True
                    break
            i = i+1
        
        if not found:
            print('Student not found :(')
    
    # Set a student to None (Deleting a student)
    elif x == "6":
        i = 0
        temp1 = input('Enter first name: ')
        temp2 = input('Enter last name: ')
        found = False
        while i < len(a):
            if a[i]:
                tempfname = a[i].getfname()
                templname = a[i].getlname()
                if tempfname == temp1 and templname == temp2:
                    a[i] = None
                    print("Student is now deleted!")
                    found = True
                    break
            i = i+1
        
        if not found:
            print('Student not found :(')
    
    # Store students into a file as (firstname|lastname|age|sex|major) each line for each student
    elif x == "7":
        file = open("students.txt","w")
        for x in a:
            if x:
                file.write(x.getfname()+"|"+x.getlname()+"|"+str(x.getage())+"|"+x.getsex()+"|"+x.getmaj()+"\n")
        file.close()
        print("Student list is written to students.txt")
    
    # Load data from students.txt into the array 'a'
    elif x == "8":
        a = np.empty(100, dtype=Student)
        file = open("students.txt","r")
        for line in file.readlines():
            v = line.strip().split("|")
            insert(a, Student(v[0],v[1],int(v[2]),v[3],v[4]))
        file.close()
        print("Student list is loaded from students.txt")
    
    # Find subset of students with a more extensive criteria
    elif x == "9":
        print("\n- Enter the criteria -")
        fname = input("Enter first name (or leave empty): ") or None
        lname = input("Enter last name (or leave empty): ") or None
        age = input("Enter age (or leave empty): ") or None
        if age:
            age = int(age)
        sex = input("Enter sex (or leave empty): ") or None
        major = input("Enter major (or leave empty): ") or None
        students = find(a, {"fname": fname,"lname":lname,"age":age,"sex":sex,"major":major})
        for student in students:
            student.printstud()