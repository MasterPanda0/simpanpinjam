import os
import fileinput

class CRUD:
    def __init__(self,file):
        self.f_dir = os.path.abspath('./')+'\DB\\'
        self.file=self.f_dir+file

    def readAll(self):
        f = open(self.file,'r+')
        data = f.read()
        f.close()
        return data
    
    def forceWrite(self,args):
        f = open(self.file,'w+')
        f.write(args)
        f.close()

    def Write(self,args):
        f= open(self.file,'a+')
        f.write("\n"+args)
        f.close()

  
   