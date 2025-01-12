from lib.artist_validator import *
import pytest

def test_is_valid():
    assert ArtistParamValidator(None, None).is_valid() == False
    assert ArtistParamValidator(None, 'test').is_valid() == False
    assert ArtistParamValidator(None, '').is_valid() == False
    assert ArtistParamValidator('', 'test').is_valid() == False
    assert ArtistParamValidator('test', None).is_valid() == False
    assert ArtistParamValidator('', None).is_valid() == False
    assert ArtistParamValidator('test', '').is_valid() == False
    assert ArtistParamValidator('', '').is_valid() == False
    assert ArtistParamValidator('', '').is_valid() == False
    assert ArtistParamValidator(None, None).is_valid() == False
    assert ArtistParamValidator('test', 'test').is_valid() == True
    

def test_artist_errors():
    assert ArtistParamValidator(None, None).generate_errors() == "Name can't be blank, Genre can't be blank"
    assert ArtistParamValidator(None, 'test').generate_errors() == "Name can't be blank"
    assert ArtistParamValidator('', 'test').generate_errors() == "Name can't be blank"
    assert ArtistParamValidator('test', None).generate_errors() == "Genre can't be blank"
    assert ArtistParamValidator('test', '').generate_errors() == "Genre can't be blank"
    assert ArtistParamValidator('', '').generate_errors() == "Name can't be blank, Genre can't be blank"
    assert ArtistParamValidator('', '').generate_errors() == "Name can't be blank, Genre can't be blank"
    assert ArtistParamValidator(None, None).generate_errors() == "Name can't be blank, Genre can't be blank"
    assert ArtistParamValidator('test', 'test').generate_errors() == None

def test_get_valid_name():
    validator_1 = ArtistParamValidator("Twenty One Pilots", "Alternative")
    assert validator_1.get_valid_name() == "Twenty One Pilots"

def test_get_valid_name_refuses_invalid_name():
    validator_1 = ArtistParamValidator("", "Alternative")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Invalid artist name"

def test_get_valid_genre():
    validator_1 = ArtistParamValidator("Twenty One Pilots", "Alternative")
    assert validator_1.get_valid_genre() == "Alternative"

def test_get_valid_name_refuses_invalid_name():
    validator_1 = ArtistParamValidator("Twenty One Pilots", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_genre()
    assert str(err.value) == "Invalid genre"