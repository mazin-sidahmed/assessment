from src.modules.database import Database

class BaseItem(Database):
    def __init__(self, filename):
        super().__init__(filename)
    
    def save(self, id, name, price):

        with open(self.dbfile, 'a+') as instance: 
            instance.write("%s, %s, %s\n"%(id, name, price))

    def search(self, name):
        results = []
        with open(self.dbfile, 'r') as instance:
            lines = instance.readlines()
            for line in lines:
                if name in line.strip("\n"):
                    results.append(line)
        return results

    def delete(self, id):
        content = []
        with open(self.dbfile, 'r') as instance:
            lines = instance.readlines()
            for line in lines:
                if id not in line.strip("\n"):
                    content.append(line)

        with open(self.dbfile, 'w') as instance:
            instance.write('\n'.join(content))