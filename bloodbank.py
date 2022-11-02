from unicodedata import name
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'bloodbankdb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("1 add blood banker")
    print("2 view all blood banker")  
    print("3 search a blood banker")
    print("4 update the blood banker")    
    print("5 delete a blood banker")
    print("6 average of blood donated")
    print("7 name of the donor with starting letter")
    print("8 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('blood banker enter selected')
        nameofdonar = input('enter the name')
        address = input('enter the address')
        phnno = input('enter the phno')
        bloodgroup = input('enter the bloodgroup ')
        litreofblood = input('enter the litreofblood')
        sql = 'INSERT INTO `bloodbank`( `nameofdonar`,`address`,`phnno`, `bloodgroup`,`literofblooddonated`) VALUES (%s,%s,%s,%s,%s)'

        data = (nameofdonar,address,phnno,bloodgroup,litreofblood)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        sql = 'SELECT * FROM `bloodbank`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search blood banker')
        bloodgroup = input('enter blood group')
        sql = "SELECT `id`,`nameofdonar`,`phnno`,`bloodgroup`,`literofblooddonated` FROM `bloodbank` WHERE `bloodgroup` = '"+bloodgroup+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update blood donar details')
        bloodgroup=input('enter the blood group')
        nameofdonar = input('enter the name')
        address =input('enter the details')
        phnno =input('enter the phone number')
        literofblooddonated=input('enter the litre of blood')
        sql = "UPDATE `bloodbank` SET `nameofdonar`='"+nameofdonar+"',`phnno`='"+phnno+"',`bloodgroup`='"+bloodgroup+"',`literofblooddonated`='"+literofblooddonated+"' WHERE `bloodgroup`='"+bloodgroup+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data updated succesfully")

        mycursor.execute(sql)
    elif(choice==5):
        print('delete the bloodbanker')
        bloodgroup = input('enter the blood group to be deleting: ')
        sql = "DELETE FROM `bloodbank` WHERE `bloodgroup`='"+bloodgroup+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted succesfully")
    elif(choice==6):
        print('Total blood donated ')
        sql = 'SELECT AVG(`literofblooddonated`) FROM `bloodbank` '
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==7):
       

        print('Name of the doner with starting letter')

        a = input('Enter the first letter of the name of the donar : ')

        sql = "SELECT `id`, `nameofdonar`, `address`, `phnno`, `bloodgroup`, `literofblooddonated` FROM `bloodbank` WHERE `nameofdonar` LIKE '%"+a+"%'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)
    elif(choice==8):
        break