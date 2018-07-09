import pickle
import getpass
from time import time as now, ctime


class DataBase:

    def __init__(self):
        try:
            storage = open('./DataBase.pkl','rb')
            db = pickle.load(storage)
            self.users = db.users
            self.admin_id = db.admin_id
            self.admin_pass = db.admin_pass
            storage.close()
        except IOError:
            self.users = {}
            print 'Please set admin user for the database'
            self.admin_id = raw_input('admin id :')
            self.admin_pass = getpass.getpass('admin_pass:')

    def __del__(self):
        file_handle = open('./DataBase.pkl', 'wb')
        pickle.dump(self, file_handle)
        file_handle.close()
        self.done = 1

    def add_user(self):
        name = raw_input('user name:')
        if name not in self.users:
            pass
        else:
            print 'user name already taken'
            return
        password = getpass.getpass('Password:')
        confirm = getpass.getpass('re-enter:')
        if password == confirm:
            new_user = NewUser(name,password)
            self.users[name] = new_user
        else:
            print 'password did not match'

    def log_in(self):
        name = raw_input('login id/user name:')
        if name not in self.users:
            print 'user does not exist'
            return
        user = self.users[name]
        password = getpass.getpass('Password:')
        if password != user.password:
            print 'wrong password'
            return
        print 'Welcome back',user.name
        print 'your last login was at', ctime(user.last_login)
        user.last_login = now()

    def remove(self):
        user = raw_input('enter username to remove:')
        if user not in self.users:
            print 'user does not exist'
        else:
            del self.users[user]

    def show_all(self):
        for u in self.users.values():
            print 'id:%s, pass = %s, last_login=%s' % (
                u.name, u.password, ctime(u.last_login))


def admin(db):
    menu="""
    [R]emove
    [S]how_all
    
    Enter choice"""
    print 'please authenticate yourself as admin'
    id = raw_input('admin_id:')
    if id != db.admin_id:
        print "not admin ###"
        return
    pswd = getpass.getpass('admin_pass:')
    if pswd != db.admin_pass:
        print "incorrect password"

    print 'Welcome admin'

    chosen = 0
    while not chosen:
        choice = raw_input(menu)
        if choice not in 'sr':
            print ' in valid option'
        else:
            chosen =1
    if choice == 'r':
        db.remove()
    if choice == 's':
        db.show_all()


def start():
    menu = """
            [A]dmin
            [S]ign up
            [L]og in
            [Q]uit

            Enter your Choice"""
    DB = DataBase()
    DB.done = 0
    while not DB.done:
        chosen = 0
        while not chosen:
            choice = raw_input(menu).strip()[0].lower()
            if choice not in 'aslq':
                print '\tinvalid option'
            else:
                chosen = 1
        if choice == 's': DB.add_user()
        if choice == 'l': DB.log_in()
        if choice == 'a': admin(DB)
        if choice == 'q': DB.__del__()


class NewUser:
    def __init__(self,name, password):
        self.name = name
        self.password = password
        self.last_login = now()


if __name__ == '__main__':
    start()