import time as wait
from time import time, ctime


class MoneyFMT:

    def __init__(self, amount):
        if not (isinstance(amount, type(1)) or isinstance(amount, type(1.5))):
            raise TypeError('Please give integer or float as argument')
        self.monetaryAmount = amount
        self.cTime = self.aTime = self.mTime = time()

    def __bool__(self):
        if self.monetaryAmount == 0:
            return False
        else:
            return True

    def __repr__(self):
        self.aTime = time()
        return self.monetaryAmount

    def update(self, amount):
        self.monetaryAmount = amount
        self.mTime = time()

    def __str__(self):
        print "print is invoked"
        return '%s\nCTime=%s\nAtime=%s\nMTime=%s' % (self.dollarize(),
                                                     ctime(self.cTime), ctime(self.aTime), ctime(self.mTime))

    def dollarize(self):
        self.aTime = time()
        a, b = str(self.monetaryAmount).split('.')
        s1 = a[0:len(a) % 3]
        for i in range(len(a) % 3, len(a), 3):
            s1 = s1+','+a[i:i+3]
        s1 = s1 + '.' + b
        return '$' + s1


myMoney = MoneyFMT(314256.456)

if myMoney:
    print("inside")
    print(myMoney)

print('exclusive:')
print(myMoney)
wait.sleep(5)
myMoney.update(1245442.23)
print(myMoney)

