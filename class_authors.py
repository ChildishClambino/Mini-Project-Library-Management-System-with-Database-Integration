class Authors_Class():
    def __init__(self, author_name, biography ):
        self.__author_name = author_name
        self.__biography = biography
    
    def details(self):
        return f"Name: {self.__author_name}, Biography: {self.__biography}"

    def get_author(self):
        return self.__author_name
    
    def get_biography(self):
        return self.__biography
    
    def set_author(self, author_name):
        self.__author_name = author_name

    def set_biography(self, biography):
        self.__biography = biography