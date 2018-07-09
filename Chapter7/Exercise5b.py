from time import time as now, ctime
import getpass
import crypt
import pickle


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
    fh = open('./Data.pkl', 'rb')
    user_dict = pickle.load(fh)
    fh.close()
    if name not in user_dict:
        print 'user does not exist'
    else:
        del user_dict[name]
        fh = open('./Data.pkl', 'wb')
        pickle.dump(user_dict, fh)
        fh.close()


def show_all():
    print "User List:"
    fh = open('./Data.pkl','rb')
    user_dict = pickle.load(fh)
    for user in user_dict:
        print 'user: %s,  pass:%s , lastLogin: %s' % (user, user_dict[user][0], ctime(user_dict[user][1]))


def new_user():
    fh = open('./Data.pkl', 'rb+')
    user_dict = pickle.load(fh)
    fh.close()
    name = raw_input('user name:')
    if name in user_dict:
        print 'user name is already taken'
        return
    pswd = getpass.getpass("Enter pass")
    cnfpswd = getpass.getpass("Confirm pass")
    if pswd == cnfpswd:
        user_dict[name] = [crypt.crypt(pswd, 'AB')]
        user_dict[name].append(now())
        fh = open('./Data.pkl', 'wb')
        pickle.dump(user_dict,fh)
        fh.close()
    else:
        print 'passwords did not match , try again'


def old_user():
    name = raw_input('enter user name:')
    fh = open('./Data.pkl', 'rb')
    user_dict = pickle.load(fh)
    fh.close()
    if name not in user_dict:
        print ' you are not existing customer'
        return
    typed_pswd = getpass.getpass('enter password:')

    if user_dict[name][0] == crypt.crypt(typed_pswd, user_dict[name][0]):
        pass
    else:
        print 'wrong user id or password\nplease try again'
        return
    print 'welcome again', name
    print 'your last login was at:', (user_dict[name][1])
    user_dict[name][1] = now()
    fh = open('./Data.pkl', 'wb')
    pickle.dump(user_dict, fh)
    fh.close()


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
    fh = open('./Data.pkl', 'rb')
    try:
        data = pickle.load(fh)
        fh.close()
    except EOFError:
        fh.close()
        fh = open('/Data.pkl', 'wb')
        dict = {}
        pickle.dump(dict, fh)
        fh.close()
    show_menu()
