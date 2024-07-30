class Genre:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.get_description
    
    def __str__(self):
        return f"Genre: {self.__name}, Desciption: {self.__description}"