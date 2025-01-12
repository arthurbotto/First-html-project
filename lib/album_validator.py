class AlbumParamValidator:
    def __init__(self, title, release_year, description, artist_id):
        self.title = title
        self.release_year = release_year
        self.description = description
        self.artist_id = artist_id


    def is_valid(self):
        if not self.is_valid_title():
            return False
        if not self.is_valid_release_year():
            return False
        if not self.is_valid_description():
            return False
        if not self.is_valid_artist_id():
            return False
        return True

    def is_valid_title(self):
        if self.title == None or self.title == "":
            return False
        return True
    
    def is_valid_release_year(self):
        if self.release_year == None or self.release_year == "":
            return False
        if not self.release_year.isdigit():
            return False
        return True
    
    def is_valid_description(self):
        if self.description == None or self.description == "":
            return False
        return True
    
    def is_valid_artist_id(self):
        if self.artist_id == None or self.artist_id == "":
            return False
        if not self.artist_id.isdigit():
            return False
        return True
    

    def generate_errors(self):
        errors = []
        if not self.is_valid_title():
            errors.append("Title can't be blank")
        if not self.is_valid_release_year():
            errors.append("Release year can't be blank and has to be a number")
        if not self.is_valid_description():
            errors.append("Description can't be blank")
        if not self.is_valid_artist_id():
            errors.append("Artist id can't be blank and has to be a number (check number at artist page)")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    def get_valid_title(self):
        if not self.is_valid_title():
            raise ValueError("Invalid title")
        return self.title
    
    def get_valid_release_year(self):
        if not self.is_valid_release_year():
            raise ValueError("Invalid release year format")
        return int(self.release_year)
    
    def get_valid_description(self):
        if not self.is_valid_description():
            raise ValueError("Invalid description")
        return self.description
    
    def get_valid_artist_id(self):
        if not self.is_valid_artist_id():
            raise ValueError("Invalid artist id format")
        return int(self.artist_id)