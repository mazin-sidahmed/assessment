class Database:

    def __init__(self, filename):
        self.dbfile = filename

    def save(self, id, name, price):
        raise NotImplementedError()

    def search(self, name):
        raise NotImplementedError()
    
    def delete(self, name):
        raise NotImplementedError()