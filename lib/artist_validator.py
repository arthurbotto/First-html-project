class ArtistParamValidator:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    
    def is_valid(self):
        if not self.is_valid_name():
            return False
        if not self.is_valid_genre():
            return False
        return True

    def is_valid_name(self):
        if self.name == None or self.name == "":
            return False
        return True
    
    def is_valid_genre(self):
        if self.genre == None or self.genre == "":
            return False
        return True
    
    def get_valid_name(self):
        if not self.is_valid_name():
            raise ValueError("Invalid artist name")
        return self.name
    
    def get_valid_genre(self):
        if not self.is_valid_genre():
            raise ValueError("Invalid genre")
        return self.genre
    
    def generate_errors(self):
        errors = []
        if not self.is_valid_name():
            errors.append("Name can't be blank")
        if not self.is_valid_genre():
            errors.append("Genre can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)