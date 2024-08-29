from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("pasword.txt", "r") as f:
        for line in f.readline():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, ", Password: ",fer.decrypt(passw.encode).decode())

def add():
    name = input("account name: ")
    pwd = input("password: ")
    with open("password.txt", "a") as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input("would you like to add new password or view existing one (add / view): ")

    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode!")
        continue