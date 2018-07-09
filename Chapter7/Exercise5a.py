from time import time as now, ctime
import getpass
import crypt

DB = {}


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
    if choice == 'r':remove_user()
    if choice == 's':show_all()
    if choice == 'e':pass


def remove_user():
    name = raw_input("\nenter name of user to remove:")
    if name not in DB:
        print 'user does not exist'
    else:
        del DB[name]


def show_all():
    print "User List:"
    for user in DB:
        print 'user: %s,  pass:%s , lastLogin: %s' % (user, DB[user][0], ctime(DB[user][1]))


def new_user():
    prompt = 'user name:'
    while 1:
        name = raw_input(prompt)
        if name in DB:
            print 'user name is already taken'
        else:
            break
    pswd = getpass.getpass("Enter pass")
    cnfpswd = getpass.getpass("Confirm pass")
    if pswd == cnfpswd:
        DB[name] = [crypt.crypt(pswd, 'AB')]
        DB[name].append(now())
    else:
        print 'passwords did not match , try again'


def old_user():
    name = raw_input('enter user name:')
    if name not in DB:
        print ' you are not existing customer'
        return
    typed_pswd = getpass.getpass('enter password:')

    if DB[name][0] == crypt.crypt(typed_pswd, DB[name][0]):
        pass
    else:
        print 'wrong user id or password\nplease try again'
        return
    print 'welcome again', name
    print 'your last login was at:', ctime(DB[name][1])
    DB[name][1] = now()


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


show_menu()
