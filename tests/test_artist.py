from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"


def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"


def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2

def test_is_valid():
    assert Artist(1, None, None).is_valid() == False
    assert Artist(1, None, 'test').is_valid() == False
    assert Artist(1, None, '').is_valid() == False
    assert Artist(1, '', 'test').is_valid() == False
    assert Artist(1, 'test', None).is_valid() == False
    assert Artist(1, '', None).is_valid() == False
    assert Artist(1, 'test', '').is_valid() == False
    assert Artist(1, '', '').is_valid() == False
    assert Artist(None, '', '').is_valid() == False
    assert Artist(None, None, None).is_valid() == False
    assert Artist(1, 'test', 'test').is_valid() == True
    assert Artist(None, 'test', 'test').is_valid() == True

def test_artist_errors():
    assert Artist(1, None, None).generate_errors() == "Name can't be blank, Genre can't be blank"
    assert Artist(1, None, 'test').generate_errors() == "Name can't be blank"
    assert Artist(1, '', 'test').generate_errors() == "Name can't be blank"
    assert Artist(1, 'test', None).generate_errors() == "Genre can't be blank"
    assert Artist(1, 'test', '').generate_errors() == "Genre can't be blank"
    assert Artist(1, '', '').generate_errors() == "Name can't be blank, Genre can't be blank"
    assert Artist(None, '', '').generate_errors() == "Name can't be blank, Genre can't be blank"
    assert Artist(None, None, None).generate_errors() == "Name can't be blank, Genre can't be blank"
    assert Artist(1, 'test', 'test').generate_errors() == None
    assert Artist(None, 'test', 'test').generate_errors() == None