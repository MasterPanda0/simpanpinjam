import View.main
from pyfiglet import Figlet

class Router:
    def __init__(self, appname = "untitled" , interface = "cli",header = False):
        self.path = [0,0,0,0]
        self.appname = appname
        self.interface = interface
        self.enable_splash_screen = False
        self.header_enable = header
        self.session = None
        self.f = Figlet(font='slant')

    def initInterface(self):
        self.view = View.main.View(self.appname)
        if self.enable_splash_screen:
            self.view.splashScreen()
        self.welcome()
        pass

    def welcome(self):
       # print("Selamat datang di aplikasi",self.appname)
        print("Selamat datang di aplikasi")
        #print(self.f.renderText(self.appname))

    def printHeader(self):
        if self.header_enable:
            print(self.f.renderText(self.appname))

    def change_path(self,index,opt):
        self.path[index] = int(opt)

    def select_path(self, min, max, message, exception = []):
        select = ''
        while( select == '' or select < min or select > max or select in exception ):
            while( not select.isnumeric() and select != "-1" ):
                print(str(message))
                select = str(input("Pilihan anda: "))
            select = int(select)
        return select

    def pressToContinue(self):
        inp = None
        while(inp == None):
            inp = input("Press any key to continue..")
        self.view.cls()


    def go_to_root_menu(self, index):
        for i in range(index,len(self.path)):
            self.change_path(i,0)

    def handleRes(self,res,success,fail):
        if res:
            self.go_to_root_menu(success)
        else:
            self.go_to_root_menu(fail)

    def required_level(self,level):
        if self.session == None:
            return False
        if self.session['level'] < level:
            return False
        return True

    def listen(self):
        while self.path[0] > -1:
            if self.path[0] == 0:
                #Main menu
                if self.session == None : ln = "Login"
                else: ln = "Logout"
                self.printHeader()
                msg = self.view.menuLister('Menu Utama',{ 1:ln, 2:"Area User", 3:"User Manager", 4:"Setting", 5:"Exit" })
                self.change_path(0,self.select_path(0,5,msg))
                self.view.cls()
                continue

            elif self.path[0] == 1:
                #Login user / Logout user
                if self.session == None:
                    #Login
                    login = self.view.login()
                    if login:
                        self.session = login
                        self.change_path(0,0)
                        self.view.cls()
                    continue
                else:
                    print("Successfully logged out! Thank You!")
                    self.session = None
                    self.change_path(0,0) #back to main menu

            elif self.path[0] == 2:
                #Logged in user only
                if self.session == None:
                    print("Please log in first")
                    self.change_path(0,1)
                    self.view.cls()
                    continue
                #Otherwise continue
                if self.path[1] == 0:
                    # Main menu kedua
                    self.printHeader()
                    msg = self.view.menuLister('User Area Menu',{ -1:'..', 1:'Administrasi', 2:"Simpan", 3:"Pinjam", 4:"Exit App" })
                    self.change_path(1,self.select_path(-1,4,msg))
                    self.view.cls()
                    continue

                elif self.path[1] == 1:
                    #Administrasi
                    if self.path[2] == 0:
                        self.printHeader()
                        msg = self.view.menuLister('Administration Menu',{ -1:'..', 1:'Register Nasabah', 2:"List Nasabah", 3:"Edit Nasabah" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        self.view.cls()
                        continue
                    elif self.path[2] == 1:
                        #Register nasabah
                        self.printHeader()
                        res = self.view.registerNasabah()
                        self.handleRes(res,1,2)
                        self.view.cls()
                        continue
                    elif self.path[2] == 2:
                        #List Nasabah

                        if self.path[3] == 0:
                            self.printHeader()
                            msg = self.view.menuLister('Administration Menu',{-1: '..', 1: 'All', 2: "Sort Simpanan",3: "Sort Pinjaman"})
                            self.change_path(3, self.select_path(-1, 3, msg))
                            self.view.cls()
                            continue
                        elif self.path[3] == 1:
                            #all
                            self.printHeader()
                            res = self.view.listNasabah()
                            self.handleRes(res,2,3)
                            self.pressToContinue()
                            continue
                        elif self.path[3] == 2:
                            #sort simpanan
                            self.printHeader()
                            res = self.view.sortSimpanan()
                            self.handleRes(res,2,3)
                            self.pressToContinue()
                            continue
                        elif self.path[3] == 3:
                            #sort pinjaman
                            self.printHeader()
                            res = self.view.sortPinjaman()
                            self.handleRes(res,2,3)
                            self.pressToContinue()
                            continue
                        elif self.path[3] == -1:
                            #up
                            self.go_to_root_menu(2)

                    elif self.path[2] == 3:
                        #Edit Nasabah
                        self.printHeader()
                        if not self.required_level(3):
                            print("Unauthorized")
                            self.go_to_root_menu(2)
                            continue
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
                        self.printHeader()
                        msg = self.view.menuLister('Simpan Uang Menu',{ -1:'..', 1:'Setor', 2:"Tarik", 3:"Mutasi" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        self.view.cls()
                        continue
                    elif self.path[2] == 1:
                        #Setor
                        self.printHeader()
                        res = self.view.setorDuit()
                        self.handleRes(res,1,2)
                        self.view.cls()
                        continue
                    elif self.path[2] == 2:
                        #Tarik
                        self.printHeader()
                        res = self.view.tarikDuit()
                        self.handleRes(res,1,2)
                        self.view.cls()
                        continue
                    elif self.path[2] == 3:
                        #Mutasi
                        self.printHeader()
                        res = self.view.mutasiDuit()
                        self.handleRes(res,1,2)
                        self.pressToContinue()
                        continue
                    elif self.path[2] == -1:
                        #go to main menu
                        self.view.cls()
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == 3:
                    #pinjam uang
                    if self.path[2] == 0:
                        self.printHeader()
                        msg = self.view.menuLister('Pinjam Uang Menu',{ -1:'..', 1:'Ajukan Pinjaman', 2:"Bayar Pinjaman", 3:"Detail Pinjaman" })
                        self.change_path(2,self.select_path(-1,3,msg))
                        self.view.cls()
                        continue
                    elif self.path[2] == 1:
                        #Ajukan
                        self.printHeader()
                        res = self.view.ajukanPinjaman()
                        self.handleRes(res,1,2)
                        self.view.cls()
                        continue
                    elif self.path[2] == 2:
                        #Bayar pinjaman
                        self.printHeader()
                        res = self.view.bayarPinjaman()
                        self.handleRes(res,1,2)
                        self.view.cls()
                        continue
                    elif self.path[2] == 3:
                        #Detail pinjaman
                        self.printHeader()
                        res = self.view.detailPinjaman()
                        self.handleRes(res,1,2)
                        self.pressToContinue()
                        continue
                    elif self.path[2] == -1:
                        #go to main menu
                        self.view.cls()
                        self.change_path(2,0) #reset path
                        self.change_path(1,0) #back to main menu kedua
                        continue

                elif self.path[1] == -1:
                    #go to main menu
                    self.view.cls()
                    self.change_path(1,0) #reset path
                    self.change_path(0,0) #back to main menu
                    continue

                elif self.path[1] == 4:
                    #Exit Application
                    self.change_path(0,-1) #exit app
                    break

            elif self.path[0] == 3:
                #User Manager
                #Logged in user only
                if self.session == None:
                    print("Please log in first")
                    self.change_path(0,1)
                    self.view.cls()
                    continue

                if not self.required_level(3):
                    print("Unauthorized")
                    self.go_to_root_menu(0)
                    continue

                if self.path[1] == 0:
                    self.printHeader()
                    msg = self.view.menuLister('User Manager', {-1: '..', 1: 'List User', 2: "Register User", 3: "Edit User", 4: "Delete User"})
                    self.change_path(1, self.select_path(-1, 4, msg))
                    self.view.cls()
                    continue
                elif self.path[1] == 1:
                    # List User
                    self.printHeader()
                    res = self.view.listUsers()
                    self.handleRes(res, 0, 1)
                    self.pressToContinue()
                    continue
                elif self.path[1] == 2:
                    # Register User
                    self.printHeader()
                    res = self.view.registerUser()
                    self.handleRes(res, 0, 1)
                    self.pressToContinue()
                    self.view.cls()
                    continue
                elif self.path[1] == 3:
                    # Edit User
                    self.printHeader()
                    res = self.view.editUser(self.session['id'])
                    self.handleRes(res, 0, 1)
                    continue
                elif self.path[1] == 4:
                    # Delete User
                    self.printHeader()
                    res = self.view.deleteUser(self.session['id'])
                    self.handleRes(res, 0, 1)
                    continue
                elif self.path[1] == -1:
                    # go to main menu
                    self.change_path(1,0) #reset path
                    self.change_path(0,0) #back to main menu
                    continue

            elif self.path[0] == 4:
                #User setting
                #Logged in user only
                if self.session == None:
                    print("Please log in first")
                    self.change_path(0,1)
                    self.view.cls()
                    continue

                if self.path[1] == 0:
                    self.printHeader()
                    msg = self.view.menuLister('User Setting', {-1: '..', 1: 'Ganti Username', 2: "Ganti Password"})
                    self.change_path(1, self.select_path(-1, 2, msg))
                    self.view.cls()
                    continue
                elif self.path[1] == 1:
                    # c username
                    self.printHeader()
                    res = self.view.changeUsername(self.session['id'])
                    self.handleRes(res, 0, 1)
                    continue
                elif self.path[1] == 2:
                    # c pwd
                    self.printHeader()
                    res = self.view.changePassword(self.session['id'])
                    self.handleRes(res, 0, 1)
                    continue
                elif self.path[1] == -1:
                    # go to main menu
                    self.change_path(1,0) #reset path
                    self.change_path(0,0) #back to main menu
                    continue

            elif self.path[0] == 5:
                #Exit Application
                self.change_path(0,-1) #exit app
                break
