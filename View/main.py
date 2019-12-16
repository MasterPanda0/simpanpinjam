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
            return {"username":user[0].username} #otentikasi return data kalo berhasil, kalo gagal return false
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
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(chr(27) + "[2J")

    def login(self):
        msg = "Login"
        username = str(input("Username: "))
        password = str(input("Password: "))
        auth = self.auth(username,password)
        if auth:
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
            nik = str(input("NIK: "))
            #update
            self.customer.update("uid",query,"nama",nama)
            self.customer.update("uid",query,"nik",nik)
            print("Update saldo data nasabah.")
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
        ada = self.getCustomer(query)
        if ada:
            print("Sisa tagihan: ")
            pinjaman = math.abs(int(input("Jumlah pinjaman: ")))
            pinjaman_awal = 0 #query saldo dr db
            pinjaman_akhir = pinjaman_awal + pinjaman
            #update pake pinjaman akhir
            print("Pengajuan pinjaman berhasil.")
            return True
        else:
            print("Pengajuan pinjaman ditolak.")
            return False

    def bayarPinjaman(self):
        print("Bayar Pinjaman")
        query = str(input("ID: "))
        ada = self.getCustomer(query)
        if ada:
            print("Sisa tagihan: ")
            pinjaman = math.abs(int(input("Jumlah pembayaran: ")))
            pinjaman_awal = 0 #query saldo dr db
            pinjaman_akhir = pinjaman_awal + pinjaman
            #update pake pinjaman akhir
            print("Pembayaran pinjaman berhasil.")
            return True
        else:
            print("Pembayaran pinjaman ditolak.")
            return False

    def detailPinjaman(self):
        print("Lihat Pinjaman")
        query = str(input("ID: "))
        ada = self.getCustomer(query)
        if ada:
            print("Sisa tagihan anda: ")
            return True
        else:
            print("Record tidak ditemukan.")
            return False
