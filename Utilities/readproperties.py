import configparser
config = configparser.RawConfigParser()
config.read("/Users/riyabakoria/OrganixmantraAPP/Configurations/config.ini")    # Path of the config file

class ReadConfig:
    @staticmethod
    def get_useremail():
        useremail = config.get('commondata','useremail')
        return useremail
    @staticmethod
    def get_password(): 
        password = config.get('commondata','password')
        return password