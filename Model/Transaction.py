import Controller.CrudController
import json
import fileinput
from datetime import datetime


class Transactions:
    def __init__(self):
        self.CRUD = Controller.CrudController.CRUD("Transaction.txt")
        self.now = datetime.now()

    def getTrxs(self):
        trxs=[]
        data = self.CRUD.readAll().split('\n')
        for i in data:
            parse = json.loads(i)
            trxs.append(TransactionModel(parse['id'],parse['date'],parse['account'],parse['type'],parse['value']))
        return trxs

    def getTrx(self,acc,type):
        trxs=[]
        data = self.CRUD.readAll().split('\n')
        for i in data:
            parse = json.loads(i)
            if parse['account']==acc and parse['type']==type:
                trxs.append(TransactionModel(parse['id'],parse['date'],parse['account'],parse['type'],parse['value']))
        return trxs

    def addTrx(self,account,type,value):
        last = self.getTrxs()
        buff = '{ "id":'+str(last[-1].id+1)+',"date":"'+self.now.strftime("%d/%m/%Y %H:%M:%S")+'","account":"'+account+'","type":'+str(type)+',"value":'+str(value)+' }'
        self.CRUD.Write(buff)

            

class TransactionModel:
    def __init__(self,id,date, account,typ, value):
        self.id = id
        self.date = date
        self.account=account
        self.typ = typ #1->tabungan, 2->pinjaman
        self.value = value #+:debit #-: kredit
