import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Alian Testing\\PycharmProjects\\alianhubTesting\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getInvalidUserEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getInvalidPassword():
        userpassword = config.get('common info', 'userpassword')
        return userpassword


    @staticmethod
    def getProjectName():
        projectname = config.get('common info', 'projectname')
        return projectname

    @staticmethod
    def getFirstName():
        firstname = config.get('common info', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getNewUserPassword():
        userpassword = config.get('common info', 'userpassword')
        return userpassword



