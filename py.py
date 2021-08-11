print("====== CRUD OPERATION IN PYTHON  | BY ONKAR JHA==============")
print("====== INSTAGRAm | onkarjha2003=========")
import mysql.connector as onkar
conn=onkar.connect(host="localhost",user="root",passwd="",database="onkar")
cursor=conn.cursor()
def insert():
    name=input("Enter your name:")
    phone=input("Enter your phone")
    sql="insert into onkar (name,phone) values(%s,%s)"
    val=(name,phone)
    try:
        cursor.execute(sql,val)
        conn.commit()
        print("Successful")
        menu()
    except exception as e: 
        print(e)
        menu()
def read():
    sql="select * from onkar"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for x in data:
            print(x)
        print("successful")
        menu()
    except:
        print("Error occured")
        menu()
def delete():
    ch=input("Do u have row id?(y/n)").lower()
    if(ch=='y'):
        idd=input("Enter your row id")
        sql="delete from onkar where id=%s"
        val=(idd,)
        try:
            cursor.execute(sql,val)
            conn.commit()
            print("Successful")
            menu()
        except:
            print("Error")
            menu()
    else:
        print("Go to read section and get your id")
        menu()
        #

        
def update():
    ch=input("Do u have row id?(y/n)").lower()
    if(ch=='y'):
        idd=input("Enter your row id")
        sql="select * from onkar where id=%s"
        val=(idd,)
        try:
            cursor.execute(sql,val)
            data=cursor.fetchall()
            for x in data:
                name=x[1]
                phone=x[2]
            print("1.update phone\n2.update name")
            ch=int(input("Enter your choice"))
            if(ch==1):
                phone=input("Enter your value")
            elif(ch==2):
                name=input("Enter your new name")
            else:
                print("wrong input")
                menu()
            sql="update onkar set name=%s,phone=%s where id=%s"
            val=(name,phone,idd)
            try:
                cursor.execute(sql,val)
                conn.commit()
                print("Successful")
                menu()
            except exception as e:
                print("error")
                menu()
        except exception as e:
            print(e)
            menu()

        
        #
def menu():
    print("Select any option\n1. Insert\n2. Read\n3.Update\n4. Delete")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        insert()
    elif(ch==2):
        read()
    elif(ch==3):
        update()
    elif(ch==4):
        delete()
    else:
        print("Wrong input choosn")
        menu()
menu()
