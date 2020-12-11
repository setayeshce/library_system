import pickle
import os

PATH=  "C:/Users/Asus/Desktop/"

def check_validation():

    if not os.path.exists(PATH + "users.dat"):
        f=open(PATH + "users.dat","wb")
        users_dict={}
        pickle.dump(users_dict,f)
        f.close()
        
    if not os.path.exists(PATH+"books.dat"):
        f=open(PATH + "books.dat","rb")
        books_dict = {}
        pickle.dump(books_dict,f)
        f.close()

    if not os.path.exists(path + "borrows.dat"):
        f=open(PATH + "borrows.dat","wb")
        borrows_dict={}
        pickle.dump(borrows_dict,f)  
        f.close() 

def add_users(name,family,father_name,code,birthday):
    check_validation()
    
    f=open(PATH + "users.dat","rb")
    users_dict = pickle.load(f)
    f.close()

    user_id = len(users_dict)
    users_dict[user_id]=[name,family,father_name,code,birthday]

    f=open(PATH + "users.dat","wb")
    pickle.dump(users_dict,f)
    f.close()

    print("Welcome to our library ... your user id is : ",user_id)

def add_book(title,author,subject,year):
    check_validation()
    f=open(PATH+"books.dat","rb")
    books_dict=pickle.load(f)
    f.close()

    books_dict[title]=[author,subject,year]
    f=open(PATH,"books.dat","wb")
    pickle.dump(books_dict,f)
    f.close()

def search_book(title):
    check_validation()

    f=open(PATH+"book.dat","rb")
    books_dict = pickle.load(f)
    f.close()


    print(books_dict[title])


def borrow(user_id ,title):
    check_validation()

    f = open(PATH + "borrows.dat","rb")
    borrows_dict = pickle.load(f)
    f.close()

    borrows_dict[user_id]= title

    f=open(PATH + "borrows.dat","wb")
    pickle.dump(borrows_dict,f)
    f.close()

def show_all_info():
    check_validation()

    f=open(PATH + "users.dat","rb")
    users_dict = pickle.load(f)
    f.close()

    f=open(PATH +"books.dat","rb")
    books_dict = pickle.load(f)
    f.close()

    f=open(PATH + "borroes.dat","rb")
    borrows_dict = pickle.load(f)
    f.close()

    print(users_dict)
    print("________________________")
    print(books_dict)
    print("________________________")
    print(borrows_dict)


ch=1
while ch != 0:
    print("1-Add User\n2-Add new Book\n3-Search\n4-Borrow\n5-Show All\n0-Exit")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        name = input("Enter Name : ")
        family = input("Enter Family : ")
        father_name = input("Enter Father Name : ")
        code = input("Enter Nationalty Code : ")
        birthday = input("Enter BirthDay : ")

        add_users(name,family,father_name,code,birthday)

    elif ch == 2:
        title = input("Enter Title : ")
        author = input("Enter Author : ")
        subject = input("Enter Subject : ")
        year = input("Enter Year : ")

        add.book(title,author,subject,year)

    elif ch == 3:
        title = input("Enter Title : ")
        search_book(title)

    elif ch == 4:            
        user_id = input("Enter User Id :")
        title = input("Enter Title : ")
        borrow(user_id,title)     
    elif ch == 5:
        show_all_info()
   