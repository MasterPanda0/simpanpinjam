import Model.User
import Model.Transaction
import Model.Customer
import time, random, string, os, math

class View:
    def __init__(self, appname):
        self.appname = appname

    def auth(self,username,password):
        return {"username":username} #otentikasi return data kalo berhasil, kalo gagal return false

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
        return False
        pass #return data nasabah kalo gaketemu return False

    def getTransaction(self):
        return False
        pass #return data transaksi kalo gaketemu return False

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
        query = True #insert
        if query:
            print("Nasabah berhasil didaftarkan")
            return True
        else:
            print("Nasabah gagal didaftarkan")
            return False

    def listNasabah(self):
        print("List Nasabah")
        return True

    def editNasabah(self):
        print("Edit Nasabah")
        query = str(input("ID/Nama: "))
        #query didieu cari aya teu baru edit
        ada = self.getCustomer(query)
        if ada:
            nama = str(input("Nama: "))
            nik = str(input("NIK: "))
            #update
            print("Update saldo data nasabah.")
            return True
        else:
            print("Gagal update data nasabah.")
            return False

    # Simpan
    def setorDuit(self):
        print("Setor Duit")
        query = str(input("ID: "))
        ada = self.getCustomer(query)
        if ada:
            saldo = math.abs(int(input("Jumlah duit: ")))
            saldo_awal = 0 #query saldo dr db
            saldo_akhir = saldo_awal + saldo
            #update pake saldo akhir
            print("Setor saldo berhasil.")
            return True
        else:
            print("Setor saldo gagal.")
            return False

    def tarikDuit(self):
        print("Tarik Duit")
        query = str(input("ID: "))
        ada = self.getCustomer(query)
        if ada:
            saldo = math.abs(int(input("Jumlah duit: ")))
            saldo_awal = 0 #query saldo dr db
            saldo_akhir = saldo_awal - saldo
            #update pake saldo akhir
            print("Tarik saldo berhasil.")
            return True
        else:
            print("Tarik saldo gagal.")
            return False

    def mutasiDuit(self):
        print("Tarik Duit")
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
