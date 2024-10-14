class UserClass():
    def __init__(self, first_name, last_name, library_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__library_id = library_id


    def detail(self):
        return f"First Name: {self.__first_name}, Last Name: {self.__last_name}, Library ID: {self.__library_id}"
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_library_id(self):
        return self.__library_id
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    def get_library_id(self, library_id):
        self.__library_id = library_id