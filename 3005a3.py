import psycopg2

# connecting to the postgre database for the assignment
conn = psycopg2.connect(database = "A3Q1",
                        host = "localhost",
                        password = "postgres",
                        user = "postgres",
                        port = "5432")

# creating a cursor tied to the connection
cursor = conn.cursor()

# uses sql and the fetch method to get all students
def getAllStudents():
    try:
        cursor.execute("SELECT * FROM students")
        print(cursor.fetchall())
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("Please try again.\n")
        exit()

# uses seperate sql and data strings to simplify the execut, and uses the commit method to ensure it is committed to the database
def addStudent(first_name, last_name, email, ennrollment_date):
    try:
        SQL = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        DATA = (first_name, last_name, email, ennrollment_date)
        cursor.execute(SQL, DATA)
        conn.commit()
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("Please try again.\n")
        exit()

# similar to addstudent, and all functions have error handling 
def updateStudentEmail(student_id, new_email):
    try:
        SQL = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(SQL, (new_email,student_id))
        conn.commit()
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("Please try again.\n")
        exit()

# deletes a student with the given student ID and throws an error if anything happens
def deleteStudent(student_id):
    try:
        SQL = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(SQL, student_id)
        conn.commit()
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("Please try again.\n")
        exit()

# main function
def main():
    flag = True
    while flag == True:
        print("Welcome to the Student Database! What function would you like to execute?\n")
        inp = input("1. getAllStudents 2. addStudent 3. updateStudentEmail 4. deleteStudent 5. quit: ")
        if inp == "1":
            getAllStudents()
        elif inp == "2":
            fn, ln, email, enrolldate = input("Enter First Name, Last Name, email, and enrollment date, seperated by spaces: ").split(" ")
            addStudent(fn, ln, email, enrolldate)
        elif inp == "3":
            studentid, email = input("Enter student ID and new email, separated by a space: ").split(" ")
            updateStudentEmail(studentid, email)
        elif inp == "4":
            deleteStudent(input("Enter Student ID to delete: "))
        elif inp == '5':
            conn.close
            flag = False
        else:
            print("Please input a valid argument.")
            pass

main()
conn.close()