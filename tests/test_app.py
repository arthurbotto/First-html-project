from playwright.sync_api import Page, expect


"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address):
   page.goto(f"http://{test_web_address}/emoji")
   strong_tag = page.locator("strong")
   expect(strong_tag).to_have_text(":)")


# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/albums', data={
#         'title': 'Trench',
#         'release_year': '2018',
#         'artist_id': '1'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == "Album added successfully"

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#     'Album(1, Clancy, 2024, 1)\n'\
#     'Album(2, Blurryface, 2015, 1)\n'\
#     'Album(3, Californication, 1999, 2)\n'\
#     'Album(4, Blood Sugar Sex Magik, 1991, 2)\n'\
#     'Album(5, AM, 2013, 3)\n'\
#     'Album(6, Favourite Worst Nightmare, 2007, 3)\n'\
#     'Album(7, Broken Machine, 2017, 4)\n'\
#     'Album(8, Moral Panic, 2020, 4)\n'\
#     'Album(9, Trench, 2018, 1)'
    


# def test_post_albums_with_no_data(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/albums')
#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == 'You must submit a title, release_year and artist_id'

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#     'Album(1, Clancy, 2024, 1)\n'\
#     'Album(2, Blurryface, 2015, 1)\n'\
#     'Album(3, Californication, 1999, 2)\n'\
#     'Album(4, Blood Sugar Sex Magik, 1991, 2)\n'\
#     'Album(5, AM, 2013, 3)\n'\
#     'Album(6, Favourite Worst Nightmare, 2007, 3)\n'\
#     'Album(7, Broken Machine, 2017, 4)\n'\
#     'Album(8, Moral Panic, 2020, 4)'

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    list_albums = page.locator('li')
    expect(list_albums).to_have_text([
    'Title: Clancy\nReleased: 2024',
    'Title: Blurryface\nReleased: 2015',
    'Title: Californication\nReleased: 1999',
    'Title: Blood Sugar Sex Magik\nReleased: 1991',
    'Title: AM\nReleased: 2013',
    'Title: Favourite Worst Nightmare\nReleased: 2007',
    'Title: Broken Machine\nReleased: 2017',
    'Title: Moral Panic\nReleased: 2020'])

def test_get_album_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    h1_tag = page.locator('h1')
    p_tag = page.locator('p')
    expect(h1_tag).to_have_text('Blurryface')
    expect(p_tag).to_have_text("" \
    'Release Year: 2015\n'\
    'Artist: Twenty One Pilots')



def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Artist added'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Twenty One Pilots, Red Hot Chili Peppers, Arctic Monkeys, Nothing But Thieves, Wild nothing'

def test_post_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post('/artists')
        
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'You must submit an artist name and genre'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Twenty One Pilots, Red Hot Chili Peppers, Arctic Monkeys, Nothing But Thieves'

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Twenty One Pilots, Red Hot Chili Peppers, Arctic Monkeys, Nothing But Thieves'