import json
import sqlite3

def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        publisher TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def read_user_file():
    users = set()
    with open('user.csv', 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            users.add((username, password))
    return users



def read_books_file(filename='books.json'):
    books_data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    return books_data

def insert_users(users):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    for user in users:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', user)

    conn.commit()
    conn.close()

def insert_books(books):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    for book in books:
        cursor.execute('INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)',
                       (book['title'], book['author'], book['publisher'], book['year']))

    conn.commit()
    conn.close()

def main_menu():
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
    return choice
