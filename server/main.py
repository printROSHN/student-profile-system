# Importing library
import random
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

sub_map  = {"maths1":1,"sciences":2,"social science":3,"english1":4,"hindi":5,"physics":6,"chemistry":7,"maths2":8,"english2":9,"cs":10}
course_map = {"dsa":1,"coa":2,"em":3,"se":4,"ai":5,"dbms":6,"cn":7,"ml":8,"os":9,"eg":10}
#============================================================================
# START
# ===========================================================================
def check_attr(table_name, attr, val):
    while(True):
        mycursor.execute("select {} from {};".format(table_name, attr))
        res = mycursor.fetchall()
        myresult = [x[0] for x in result]
        if(val in myresult):
            return 1
        else:
            print("Value not found!!")
            return 0

def input_student_data(PRN):
    fname = input("\nEnter First Name = ")
    lname = input("\nEnter Last Name = ")
    DOB = input("\nEnter Date of Birth (dd/mm/yyyy): = ")
    grad = int(input("\nEnter Graduation year = "))
    city = input("\nEnter City = ")
    gender = input("\nEnter your gender = ")

    mycursor.execute("insert into student values({}, '{}', '{}', '{}', {}, '{}', '{}');".format(PRN, fname, lname, DOB, grad, city, gender))
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
    print("1 record inserted, ID:", mycursor.lastrowid)


def input_course_data(PRN):
    ky = course_map.keys()
    for x in ky:
        ip = int(input("\nEnter marks for {} = ".format(x)))
        mycursor.execute("insert into course_prn values ({}, {}, {})".format(course_map[x],PRN,ip))
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)

def input_subject_data(PRN):
    ky = sub_map.keys()
    for x in ky:
        ip = int(input("\nEnter marks for {} = ".format(x)))
        mycursor.execute("insert into subject_prn values ({}, {}, {})".format(PRN,sub_map[x],ip))
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)

def input_skill_data(PRN):
    skill_c = 0
    while(skill_c == 0):
        skill = input("\nEnter Skill Name = ")
        #check
        mycursor.execute("select skill_name from skill;")
        res = mycursor.fetchall()
        myresult = [x[0] for x in res]

        if(skill in myresult): 
            mycursor.execute("select skill_id form skill where skill_name = '{}';".format(skill))
            res = mycursor.fetchall()
            myresult = [x[0] for x in res]
            i_d = myresult[0]
            mycursor.execute("insert into skill_prn values({}, {});".format(PRN,i_d))
            mydb.commit()
            print("1 record inserted, ID:", mycursor.lastrowid)

        else:
            mycursor.execute("insert into skill(skill_name) values('{}');".format(skill))
            mydb.commit()
            print("1 record inserted, ID:", mycursor.lastrowid)

            mycursor.execute("select skill_id from skill where skill_name = '{}';".format(skill))
            res = mycursor.fetchall()
            myresult = [x[0] for x in res]
            i_d = myresult[0]

            mycursor.execute("insert into skill_prn values({},{})".format(PRN,i_d))
            mydb.commit()
            print("1 record inserted, ID:", mycursor.lastrowid)

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
    result = mycursor.fetchall()
    myresult = [x[0] for x in result]
    print(myresult)

    if(PRN in myresult):
        ck = 0
        while(ck == 0):
            edit_ck = int(input("\n1.EDIT Profile\n2.EDIT Subject\n3.EDIT Skill\n4.EDIT Course\n5.Exit."))
            if(edit_ck == 1):
                col = input("\nEnter attribute to be updated = ")
                val = input("\nEnter value to be updated = ")
                
                mycursor.execute("UPDATE student SET {}='{}' where prn={};".format(col, val, PRN))
                
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
                #input_skill_data(PRN)
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
        input_skill_data(prn)

def comapny_info(CID):
    cname = input("\nEnter Comapny name: ")
    ctype = input("\nEnter Comapny type: ")
    cloc = input("\nEnter Comapany Location: ")

    mycursor.execute("INSERT INTO company values({}, '{}', '{}', '{}');".format(CID, cname, ctype, cloc))
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

def create_opening():
    print("\nEnter Criteria for Openening => ")
    ssc_hsc = int(input("\nEnter average marks for SSC and HSC combine = "))
    avg_cgpa = int(input("\nEnter average marks for Course = "))
    checker1 = []
    checker2 = []

    mycursor.execute("select distinct prn from skill_prn;")
    result = mycursor.fetchall()
    myresult = [x[0] for x in result]
    #print(myresult)
    for i in myresult:
        mycursor.execute("select avg(marks) from subject_prn where prn = {}".format(i))
        res = mycursor.fetchall()
        myres = [x[0] for x in res]
        #print(myres[0])
        if(myres[0] >= ssc_hsc):
            checker1.append(i)
    
    mycursor.execute("select distinct prn from course_prn;")
    result = mycursor.fetchall()
    myresult = [x[0] for x in result]
    for i in myresult:
        mycursor.execute("select avg(marks) from course_prn where prn = {}".format(i))
        res = mycursor.fetchall()
        myres = [x[0] for x in res]
        #print(myres[0])
        if(myres[0] >= avg_cgpa):
            checker2.append(i)
    
    print(checker1,checker2)
    ck1 = set(checker1)
    ck2 = set(checker2)
    if (ck1 & ck2):
        print(ck1 & ck2)
    else:
        print("No Matching students to criteria")
    


def comapny_side(CID):
        create_opening()


def company():
    cid = int(input('\nPlease enter Comapny ID = '))

    mycursor.execute("SELECT c_id from company;")
    myresult = mycursor.fetchall()
    myres = [x[0] for x in myresult]


    if(cid in myres):
        comapny_side(cid)
        
    else:
        while(True):
            tp = int(input('\nThis comapny is not registered do you want to add a new company \n1.Yes\n2.No \n=> '))
            if(tp == 1):
                comapny_info(cid)
                comapny_side(cid)
                break
            elif(tp == 2):
                break



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
