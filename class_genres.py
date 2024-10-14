class Genre_Class():
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category
    
    def details(self):
        return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_category(self):
        return self.__category
    
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_name(self, category):
        self.__category = category

        