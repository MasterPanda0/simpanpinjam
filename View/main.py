import Model.User
import Model.Transaction
import Model.Customer
import time
import random
import string
import locale
locale.setlocale(locale.LC_ALL, 'id_ID')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

def printmutasi(account, type):
    data = transactions.getTrx(account,type)
    bal = 0
    print("-"*110)
    print('|','Date'.center(30),'|','Debet'.center(25),'|','Kredit'.center(25),'|','Saldo'.center(25),'|',sep='')
    print('-'*110)
    saldo =0
    for i in data:
        saldo +=i.value
        if i.value<0:
            print('|',i.date.center(30),'|',' '*25,'|',locale.format_string("%d", abs(i.value), grouping=True).ljust(25),'|',locale.format_string("%d", saldo, grouping=True).ljust(25),'|',sep='')
        else:
            pass
            print('|',i.date.center(30),'|',locale.format_string("%d",i.value,True).ljust(25),'|',' '.center(25),'|',locale.format_string("%d", saldo, grouping=True).ljust(25),'|',sep='')
    print('-'*110)

tester = Model.User.User()
customers = Model.Customer.Customer()
transactions = Model.Transaction.Transactions()
uid = id_generator()
#print("UID:",uid)
#for i in range(20):
#    transactions.addTrx(uid,i%2,((-1)**i)*i**i)
#   time.sleep(1)

#printmutasi('GFPJQR',0)

customers.update("uid","13202358","pinjaman",123000)





