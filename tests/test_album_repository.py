from lib.album_repository import *
from lib.album import *

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
    Album(1, 'Clancy', 2024, 1),
    Album(2, 'Blurryface', 2015, 1),
    Album(3, 'Californication', 1999, 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 2),
    Album(5, 'AM', 2013, 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 3),
    Album(7, 'Broken Machine', 2017, 4),
    Album(8, 'Moral Panic', 2020, 4),]
    


def test_find_one_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.find(2, "id")
    assert album == Album(2, 'Blurryface', 2015, 1)

def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.create_album(Album(None, 'Trench', 2018, 1))
    result = repo.all()
    assert result == [
    Album(1, 'Clancy', 2024, 1),
    Album(2, 'Blurryface', 2015, 1),
    Album(3, 'Californication', 1999, 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 2),
    Album(5, 'AM', 2013, 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 3),
    Album(7, 'Broken Machine', 2017, 4),
    Album(8, 'Moral Panic', 2020, 4),
    Album(9, 'Trench', 2018, 1)]

def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.delete_album(7, 'id')
    result = repo.all()
    assert result == [
    Album(1, 'Clancy', 2024, 1),
    Album(2, 'Blurryface', 2015, 1),
    Album(3, 'Californication', 1999, 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 2),
    Album(5, 'AM', 2013, 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 3),
    Album(8, 'Moral Panic', 2020, 4)]




def test_update_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.find(8, 'id')
    album.release_year = 2025
    repo.update_album(album)
    result = repo.all()
    assert result == [
        Album(1, 'Clancy', 2024, 1),
        Album(2, 'Blurryface', 2015, 1),
        Album(3, 'Californication', 1999, 2),
        Album(4, 'Blood Sugar Sex Magik', 1991, 2),
        Album(5, 'AM', 2013, 3),
        Album(6, 'Favourite Worst Nightmare', 2007, 3),
        Album(7, 'Broken Machine', 2017, 4),
        Album(8, 'Moral Panic', 2025, 4)]

def test_delete_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    result = repo.delete_all_albums()
    assert result == 'All albums deleted successfuly!'
    result2 = repo.all()
    assert result2 == []
