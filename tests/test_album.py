from lib.album import *

def test_album_constructs():
    album = Album(1, "Clancy", 2024, 1)
    assert album.id == 1
    assert album.title == "Clancy"
    assert album.release_year == 2024
    assert album.artist_id == 1

def test_album_format_nicely():
    album = Album(1, "Clancy", 2024, 1)
    assert str(album) == "Album(1, Clancy, 2024, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Clancy", 2024, 1)
    album2 = Album(1, "Clancy", 2024, 1)
    assert album1 == album2