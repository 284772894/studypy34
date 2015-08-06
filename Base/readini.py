__author__ = 'Administrator'
import configparser
import Base.getDir
class baseReadnin():
    def __init__(self, init_file):
        config = configparser.ConfigParser()
        config.read(init_file)
        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']
    def set_host(self, host):
        self.host = host
    def get_host(self):
        return self.host
    def set_port(self, port):
        self.port = port
    def get_port(self):
        return self.port
# t = baseReadnin(Base.getDir.BaseGetPreDir('conf.ini')).get_host()

