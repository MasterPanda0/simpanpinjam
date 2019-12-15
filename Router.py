import View

class Router:
    def __init__(self, appname = "untitled", interface = "CLI"):
        self.path = [0,0,0]
        self.appname = appname
        self.interface = interface
        self.enable_splash_screen = False
        self.session = None

    def initInterface(self):
        self.view = View()
        if self.enable_splash_screen:
            pass
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

    def listen(self):
        while self.path[0] > -1:
            if self.path[0] == 0:
                #Main menu
                msg = "Pilihan"
                self.change_path(0,self.select_path(0,3,msg))

            elif self.path[0] == 1:
                #Login user / Logout user
                if self.session == None:
                    #Login
                    msg = "Login"
                    #self.change_path(0,self.select_path(-1,3,msg))
                else:
                    print("a")
                    self.change_path(0,0) #back to main menu

            elif self.path[0] == 2:
                #Logged in user only
                if self.session == None:
                    print("Please log in first")
                    continue
                #Otherwise continue
                if self.path[1] == 0:
                    # Main menu kedua
                    msg = "Pilih menu"
                    self.change_path(1,self.select_path(-1,5,msg))
                    continue

                elif self.path[1] == 1:
                    #Administrasi
                    if self.path[2] == 0:
                        msg = "Pilih menu"
                        self.change_path(2,self.select_path(0,4,msg))
                        continue
                    elif self.path[2] == 1:
                        #Register nasabah
                        pass
                    elif self.path[2] == 2:
                        #List Nasabah
                        pass
                    elif self.path[2] == 2:
                        #Edit Nasabah
                        pass
                    elif self.path[2] == 4:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua

                elif self.path[1] == 2:
                    #Simpan uang
                    if self.path[2] == 0:
                        msg = "Pilih menu"
                        self.change_path(2,self.select_path(0,4,msg))
                        continue
                    elif self.path[2] == 1:
                        #Setor
                        pass
                    elif self.path[2] == 2:
                        #Tarik
                        pass
                    elif self.path[2] == 2:
                        #Mutasi
                        pass
                    elif self.path[2] == 4:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua

                elif self.path[1] == 3:
                    #pinjam uang
                    if self.path[2] == 0:
                        msg = "Pilih menu"
                        self.change_path(2,self.select_path(0,4,msg))
                        continue
                    elif self.path[2] == 1:
                        #Ajukan
                        pass
                    elif self.path[2] == 2:
                        #Bayar pinjaman
                        pass
                    elif self.path[2] == 2:
                        #Detail pinjaman
                        pass
                    elif self.path[2] == 4:
                        #go to main menu
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua

                elif self.path[1] == 4:
                    #Transaksi
                    pass

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
