from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_library.sql") 
    repository = ArtistRepository(db_connection) 

    artists = repository.all() 

    
    assert artists == [
        Artist(1, 'Twenty One Pilots', 'Alternative'),
        Artist(2, 'Red Hot Chili Peppers', 'Rock'),
        Artist(3, 'Arctic Monkeys', 'Indie Rock'),
        Artist(4, 'Nothing But Thieves', 'Alternative Rock')
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3, 'id')
    assert artist == Artist(3, "Arctic Monkeys", "Indie Rock")


def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "The Beatles", "Rock"))

    result = repository.all()
    assert result == [
        Artist(1, 'Twenty One Pilots', 'Alternative'),
        Artist(2, 'Red Hot Chili Peppers', 'Rock'),
        Artist(3, 'Arctic Monkeys', 'Indie Rock'),
        Artist(4, 'Nothing But Thieves', 'Alternative Rock'),
        Artist(5, "The Beatles", "Rock"),
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3, 'id') 

    result = repository.all()
    assert result == [
        Artist(1, 'Twenty One Pilots', 'Alternative'),
        Artist(2, 'Red Hot Chili Peppers', 'Rock'),
        Artist(4, 'Nothing But Thieves', 'Alternative Rock')
    ]

def test_update_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find(4, "id")
    artist.genre = "Pop"
    repository.update(artist)
    assert repository.all() == [
        Artist(1, 'Twenty One Pilots', 'Alternative'),
        Artist(2, 'Red Hot Chili Peppers', 'Rock'),
        Artist(3, 'Arctic Monkeys', 'Indie Rock'),
        Artist(4, 'Nothing But Thieves', 'Pop')
    ]
