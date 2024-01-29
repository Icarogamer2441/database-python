import sqlite3 as sq

db = "users.db"

conn = sq.connect(db)
cursor = conn.cursor()

print("do you have an account to login or not?")

while True:
    command = input("type 'exit' do exit, type 's' to create an account and type 'd' to delete an account: ")
    if command.lower() == "s":
        username = input("your username: ")
        password = input("your password: ")
        account = (username,password)

        cursor.execute("INSERT INTO users (username,password) VALUES (?, ?)",account)
        conn.commit()
    elif command.lower() == "exit":
        break
    elif command.lower() == "d":
        username = input("your username: ")
        password = input("your password: ")
        account = (username,password)

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", account)
        user = cursor.fetchone()

        if user:
            cursor.execute("DELETE FROM users WHERE username=? AND password=?", account)
            conn.commit()
            print("account deleted sucefully!")
        else:
            print("this account dont exists or the username o password is incorrect")
    else:
        username = input("your username: ")
        password = input("your password: ")
        login = (username,password)

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",login)
        user = cursor.fetchone()

        if user:
            if username.lower() == "admin":
                while True:
                    command = input("your admin commands. type 'exit' to exit: ")
                    if command.lower() == "exit":
                        break
                    else:
                        print("dont have admins commands, in the future i can add some!")
            else:
                print("sucefully loged in!")
                break
        else:
            print("incorrect login or account dont exists. please verify your password or username")

