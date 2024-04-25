import json
import pack.modu as lib

def login():
    while True:
        username = input("請輸入帳號：")
        password = input("請輸入密碼：")
        users = lib.read_user_file()
        if (username, password) in users:
            return True
        else:
            print("帳號或密碼錯誤，請重新輸入。")
def display_books(books_data):
    print("|　　　　　　書名　　　　　　|　　　　　　作者　　　　　　|　　　　　　　出版社　　　　　　　　|年份|")
    for book in books_data:
        print(f"|{book['title']:{chr(12288)}<14}|{book['author']:{chr(12288)}<14}|{book['publisher']:{chr(12288)}<18}|{book['year']}|")

def main():
    lib.create_database()
    books_data = lib.read_books_file()
    lib.insert_books(books_data)

    if login():
        while True:
            print("-------------------")
            print("    資料表 CRUD")
            print("-------------------")
            print("    1. 增加記錄")
            print("    2. 刪除記錄")
            print("    3. 修改記錄")
            print("    4. 查詢記錄")
            print("    5. 資料清單")
            print("-------------------")
            choice = input("選擇要執行的功能(Enter離開)：")
            if choice == '1':
                title = input("請輸入要新增的標題：")
                author = input("請輸入要新增的作者：")
                publisher = input("請輸入要新增的出版社：")
                year = input("請輸入要新增的年份：")
                if title and author and publisher and year:
                    new_book = {'title': title, 'author': author, 'publisher': publisher, 'year': year}
                    books_data.append(new_book)
                    lib.insert_books([new_book])
                    print("異動 1 記錄")
                    display_books(books_data)
                    with open('books.json', 'w', encoding='utf-8') as file:
                        json.dump(books_data, file, ensure_ascii=False, indent=2)
                else:
                    print("給定的條件不足，無法進行新增作業")
            elif choice == '2':
                print("執行刪除記錄功能")
                display_books(books_data)
                book_title = input("請問要刪除哪一本書？：")

                deleted = False
                for book in books_data:
                    if book['title'] == book_title:
                        books_data.remove(book)
                        deleted = True
                        break

                if deleted:
                    print("異動 1 記錄")
                    display_books(books_data)
                    with open('books.json', 'w', encoding='utf-8') as file:
                        json.dump(books_data, file, ensure_ascii=False, indent=2)
                else:
                    print("給定的條件不足，無法進行刪除作業")
            elif choice == '3':
                print("執行修改記錄功能")
                display_books(books_data)
                title_to_modify = input("請問要修改哪一本書的標題？：")
                matched_books = [book for book in books_data if book['title'] == title_to_modify]
                if matched_books:
                    new_title = input("請輸入要更改的標題：")
                    new_author = input("請輸入要更改的作者：")
                    new_publisher = input("請輸入要更改的出版社：")
                    new_year = input("請輸入要更改的年份：")
                    if new_title and new_author and new_publisher and new_year:
                        for book in matched_books:
                            book['title'] = new_title
                            book['author'] = new_author
                            book['publisher'] = new_publisher
                            book['year'] = new_year
                        print("異動 1 記錄")
                        display_books(books_data)
                        with open('books.json', 'w', encoding='utf-8') as file:
                            json.dump(books_data, file, ensure_ascii=False, indent=2)
                    else:
                        print("給定的條件不足，無法進行修改作業")
                else:
                    print("找不到要修改的書籍。")
            elif choice == '4':
                keyword = input("請輸入想查詢的關鍵字：")
                matched_books = [book for book in books_data if keyword in book['title'] or keyword in book['author']]
                if matched_books:
                    display_books(books_data)
                else:
                    print("找不到符合條件的記錄。")
            elif choice == '5':
                print("執行資料清單功能")
                display_books(books_data)
            elif choice == '':
                break
            else:
                print("無效的選擇")

if __name__ == "__main__":
    main()
