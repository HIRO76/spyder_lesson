import time
import os 
import csv 
import platform

with open("books.cvs", encoding="utf-8")as fp:
    books = list(csv.reader(fp))

# 本を登録する
def add_book():
    ID = input("Enter ID: ")
    title = input("Enter title: ")
    price = input("Enter price: ")
    memo = input("Enter memo: ")
    print()
    print("About to add new book")
    print("-----------")
    print("ID:", ID)
    print("Title:", title)
    print("Price:", price)
    print("Memo:", memo)
    print("-----------")
    
    if get_confirm():
        if len(b for b in books if b[0]==ID) == 0:
            books.append([ID, title, price, memo])
            print("Entry added")
        else:
            print(f"ERROR!! ID: {ID} already exeists")
    
    get_return()
    return 

# 指定されたIDの書籍データを削除
def remove_book():
    print("remove book")
    global books
    
    ID = input("Enter ID to remove: ")
    
    try:
        book = [b for b in books if b[0]==ID][0]
    except IndexError:
        print("There is no book")
    else:
        print()
        print("You are about to remove\n")
        print("----------")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Price: {book[2]}")
        print(f"Memo: {book[3]}")
        print("----------")
        
        if get_confirm():
            books = [b for b in books if b[0]!=ID]
            print("Entry removed\n")
            
    get_return()
    return
     
# 指定された書籍データを更新する   
def update_book():
    print("update_book")
    global books
    
    ID = input("Enter ID to update: ")
    
    try:
        books = [b for b in books if b[0]==ID][0]
    except IndexError:
        print("There is no book")
    else:
        print()
        print("You are about to update\n")
        print("-----------")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Price: {book[2]}")
        print(f"Memo: {book[3]}")
        print("-----------")
    
    if get_confirm():
        title = input("Enter new Title: ")
        price = input("Enter new Price: ")
        memo = input("Enter new Memo: ")
        
        print()
        print("About to update")
        print("-----------")
        print(f"ID: {ID}")
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Memo: {memo}")
        print("-----------")
        
        if get_confirm():
            books = [b for b in books if b[0]!=ID]
            books.append([ID, title, price, memo])
            print("Entry updated")
            
    get_return()
    return

# 書籍リストを表示
def list_book():
    if len(books) == 0:
        print("There is no book")
    else:
        print()
        print(f"{%^4ID}{%^6price}{title}")
        print("----------")
        for book in books:
            print(f"{%>4book[0]}{%>6,d int(book[2])}{book[1]}")
        print()
        
    get_return()
    return

# 指定された書籍データを表示
def show_book():
    ID = input("Enter ID: ")
    try:
        book = [b for b in books if b[0]==ID][0]
    except IndexError:
        print("There is no book")
    else:
        print("---------")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Price: {book[2]}")
        print(f"Memo: {book[3]}")
        print("---------")
    
    get_return()
    return 


# 書籍データを保存する
def save_changes():
    while True():
        print("Save changes?: ", end="")
        x = input()
        if x in ["y", "yes", "Y", "Yes", "YES"]:
            with open("books.csv", "w", encoding="utf-8")as fp:
                writer = csv.writer(fp, lineterminatr="\n")
                writer.writerows(books)
            print("Changes saved")
            time.sleep(1)
            return 
        elif x in ["n", "no", "N", "No", "NO"]:
            print("Changes discarded")
            time.sleep(1)
            return
        else:
            print("input y or n : ", end="")
            time.sleep(1)
    
# pless returnを表示してenterの入力待ち
def get_return():
    return input("Pless return ")

# Are you sure?を表示してy or nの入力待ち
def get_confirm():
    while True:
        x = input("Are you sure?: ")
        if x in ["y", "yes", "Y", "Yes", "YES"]:
            return True
        if x in ["n", "no", "N", "No", "NO"]:
            return False
        print("Please enter yes or no: ", end="")
        time.sleep(1)    

# ターミナル画面をクリアする
def clear_screen(): 
    if platform.system() == "Windows":
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux or mac

# メニュー選択
def set_menu_choice():
    clear_screen()
    print("Options: ")
    print()
    print(" a) Add new book")
    print(" l) List book")
    print(" r) Remove book")
    print(" u) Update book")
    print(" s) Show book")
    print(" q) Quit")
    print()
    ret = input("Please enter choice then press return: ")
    return ret

# はじめに実行される関数
def main():
    clear_screen()
    print()
    print()
    print("Mini Book manager")
    
    time.sleep(1)
    
    quit = "n"
    while quit != "y":
        ret = set_menu_choice()
        if ret == "a":
            add_book()
        elif ret == "r":
            remove_book()
        elif ret == "u":
            update_book()
        elif ret == "l":
            list_book()
        elif ret == "s":
            show_book()
        elif ret == "q" or ret == "Q":
            print(books)
            save_changes()
            quit = "y"
        else:
            print("Sorry. choice not recognized")
            time.sleep(1)
            
if __name__ == "__main__":
    main()
            
        