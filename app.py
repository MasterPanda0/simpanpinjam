import configparser
import locale
locale.setlocale(locale.LC_ALL, 'id_ID')
import Router

class App:
    def __init__(self):
        #config
        self.config = configparser.ConfigParser()
        self.config_dir = 'config.INI'
        self.config.read(self.config_dir)
        self.interface_mode = self.config['DEFAULT']['interface_mode']
        self.app_name = self.config['DEFAULT']['app_name']
        self.head = self.config['DEFAULT']['header_en']

        #init
        self.route = Router.Router(self.app_name, self.interface_mode,self.head)

    def updateConfig(self):
        self.config.read(self.config_dir)
        self.interface_mode = self.config['DEFAULT']['interface_mode']


def main():
    app = App()
    app.route.initInterface()
    app.route.listen()


if __name__ == '__main__':
    main()
