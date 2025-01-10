from lib.album_repository import *
from lib.album import *

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
    Album(1, 'Clancy', 2024, 'Clancy is the seventh studio album by American musical duo Twenty One Pilots, released on May 24, 2024, through Fueled by Ramen and Elektra Records.', 1),
    Album(2, 'Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1),
    Album(3, 'Californication', 1999, 'Californication is the seventh studio album by U.S. rock band Red Hot Chili Peppers, released on June 8, 1999, on Warner Bros. Records. It was produced by Rick Rubin. Along with Blood Sugar Sex Magik, Californication is one of the bands best-selling albums.', 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 'Blood Sugar Sex Magik is the fifth studio album by American rock band Red Hot Chili Peppers, released on September 24, 1991, by Warner Bros. Records.', 2),
    Album(5, 'AM', 2013, 'AM is the fifth studio album by English rock band Arctic Monkeys. It was produced by longtime collaborator James Ford and co-produced by Ross Orton.', 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 'Favourite Worst Nightmare is the second studio album by English rock band Arctic Monkeys, first released in Japan on 18 April 2007', 3),
    Album(7, 'Broken Machine', 2017, 'Broken Machine is the second studio album by English rock band Nothing but Thieves. It was released on 8 September 2017 under RCA and Sony Music and produced by Mike Crossey.', 4),
    Album(8, 'Moral Panic', 2020, 'Moral Panic is the third studio album by English alternative rock band Nothing but Thieves. The album was released on 23 October 2020 through Sony Music UK.', 4)]
    


def test_find_one_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.find(2, "id")
    assert album == Album(2, 'Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1)
    album2 = repo.find(12, 'id')
    assert album2 == None
def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.create_album(Album(None, 'Trench', 2018, 'great album', 1))
    result = repo.all()
    assert result == [
    Album(1, 'Clancy', 2024, 'Clancy is the seventh studio album by American musical duo Twenty One Pilots, released on May 24, 2024, through Fueled by Ramen and Elektra Records.', 1),
    Album(2, 'Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1),
    Album(3, 'Californication', 1999, 'Californication is the seventh studio album by U.S. rock band Red Hot Chili Peppers, released on June 8, 1999, on Warner Bros. Records. It was produced by Rick Rubin. Along with Blood Sugar Sex Magik, Californication is one of the bands best-selling albums.', 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 'Blood Sugar Sex Magik is the fifth studio album by American rock band Red Hot Chili Peppers, released on September 24, 1991, by Warner Bros. Records.', 2),
    Album(5, 'AM', 2013, 'AM is the fifth studio album by English rock band Arctic Monkeys. It was produced by longtime collaborator James Ford and co-produced by Ross Orton.', 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 'Favourite Worst Nightmare is the second studio album by English rock band Arctic Monkeys, first released in Japan on 18 April 2007', 3),
    Album(7, 'Broken Machine', 2017, 'Broken Machine is the second studio album by English rock band Nothing but Thieves. It was released on 8 September 2017 under RCA and Sony Music and produced by Mike Crossey.', 4),
    Album(8, 'Moral Panic', 2020, 'Moral Panic is the third studio album by English alternative rock band Nothing but Thieves. The album was released on 23 October 2020 through Sony Music UK.', 4),
    Album(9, 'Trench', 2018, 'great album', 1)]

def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.delete_album(7, 'id')
    result = repo.all()
    assert result == [
    Album(1, 'Clancy', 2024, 'Clancy is the seventh studio album by American musical duo Twenty One Pilots, released on May 24, 2024, through Fueled by Ramen and Elektra Records.', 1),
    Album(2, 'Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1),
    Album(3, 'Californication', 1999, 'Californication is the seventh studio album by U.S. rock band Red Hot Chili Peppers, released on June 8, 1999, on Warner Bros. Records. It was produced by Rick Rubin. Along with Blood Sugar Sex Magik, Californication is one of the bands best-selling albums.', 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 'Blood Sugar Sex Magik is the fifth studio album by American rock band Red Hot Chili Peppers, released on September 24, 1991, by Warner Bros. Records.', 2),
    Album(5, 'AM', 2013, 'AM is the fifth studio album by English rock band Arctic Monkeys. It was produced by longtime collaborator James Ford and co-produced by Ross Orton.', 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 'Favourite Worst Nightmare is the second studio album by English rock band Arctic Monkeys, first released in Japan on 18 April 2007', 3),
    Album(8, 'Moral Panic', 2020, 'Moral Panic is the third studio album by English alternative rock band Nothing but Thieves. The album was released on 23 October 2020 through Sony Music UK.', 4)]




def test_update_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.find(8, 'id')
    album.release_year = 2025
    repo.update_album(album)
    result = repo.all()
    assert result == [
    Album(1, 'Clancy', 2024, 'Clancy is the seventh studio album by American musical duo Twenty One Pilots, released on May 24, 2024, through Fueled by Ramen and Elektra Records.', 1),
    Album(2, 'Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1),
    Album(3, 'Californication', 1999, 'Californication is the seventh studio album by U.S. rock band Red Hot Chili Peppers, released on June 8, 1999, on Warner Bros. Records. It was produced by Rick Rubin. Along with Blood Sugar Sex Magik, Californication is one of the bands best-selling albums.', 2),
    Album(4, 'Blood Sugar Sex Magik', 1991, 'Blood Sugar Sex Magik is the fifth studio album by American rock band Red Hot Chili Peppers, released on September 24, 1991, by Warner Bros. Records.', 2),
    Album(5, 'AM', 2013, 'AM is the fifth studio album by English rock band Arctic Monkeys. It was produced by longtime collaborator James Ford and co-produced by Ross Orton.', 3),
    Album(6, 'Favourite Worst Nightmare', 2007, 'Favourite Worst Nightmare is the second studio album by English rock band Arctic Monkeys, first released in Japan on 18 April 2007', 3),
    Album(7, 'Broken Machine', 2017, 'Broken Machine is the second studio album by English rock band Nothing but Thieves. It was released on 8 September 2017 under RCA and Sony Music and produced by Mike Crossey.', 4),
    Album(8, 'Moral Panic', 2025, 'Moral Panic is the third studio album by English alternative rock band Nothing but Thieves. The album was released on 23 October 2020 through Sony Music UK.', 4)]

def test_delete_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    result = repo.delete_all_albums()
    assert result == 'All albums deleted successfuly!'
    result2 = repo.all()
    assert result2 == []
