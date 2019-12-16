import View.main

class Router:
    def __init__(self, appname = "untitled", interface = "cli"):
        self.path = [0,0,0]
        self.appname = appname
        self.interface = interface
        self.enable_splash_screen = False
        self.session = None

    def initInterface(self):
        self.view = View.main.View(self.appname)
        if self.enable_splash_screen:
            self.view.splashScreen()
        self.welcome()
        pass

    def welcome(self):
        print("Selamat datang di aplikasi",self.appname)

    def change_path(self,index,opt):
        self.path[index] = int(opt)

    def select_path(self, min, max, message, exception = []):
        select = None
        while( select == None or select < min or select > max or select in exception ):
            print(str(message))
            select = int(input("Pilihan anda: "))
        return select

    def go_to_root_menu(self, index):
        for i in range(index,len(self.path)):
            self.change_path(i,0)

    def handleRes(self,res,success,fail):
        if res:
            self.go_to_root_menu(success)
        else:
            self.go_to_root_menu(fail)

    def listen(self):
        while self.path[0] > -1:
            if self.path[0] == 0:
                #Main menu
                if self.session == None : ln = "Login"
                else: ln = "Logout"
                msg = self.view.menuLister('Menu Utama',{ 1:ln, 2:"Area User", 3:"Exit" })
                self.change_path(0,self.select_path(0,3,msg))
                continue

            elif self.path[0] == 1:
                #Login user / Logout user
                if self.session == None:
                    #Login
                    login = self.view.login()
                    if login:
                        self.session = login
                        self.change_path(0,2)
                    continue
                else:
                    print("a")
                    self.session = None
                    self.change_path(0,0) #back to main menu

            elif self.path[0] == 2:
                #Logged in user only
                if self.session == None:
                    print("Please log in first")
                    self.change_path(0,1)
                    continue
                #Otherwise continue
                if self.path[1] == 0:
                    # Main menu kedua
                    msg = self.view.menuLister('User Area Menu',{ -1:'..', 1:'Administrasi', 2:"Simpan", 3:"Pinjam", 4:"Transaksi" })
                    self.change_path(1,self.select_path(-1,5,msg))
                    continue

                elif self.path[1] == 1:
                    #Administrasi
                    if self.path[2] == 0:
                        msg = self.view.menuLister('Administration Menu',{ -1:'..', 1:'Register Nasabah', 2:"List Nasabah", 3:"Edit Nasabah" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        continue
                    elif self.path[2] == 1:
                        #Register nasabah
                        res = self.view.registerNasabah()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 2:
                        #List Nasabah
                        res = self.view.listNasabah()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 3:
                        #Edit Nasabah
                        res = self.view.editNasabah()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == -1:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == 2:
                    #Simpan uang
                    if self.path[2] == 0:
                        msg = self.view.menuLister('Simpan Uang Menu',{ -1:'..', 1:'Setor', 2:"Tarik", 3:"Mutasi" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        continue
                    elif self.path[2] == 1:
                        #Setor
                        res = self.view.setorDuit()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 2:
                        #Tarik
                        res = self.view.tarikDuit()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 3:
                        #Mutasi
                        res = self.view.mutasiDuit()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == -1:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == 3:
                    #pinjam uang
                    if self.path[2] == 0:
                        msg = self.view.menuLister('Pinjam Uang Menu',{ -1:'..', 1:'Ajukan Pinjaman', 2:"Bayar Pinjaman", 3:"Detail Pinjaman" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        continue
                    elif self.path[2] == 1:
                        #Ajukan
                        res = self.view.ajukanPinjaman()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 2:
                        #Bayar pinjaman
                        res = self.view.bayarPinjaman()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == 3:
                        #Detail pinjaman
                        res = self.view.detailPinjaman()
                        self.handleRes(res,1,2)
                        continue
                    elif self.path[2] == -1:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == 4:
                    #Transaksi
                    if self.path[2] == 0:
                        msg = self.view.menuLister('Cari Transaksi',{ -1:'..', 1:'Cari bedasarkan ID', 2:"Apa", 3:"Apa" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        continue
                    elif self.path[2] == 1:
                        #Ajukan
                        pass
                    elif self.path[2] == 2:
                        #Bayar pinjaman
                        pass
                    elif self.path[2] == 3:
                        #Detail pinjaman
                        pass
                    elif self.path[2] == -1:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == -1:
                    #go to main menu
                    self.change_path(1,0) #reset path
                    self.change_path(0,0) #back to main menu
                    continue

                elif self.path[1] == 5:
                    #Exit Application
                    self.change_path(0,-1) #exit app
                    break

            elif self.path[0] == 3:
                #Exit Application
                self.change_path(0,-1) #exit app
                break
