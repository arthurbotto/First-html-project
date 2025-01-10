from lib.album import *

def test_album_constructs():
    album = Album(1, "Clancy", 2024, "great album", 1)
    assert album.id == 1
    assert album.title == "Clancy"
    assert album.release_year == 2024
    assert album.description == "great album"
    assert album.artist_id == 1

def test_album_format_nicely():
    album = Album(1, "Clancy", 2024, "great album", 1)
    assert str(album) == "Album(1, Clancy, 2024, great album, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Clancy", 2024, "great album", 1)
    album2 = Album(1, "Clancy", 2024, "great album", 1)
    assert album1 == album2

def test_is_valid():
    assert Album(1, None, 2024, "Description", 1).is_valid() == False
    assert Album(1, "", 2024, "Description", 1).is_valid() == False
    assert Album(1, "Clancy", None, "Description", 1).is_valid() == False
    assert Album(1, "Clancy", "", "Description", 1).is_valid() == False
    assert Album(1, "Clancy", 2024, None, 1).is_valid() == False
    assert Album(1, "Clancy", 2024, "", 1).is_valid() == False
    assert Album(1, "Clancy", 2024, "Description", None).is_valid() == False
    assert Album(1, "Clancy", 2024, "Description", "").is_valid() == False
    assert Album(1, "", "", "", "").is_valid() == False
    assert Album(1, "Clancy", "", "", "").is_valid() == False
    assert Album(1, "Clancy", 2024, "", "").is_valid() == False
    assert Album(1, "", "", "", 1).is_valid() == False
    assert Album(1, "", "", "Description", 1).is_valid() == False
    assert Album(1, None, None, None, None).is_valid() == False
    assert Album(1, None, "", "", "").is_valid() == False
    assert Album(1, "", None, "", "").is_valid() == False
    assert Album(1, "", "", None, "").is_valid() == False
    assert Album(1, "", "", "", None).is_valid() == False
    assert Album(1, None, None, None, 1).is_valid() == False
    assert Album(1, None, None, "Description", 1).is_valid() == False
    assert Album(1, None, 2024, None, 1).is_valid() == False
    assert Album(1, "Clancy", None, None, 1).is_valid() == False
    assert Album(1, "Clancy", 2024, None, None).is_valid() == False
    assert Album(1, None, 2024, "Description", None).is_valid() == False
    assert Album(1, None, "", "Description", 1).is_valid() == False
    assert Album(1, "Clancy", None, "", 1).is_valid() == False
    assert Album(1, "Clancy", 2024, "", None).is_valid() == False
    assert Album(1, "Clancy", 2024, "Description", 1).is_valid() == True
    assert Album(None, "Clancy", 2024, "Description", 1).is_valid() == True

    
def test_album_errors():
    assert Album(1, None, 2024, "Description", 1).generate_errors() == "Title can't be blank"
    assert Album(1, "", 2024, "Description", 1).generate_errors() == "Title can't be blank"
    assert Album(1, "Clancy", None, "Description", 1).generate_errors() == "Release year can't be blank"
    assert Album(1, "Clancy", "", "Description", 1).generate_errors() == "Release year can't be blank"
    assert Album(1, "Clancy", 2024, None, 1).generate_errors() == "Description can't be blank"
    assert Album(1, "Clancy", 2024, "", 1).generate_errors() == "Description can't be blank"
    assert Album(1, "Clancy", 2024, "Description", None).generate_errors() == "artist id can't be blank"
    assert Album(1, "Clancy", 2024, "Description", "").generate_errors() == "artist id can't be blank"
    assert Album(1, "", "", "", "").generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, "Clancy", "", "", "").generate_errors() == "Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, "Clancy", 2024, "", "").generate_errors() == "Description can't be blank, artist id can't be blank"
    assert Album(1, "", "", "", 1).generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank"
    assert Album(1, "", "", "Description", 1).generate_errors() == "Title can't be blank, Release year can't be blank"
    assert Album(1, None, None, None, None).generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, None, "", "", "").generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, "", None, "", "").generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, "", "", None, "").generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, "", "", "", None).generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank"
    assert Album(1, None, None, None, 1).generate_errors() == "Title can't be blank, Release year can't be blank, Description can't be blank"
    assert Album(1, None, None, "Description", 1).generate_errors() == "Title can't be blank, Release year can't be blank"
    assert Album(1, None, 2024, None, 1).generate_errors() == "Title can't be blank, Description can't be blank"
    assert Album(1, "Clancy", None, None, 1).generate_errors() == "Release year can't be blank, Description can't be blank" 
    assert Album(1, "Clancy", 2024, None, None).generate_errors() == "Description can't be blank, artist id can't be blank"
    assert Album(1, None, 2024, "Description", None).generate_errors() == "Title can't be blank, artist id can't be blank"
    assert Album(1, None, "", "Description", 1).generate_errors() == "Title can't be blank, Release year can't be blank"
    assert Album(1, "Clancy", None, "", 1).generate_errors() == "Release year can't be blank, Description can't be blank"
    assert Album(1, "Clancy", 2024, "", None).generate_errors() == "Description can't be blank, artist id can't be blank"
    assert Album(1, "Clancy", 2024, "Description", 1).generate_errors() == None 
    assert Album(None, "Clancy", 2024, "Description", 1).generate_errors() == None
