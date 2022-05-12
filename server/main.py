# Importing library

import mysql.connector
# initialize connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="zxcvbnm",
database="pbl"
)
mycursor = mydb.cursor()

print(mydb)

#============================================================================
# START
# ===========================================================================

def input_student_data(PRN):
    fname = input("\nEnter First Name = ")
    lname = input("\nEnter Last Name = ")
    DOB = input("\nEnter Date of Birth (dd/mm/yyyy): = ")
    grad = int(input("\nEnter Graduation year = "))
    city = input("\nEnter City = ")
    gender = input("\nEnter your gender = ")

    mycursor.execute("insert into student values({}, {}, {}, {}, {}, {}, {});".format(PRN, fname, lname, DOB, grad, city, gender))
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
    print("1 record inserted, ID:", mycursor.lastrowid)


def input_course_data(PRN):
    #iterate
    
    pass

def input_subject_data(PRN):
    #iterate
    pass

def input_skill_data(PRN):
    skill_c = 0
    while(skill_c == 0):
        skill = input("\nEnter Skill Name = ")
        #check
        mycursor.execute("select skill_name form skill;")
        myresult = mycursor.fetchall()

        if(skill in myresult): 
            mycursor.execute("select skill_id form skill where skill_name = {}".format(skill))
            tempres = mycursor.fetchall()[0]
            mycursor.execute("insert into skill_prn values({}, {});".format(PRN,tempres))

            #prn import condition

        while(True):
            temp = int(input("\nDo you want to add another skill 1.Yes 2.No = "))
            if(temp == 1):
                skill_c = 0
                break
            elif(temp == 2):
                skill_c = 1
                break
            else:
                print("\nPlease enter valid choice!!")
                


def student():
    PRN = int(input('\nPlease enter your PRN = '))
    
    #check if PRN exists
    mycursor.execute("SELECT prn from student;")
    myresult = mycursor.fetchall()

    if(PRN in myresult):
        #edit
        ck = 0
        while(ck == 0):
            edit_ck = int(input("\n1.EDIT Profile\n2.EDIT Subject\n3.EDIT Skill\n4.EDIT Course\n5.Exit."))
            if(edit_ck == 1):
                col = input("\nEnter attribute to be updated = ")
                val = input("\nEnter value to be updated = ")
                mycursor.execute("UPDATE student SET {}={} where prn={};".format(col, val, PRN))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")

                #check if error exists

            elif(edit_ck == 2):
                col = input("\nEnter attribute to be updated = ")    #check if attribute exists
                val = input("\nEnter value to be updated = ")
                mycursor.execute("UPDATE student subject {}={} where prn={};".format(col, val, PRN))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                

            elif(edit_ck == 3):
                col = input("\nEnter attribute to be updated = ")
                val = input("\nEnter value to be updated = ")
                mycursor.execute("UPDATE skill SET {}={} where prn={};".format(col, val, PRN))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                #check 

            elif(edit_ck == 4):
                col = input("\nEnter attribute to be updated = ")
                val = input("\nEnter value to be updated = ")
                mycursor.execute("UPDATE course SET {}={} where prn={};".format(col, val, PRN))
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                #check

            elif(edit_ck == 5):
                ck = 1
            else:
                print("\nPlease enter valid choice!!")
        pass
    else:
        prn = int(input('\nPlease enter PRN = '))
        input_student_data(prn)
        input_course_data(prn)
        input_subject_data(prn)


def main():

    # Menu satrt
    ck = 0
    print("\nWelcome To Student Profiling System")

    while(ck>=0):
        print("\n1.STUDENT\n2.COMPANY\n3.EXIT")
        ck = int(input("\nEnter your choice = "))
        if(ck == 1):
            student()
        elif(ck == 2):
            company()
        elif(ck == 3):
            break
        else:
            print("\nEnter a Valid choice")
        ck = int(input("\Do you want to continue 1.Yes 2.No"))
    print("\nThank you")

main()







