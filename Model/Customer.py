import Controller.CrudController
import json
import fileinput


class Customer:
    def __init__(self):
        self.CRUD = Controller.CrudController.CRUD("Customer.txt")

    def getCusts(self):
        custs=[]
        data = self.CRUD.readAll().split('\n')
        for i in data:
            parse = json.loads(i)
            custs.append(CustModel(parse['id'],parse['uid'],parse['nama'],parse['nik'],parse['simpanan'],parse['pinjaman']))
        return custs

    def getWhere(self,col,val):
        cust=[]
        data = self.CRUD.readAll().split('\n')
        for i in data:
            parse = json.loads(i)
            if parse[col]==val:
                 cust.append(CustModel(parse['id'],parse['uid'],parse['nama'],parse['nik'],parse['simpanan'],parse['pinjaman']))
        return cust

    def addCust(self,name,nik,simpanan=0):
        last = self.getCusts()
        buff = '{ "id":'+str(last[-1].id+1)+',"uid":"'+str(int(last[-1].uid.strip('\''))+3)+'","nama":"'+name+'","nik":"'+nik+'","simpanan":'+str(simpanan)+',"pinjaman":0 }'
        self.CRUD.Write(buff)
        return str(int(last[-1].uid.strip('\''))+3)

    def findRecord(self, col, value):
        data = self.CRUD.readAll().split('\n')
        pos =0
        for i in data:
            parsed = json.loads(i)
            if parsed[col] == value:
                return pos
            pos+=1

    def update(self,col,val,colu,vals):
        raw = self.CRUD.readAll()
        rw = raw.split('\n')
        row = self.findRecord(col,val)
        data = json.loads(rw[row])
        a = str(rw[row])
        old = '"'+colu+'":'+str(data[colu])
        new = '"'+colu+'":'+str(vals)
        a = a.replace(old,new)
        raw= raw.replace(old,new)
        self.CRUD.forceWrite(raw)


            

class CustModel:
    def __init__(self,id,acc, name,nik,simpanan, pinjaman):
        self.id = id
        self.uid = acc
        self.nama = name
        self.NIK = nik
        self.simpanan = simpanan
        self.pinjaman = pinjaman
