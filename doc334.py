#---- Check Connectivity----------
import mysql.connector
from mysql.connector import Error

try:
    conn=mysql.connector.connect(host='localhost',user='root',password='')
    if conn.is_connected():
        print("connected")

except Error as e:
    print("oops")
    print(e)


#------------View the available databases---------
# open database connection

db= mysql.connector.connect(host="localhost",
                            user="root",
                            password="")

#prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method
print("available databases = ")
cursor.execute("SHOW DATABASES")

# Fetch results using fetchall() method
data=cursor.fetchall()


for item in data:
   print(item)
  

#------create menu-----------
   
def menu():
    print("Student Details")
    print("[1] View all student details")
    print("[2] Insert new student details")
    print("[3] update")
    print("[4] Delete")
    print("Attendance")
    print("[5] view all attendance details")
    print("[6] For mark attendance")
    print("[7] search")
    print("[8] Exit")
    

menu()
option= int(input("\nEnter your prefered option:"))

while option != 8:
#-----------View all student details in student details table ---------------
    if option==1:

        import mysql.connector
# open database connection with  a dictionery

        conDict={'host':'localhost',
        'database':'db_school_attendance',
        'user':'root',
        'password':''}
        db= mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor()method
        
        cursor=db.cursor()
# execute SQL query using execute() method
        cursor.execute("SELECT * FROM studentdetails")
        
# Fetch result using fetchall() method
        data=cursor.fetchall()

        for item in data:
            print(item)

        menu()
        option= int(input("\nEnter your prefered option:"))

#------------Insert new student details--------------
    elif option==2:

        import mysql.connector

# open database connection with  a dictionery
        
        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}
        db= mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# read user input

        StudentNo=input("Type student No:")
        FName=input("Type first name:")
        LName=input("Type last name:")

# execute SQL query using execute() method

        mySQLText="INSERT INTO studentdetails(StudentNo,FName,LName) VALUES (%s,%s,%s)"
        myValues=(StudentNo,FName,LName)
        cursor.execute(mySQLText,myValues)

# commit the change

        db.commit()

        print(cursor.rowcount,"Record Added")
        
        menu()
        option= int(input("\nEnter your prefered option:"))

#----------update-----------------
    elif option==3:

        
# open database connection with  a dictionery
        
        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}
        db= mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# read user input

        StudentNo=input("Type studentNo:")
        FName=input("Type new first name:")
        LName=input("Type new Last name:")

# Prepare a cursor object using cursor()method

        updTxt="UPDATE studentdetails SET FName= '" + FName + "' WHERE StudentNo = " + StudentNo
        updTxt="UPDATE studentdetails SET LName= '" + LName + "' WHERE StudentNo = " + StudentNo
        cursor.execute(updTxt)

# commit the change

        db.commit()
        print(cursor.rowcount," Record Updated")
        db.close()

        menu()
        option= int(input("\nEnter your prefered option:"))

#--------------Delete----------------
    elif option==4:

        import mysql.connector
        
#open database connection with  a dictionery
        
        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}
        db = mysql.connector.connect(**conDict)
        
# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# read user input

        StudentNo= input(" Type a student No :")

# Prepare a cursor object using cursor()method

        cursor.execute(" DELETE FROM studentdetails WHERE StudentNo= " + StudentNo + "")

# commit the change

        db.commit()

        print(cursor.rowcount," Record Deleted")

    

        menu()
        option= int(input("\nEnter your prefered option:"))

#--------------view all attendance details-------------
    elif option==5:

        import mysql.connector
        
# open database connection with  a dictionery 
        
        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}
        db= mysql.connector.connect(**conDict)
        
# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# execute SQL query using execute() method

        cursor.execute("SELECT * FROM attendance")

# Fetch result using fetchall() method

        data=cursor.fetchall()

        for item in data:
            print(item)

        menu()
        option= int(input("\nEnter your prefered option:"))


#----------------For mark attendance----------------
    elif option==6:

        import mysql.connector
        
# open database connection with  a dictionery
        
        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}

        db= mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# execute SQL query using execute() method
        cursor.execute("SELECT DISTINCT StudentNo,Fname FROM studentdetails")

# Fetch result using fetchall() method
        data=cursor.fetchall()
        
        print("student count :")
        for item in data:
            print(item)

# input student count 
        StudentNo=0
        student =int(input("student count :"))
        Day=input("Date(YYYY-MM-DD) :")


            
# using while loop ask date and attendance

        while StudentNo<student:
            print("0 means 1")
            print("Student No :",StudentNo)
            

# read user input

            
            Attendance=input("student present today :")
            StudentNo+=1

# execute SQL query using execute() method    
            mySQLText="INSERT INTO attendance(StudentNo,Day,Attendance) VALUES (%s,%s,%s)"
            myValues=(StudentNo,Day,Attendance)
            cursor.execute(mySQLText,myValues)


# commit the change

            db.commit()

            print(cursor.rowcount,"Record Added")

        menu()
        option= int(input("\nEnter your prefered option:"))

#------------search---------------
    elif option==7:

        import mysql.connector

# open database connection with  a dictionery

        conDict={'host':'localhost',
                 'database':'db_school_attendance',
                 'user':'root',
                 'password':''}

        db= mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor()method

        cursor=db.cursor()

# read user input

        StudentNo=input("Enter StudentNo :")

# execute SQL query using execute() method
    
        mySQLText="select * from attendance where StudentNo like '%{}%'".format(StudentNo)

# execute SQL query using execute() method

        cursor.execute(mySQLText)

# Fetch result using fetchall() method

        rows=cursor.fetchall()
    
        for row in rows:
            print(row)
        db.close()

        menu()
        option= int(input("\nEnter your prefered option:"))

#----------EXIT-----------    

print("thanks for using this programme")
print("EXIT")



        


        


        


        




        

    
