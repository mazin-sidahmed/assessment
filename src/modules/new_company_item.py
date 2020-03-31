from src.modules.base_item import BaseItem


class NewCompanyItem(BaseItem):

    def __init__(self, filename):
        super().__init__(filename)


    def save(self, id, name, price, brand):

        with open(self.dbfile, 'a+') as instance: 
            instance.write("%s, %s, %s, %s\n"%(id, name, price, brand))
    
    