from crypt import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key

#master_pwd = input("Type master password : ")
key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as w:
        for lines in w.readlines():
            data =lines.rstrip()
            user, password = data.split("|")
            print("User:",user+", password:",fer.decrypt(password.encode().decode()))
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('password.txt', 'a') as w:
        w.write(name+"|"+fer.encrypt(pwd.encode().decode())+"\n")
 
while True:
    mode = input("Add new password/view password/quit .Type add/view/q: ").lower()
    if mode=="q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else :
        print("Please enter the valid options!!!")
        continue