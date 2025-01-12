from lib.album_validator import *
import pytest


def test_is_valid():
    assert AlbumParamValidator("Clancy", "2024", "great", "1").is_valid() == True
    assert AlbumParamValidator( "", "2024", "Description", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", None, "Description", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "", "Description", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", None, "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "Description", None).is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "Description", "").is_valid() == False
    assert AlbumParamValidator("", "", "", "").is_valid() == False
    assert AlbumParamValidator("Clancy", "", "", "").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "", "").is_valid() == False
    assert AlbumParamValidator("", "", "", "1").is_valid() == False
    assert AlbumParamValidator("", "", "Description", "1").is_valid() == False
    assert AlbumParamValidator(None, None, None, None).is_valid() == False
    assert AlbumParamValidator(None, "", "", "").is_valid() == False
    assert AlbumParamValidator("", None, "", "").is_valid() == False
    assert AlbumParamValidator("", "", None, "").is_valid() == False
    assert AlbumParamValidator("", "", "", None).is_valid() == False
    assert AlbumParamValidator(None, None, None, "1").is_valid() == False
    assert AlbumParamValidator(None, None, "Description", "1").is_valid() == False
    assert AlbumParamValidator(None, "2024", None, "1").is_valid() == False
    assert AlbumParamValidator("Clancy", None, None, "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", None, None).is_valid() == False
    assert AlbumParamValidator(None, "2024", "Description", None).is_valid() == False
    assert AlbumParamValidator(None, "", "Description", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", None, "", "1").is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "", None).is_valid() == False
    assert AlbumParamValidator("Clancy", "great", "", None).is_valid() == False
    assert AlbumParamValidator("Clancy", "2024", "", "two").is_valid() == False



def test_album_errors():
    assert AlbumParamValidator(None, "2024", "Description", "1").generate_errors() == "Title can't be blank"
    assert AlbumParamValidator("", "2024", "Description", "1").generate_errors() == "Title can't be blank"
    assert AlbumParamValidator("Clancy", None, "Description", "1").generate_errors() == "Release year can't be blank and has to be a number"
    assert AlbumParamValidator("Clancy", "", "Description", "1").generate_errors() == "Release year can't be blank and has to be a number"
    assert AlbumParamValidator("Clancy", "2024", None, "1").generate_errors() == "Description can't be blank"
    assert AlbumParamValidator("Clancy", "2024", "", "1").generate_errors() == "Description can't be blank"
    assert AlbumParamValidator("Clancy", "2024", "Description", None).generate_errors() == "Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("Clancy", "2024", "Description", "").generate_errors() == "Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("", "", "", "").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("Clancy", "", "", "").generate_errors() == "Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("Clancy", "2024", "", "").generate_errors() == "Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("", "", "", "1").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank"
    assert AlbumParamValidator("", "", "Description", "1").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number"
    assert AlbumParamValidator(None, None, None, None).generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator(None, "", "", "").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("", None, "", "").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("", "", None, "").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("", "", "", None).generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator(None, None, None, "1").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number, Description can't be blank"
    assert AlbumParamValidator(None, None, "Description", "1").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number"
    assert AlbumParamValidator(None, "2024", None, "1").generate_errors() == "Title can't be blank, Description can't be blank"
    assert AlbumParamValidator("Clancy", None, None, "1").generate_errors() == "Release year can't be blank and has to be a number, Description can't be blank" 
    assert AlbumParamValidator("Clancy", "2024", None, None).generate_errors() == "Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator(None, "2024", "Description", None).generate_errors() == "Title can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator(None, "", "Description", "1").generate_errors() == "Title can't be blank, Release year can't be blank and has to be a number"
    assert AlbumParamValidator("Clancy", None, "", "1").generate_errors() == "Release year can't be blank and has to be a number, Description can't be blank"
    assert AlbumParamValidator("Clancy", "2024", "", None).generate_errors() == "Description can't be blank, Artist id can't be blank and has to be a number (check number at artist page)"
    assert AlbumParamValidator("Clancy", "2024", "Description", "1").generate_errors() == None 
    

def test_get_valid_title():
    validator_1 = AlbumParamValidator("Clancy", "2024", "Description", "1")
    assert validator_1.get_valid_title() == "Clancy"

def test_get_valid_title_refuses_bad_title():
    validator_1 = AlbumParamValidator("", "2024", "Description", "1")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_title()
    assert str(err.value) == "Invalid title"

def test_get_valid_release_year():
    validator_2 = AlbumParamValidator("Clancy", "2024", "Description", "1")
    assert validator_2.get_valid_release_year() == 2024

def test_get_valid_year_refuses_bad_year():
    validator_2 = AlbumParamValidator("Clancy", "", "Description", "1")
    with pytest.raises(ValueError) as err:
        validator_2.get_valid_release_year()
    assert str(err.value) == "Invalid release year format"

def test_get_valid_description():
    validator_3 = AlbumParamValidator("Clancy", "2024", "Description", "1")
    assert validator_3.get_valid_description() == "Description"

def test_get_valid_description_refuses_bad_description():
    validator_3 = AlbumParamValidator("Clancy", "2024", "", "1")
    with pytest.raises(ValueError) as err:
        validator_3.get_valid_description()
    assert str(err.value) == "Invalid description"

def test_get_valid_artist_id():
    validator_4 = AlbumParamValidator("Clancy", "2024", "Description", "1")
    assert validator_4.get_valid_artist_id() == 1

def test_get_valid_title_refuses_bad_artist_id():
    validator_4 = AlbumParamValidator("Clancy", "2024", "Description", "")
    with pytest.raises(ValueError) as err:
        validator_4.get_valid_artist_id()
    assert str(err.value) == "Invalid artist id format"