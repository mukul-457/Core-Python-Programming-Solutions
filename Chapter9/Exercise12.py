from time import time as now, ctime
import getpass
import crypt


def show_admin_menu():
    menu = """
    [R]emove user 
    [S]how all user
    [E]xit

    Enter your Choice:"""
    chosen = 0
    while not chosen:
        choice = raw_input(menu).lower()
        if choice not in 'rse':
            print '\tinvalid option.'
        else:
            chosen = 1
    if choice == 'r': remove_user()
    if choice == 's': show_all()
    if choice == 'e': pass


def remove_user():
    name = raw_input("\nenter name of user to remove:")
    f = open('./UserData.txt', 'r')
    users = f.readlines()
    f.close()
    if name not in ''.join(users):
        print 'user does not exist'
        return
    f = open('./UserData.txt', 'w')
    for user in users:
        if name not in user:
            f.write(user)
    f.close()


def show_all():
    f = open('./UserData.txt', 'r')
    users = f.readlines()
    for user in users:
        print user
    f.close()


def new_user():
    f = open('./UserData.txt', 'a+')
    users = f.readlines()
    name = raw_input('enter user name:')
    for user in users:
        if name in user:
            print 'user name already taken'
            return
    pswd = getpass.getpass("Enter pass")
    cnfpswd = getpass.getpass("Confirm pass")
    if pswd == cnfpswd:
        user_line = name+':'+crypt.crypt(pswd, 'AB')+':'+ctime(now())+'\n'
        f.write(user_line)
        f.close()
        print 'user successfully added'
    else:
        print 'passwords did not match , try again'


def old_user():
    name = raw_input('enter user name:')
    f = open('./UserData.txt', 'r')
    users = f.readlines()
    f.close()
    if name not in ''.join(users):
        print 'user does not exist'
        return

    typed_pswd = getpass.getpass('enter password:')

    for user in users:
        if name in user:
            password = user.split(':')[1].strip()
            last_login = user.split(':')[2].strip()

    if password == crypt.crypt(typed_pswd, password):
        pass
    else:
        print 'wrong user id or password\nplease try again'
        return
    print 'welcome again', name
    print 'your last login was at:', last_login
    f = open('./UserData.txt', 'w')
    for user in users:
        if name not in user:
            f.write(user)
        else:
            f.write(name+':'+password+':'+ctime(now())+'\n')
    f.close()





def show_menu():
    menu = """
    [a]dmin
    [n]ew User
    [o]ld user
    [q]uit 

    Enter Choise:"""

    done = 0
    while not done:

        chosen = 0

        while not chosen:
            choice = raw_input(menu)

            if choice not in 'anoq':
                print 'invalid option . try again'
            else:
                chosen = 1

        if choice == 'n':
            new_user()
        if choice == 'o':
            old_user()
        if choice == 'a':
            show_admin_menu()
        if choice == 'q':
            done = 1


if __name__ == '__main__':
    f = open('./UserData.txt', 'r+')
    f.close()
    show_menu()
