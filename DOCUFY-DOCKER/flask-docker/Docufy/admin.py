from database import Database

class Admin:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def json(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def addAdmin(self):
        Database.insert(collection='admin', data=self.json())
    
    @staticmethod
    def getAdmin(query={}):
        return Database.find_one(collection='admin', query=query)