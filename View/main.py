import Model.User
import Model.Transaction
import Model.Customer
import time, random, string, os, math
import locale
locale.setlocale(locale.LC_ALL, 'id_ID')

class View:
    def __init__(self, appname):
        self.appname = appname
        self.users = Model.User.User()
        self.customer = Model.Customer.Customer()
        self.transaction = Model.Transaction.Transactions()

    def auth(self,username,password):
        user = self.users.getWhere("username",username)
        if len(user)>0 and user[0].password == password:
            return {"id":user[0].id,"username":user[0].username,"level":user[0].level} #otentikasi return data kalo berhasil, kalo gagal return false
        else:
            return False

    def exit(self):
        # self.root.destroy()
        pass

    def splashScreen(self):
        pass

    def menuLister(self,title,menu = {}, container = "="*30):
        txt = ''
        txt += container + "\n"
        if title != None:  txt += title + "\n"
        for key,val in menu.items():
            txt += str(key).rjust(5) + " | " + str(val) + "\n"
        txt += container
        return txt

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # print(chr(27) + "[2J")

    def login(self):
        msg = "Login"
        username = str(input("Username: "))
        password = str(input("Password: "))
        auth = self.auth(username,password)
        if auth:
            print("Login success!")
            return auth
        else:
            print("Wrong credential given.")
            return False

    def getCustomer(self):
        cust = self.customer.getCusts()
        if len(cust)>0:
            return cust
        else:
            return False #return data nasabah kalo gaketemu return False

    def getTransaction(self):
        trx = self.transaction.getTrxs()
        if len(trx)>0:
            return trx
        else:
            return False #return data transaksi kalo gaketemu return False

    # Admininistrasi
    def registerNasabah(self):
        print("Reg Nasabah (siapkan Nama, NIK, Saldo Setoran Awal")
        nama = str(input("Nama: "))
        nik = str(input("NIK: "))
        saldo = int(input("Setoran awal: "))
        while saldo < 1000000:
            if saldo < 0:
                print("Maneh mabok?")
            else:
                print("Kurang boi")
            saldo = int(input("Setoran awal: "))
        query = self.customer.addCust(nama, nik, saldo)
        uid = self.customer.getCusts()[-1].uid
        self.transaction.addTrx(uid,0,saldo)
        if query:
            print("Nasabah berhasil didaftarkan")
            return True
        else:
            print("Nasabah gagal didaftarkan")
            return False

    def listNasabah(self):
        custs = self.customer.getCusts()
        print("List Nasabah")
        print("-"*150)
        print("|","Id".center(3),"|","Account".center(20),"|","Nama".center(30),"|","NIK".center(30),"|","Simpanan".center(30),"|","Pinjaman".center(30),"|",sep="")
        print("-"*150)
        for i in custs:
            print('|',str(i.id).center(3),'|',i.uid.center(20),'|', i.nama.center(30),'|', i.NIK.center(30),'|', str(i.simpanan).center(30),'|', str(i.pinjaman).center(30),'|',sep='')
        print("-"*150)
        return True

    def editNasabah(self):
        print("Edit Nasabah")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            nama = str(input("Nama: "))
            if nama != "":
                self.customer.update("uid",query,"nama",nama)
            nik = str(input("NIK: "))
            if nik != "":
                self.customer.update("uid",query,"nik",nik)
            #update
            print("Update data nasabah berhasil.")
            return True
        else:
            print("Gagal update data nasabah.")
            return False

    # Simpan
    def setorDuit(self):
        print("Setor Duit")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            saldo = abs(int(input("Jumlah duit: ")))
            saldo_awal = cust[0].simpanan
            saldo_akhir = saldo_awal + saldo
            self.transaction.addTrx(query,0,saldo)
            self.customer.update("uid",query,"simpanan",saldo_akhir)
            #update pake saldo akhir
            print("Setor saldo berhasil.")
            return True
        else:
            print("Setor saldo gagal.")
            return False

    def tarikDuit(self):
        print("Tarik Duit")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            saldo = abs(int(input("Jumlah duit: ")))
            saldo_awal = cust[0].simpanan
            saldo_akhir = saldo_awal - saldo
            if saldo_akhir<0:
                print("Saldo kurang")
                return False
            self.transaction.addTrx(query,0,(-1)*saldo)
            self.customer.update("uid",query,"simpanan",saldo_akhir)
            #update pake saldo akhir
            print("Tarik saldo berhasil.")
            return True
        else:
            print("Tarik saldo gagal.")
            return False

    def mutasiDuit(self):
        print("Mutasi Saldo")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)<=0:
            return False
        print("Account:",query)
        print("Nama   :",cust[0].nama)
        print("Saldo  :",cust[0].simpanan)
        data = self.transaction.getTrx(query,0)
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
                print('|',i.date.center(30),'|',locale.format_string("%d",i.value,True).ljust(25),'|',' '.center(25),'|',locale.format_string("%d", saldo, grouping=True).ljust(25),'|',sep='')
        print('-'*110)
        return True

    # Pinjam
    def ajukanPinjaman(self):
        print("Ajukan Pinjaman")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            if cust[0].pinjaman != 0:
                print("Anda masih memiliki pinjaman yang harus dilunasi")
                return False
            pinjaman = abs(int(input("Jumlah pinjaman: ")))
            print("biaya Admin: Rp.1.000.000")
            print("total bunga: Rp.",locale.format_string("%d",pinjaman*0.14,True),sep='')
            print("Total pinjaman: Rp.",locale.format_string("%d",pinjaman*1.14+1000000,True),sep='')
            print("Cicilan perbulan: Rp.",locale.format_string("%d",(pinjaman*1.14+1000000)/12,True),sep='')
            c ='a'
            while not (c=='y' or c=='n'):
                c = input("Ajukan? (y/n)")
            if c=='y':
                self.customer.update("uid",query,"pinjaman",int(pinjaman*1.14+1000000))
                self.transaction.addTrx(query,1,int(pinjaman*1.14+1000000))
                print("Pengajuan pinjaman berhasil.")
            return True
        else:
            print("Pengajuan pinjaman ditolak.")
            return False

    def bayarPinjaman(self):
        print("Bayar Pinjaman")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            print("Sisa tagihan: Rp.",locale.format_string("%d",cust[0].pinjaman,True),sep='')
            pinjaman = abs(int(input("Jumlah pembayaran: ")))
            pinjaman_awal = cust[0].pinjaman
            pinjaman_akhir = pinjaman_awal - pinjaman
            self.customer.update("uid",query,"pinjaman",int(pinjaman_akhir))
            self.transaction.addTrx(query,1,(-1)*pinjaman)
            print("Pembayaran pinjaman berhasil.")
            return True
        else:
            print("Pembayaran pinjaman ditolak.")
            return False

    def detailPinjaman(self):
        print("Lihat Pinjaman")
        query = str(input("ID: "))
        cust = self.customer.getWhere("uid",query)
        if len(cust)>0:
            sisa = 0
            print("Sisa tagihan anda: Rp.",locale.format_string("%d",cust[0].pinjaman,True),sep='')
            trxs = self.transaction.getTrx(query,1)
            print('-'*115)
            print('|','Tanggal'.center(30),'|','Jumlah'.center(30),'|','Sisa'.center(30),'|','Keterangan'.center(20),'|',sep='')
            print('-'*115)
            for trx in trxs:
                sisa += trx.value
                if trx.value<0:
                    print('|',trx.date.center(30),'|',locale.format_string("%d",-1*trx.value,True).ljust(30),'|',locale.format_string("%d",sisa,True).ljust(30),'|','Pebayaran'.ljust(20),'|',sep='')
                else:
                    print('|',trx.date.center(30),'|',locale.format_string("%d",trx.value,True).ljust(30),'|',locale.format_string("%d",sisa,True).ljust(30),'|','Pinjaman'.ljust(20),'|',sep='')
            print('-'*115)
            return True
        else:
            print("Record tidak ditemukan.")
            return False

    def changeUsername(self, id):
        print("Ubah Username")
        query = str(input("Masukan username baru: "))
        if query == "":
            return False
        user = self.users.getWhere("username",query)
        if len(user) > 0:
            print("Username sudah dipakai.")
            return False
        self.users.update("id",id,"username",query)
        print("Update username berhasil.")
        return True

    def changePassword(self, id):
        print("Ubah Password")
        old = str(input("Masukan password lama: "))
        new = str(input("Masukan password baru: "))
        re_new = str(input("Masukan password baru lagi: "))
        if new == "":
            return False
        user = self.users.getWhere("id",id)
        if len(user) > 0:
            if new == re_new and old == user[0].password:
                self.users.update("id",id,"password",new)
                print("Update password berhasil.")
                return True
        print("Update password gagal.")
        return False

    def listUsers(self):
        users = self.users.getUsers()
        print("List Users")
        print("-"*67)
        print("|","Id".center(3),"|","Username".center(30),"|","Level".center(30),"|",sep="")
        print("-"*67)
        for i in users:
            print('|',str(i.id).center(3),'|', i.username.center(30),'|', str(i.level).center(30),'|',sep="")
        print("-"*67)
        return True

    def registerUser(self):
        print("Reg User")
        username = str(input("Username: "))
        level = str(input("Level: "))
        pwd = str(input("Password: "))
        re_pwd = str(input("Re-password: "))
        if pwd != re_pwd:
            print('Password mismatch')
            return False
        if username == "":
            print('Username cannot be blank!')
            return False
        if level == "":
            print('Level cannot be blank!')
            return False
        if not level.isnumeric():
            print('Level must be a number!')
            return False
        level = int(level)
        exist = self.users.getWhere("username",username)
        if len(exist) > 0:
            print("Username already taken")
            return False
        query = self.users.addUser(username,pwd,level)
        print("User berhasil didaftarkan")
        return True

    def editUser(self, id):
        print("Edit User")
        query = int(input("ID: "))
        if query == id:
            print("Tolong ubah data anda pada setting.")
            return False
        user = self.users.getWhere("id",query)
        if len(user)>0:
            username = str(input("Username: "))
            if username != "":
                self.users.update("id",query,"username",username)
            pwd = str(input("Password: "))
            if pwd != "":
                self.users.update("id",query,"password",pwd)
            #update
            print("Update data user berhasil.")
            return True
        else:
            print("Gagal update data user.")
            return False

    def deleteUser(self, id):
        print("Delete User")
        query = int(input("ID: "))
        if query == id:
            print("Tidak dapat menghapus diri sendiri")
            return False
        user = self.users.getWhere("id",query)
        if len(user)>0:
            choice = None
            while choice == None or choice.lower() != "y" or choice.lower() != "n":
                choice = str(input("Are you sure (y/n): "))
                if choice.lower() == "y" or choice.lower() == "n":
                    break
            if choice.lower() == "y":
                #delete user
                print("Delete user berhasil.")
                return True
            else:
                print("Anda menggagalkan operasi delete user.")
                return False
        else:
            print("Gagal delete user.")
            return False