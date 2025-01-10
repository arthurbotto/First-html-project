from playwright.sync_api import Page, expect


"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address):
   page.goto(f"http://{test_web_address}/emoji")
   strong_tag = page.locator("strong")
   expect(strong_tag).to_have_text(":)")


def test_create_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "Trench")
    page.fill("input[name='release_year']", "2018")
    page.fill("input[name='description']", "great album")
    page.fill("input[name='artist_id']", "1")
    page.click("text=Create Album")
    
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Trench")
    
    release_year = page.locator(".t-release_year")
    expect(release_year).to_have_text("Released on: 2018")
    
    description = page.locator(".t-description")
    expect(description).to_have_text("great album")

    artist = page.locator(".t-artist_name")
    expect(artist).to_have_text("By: Twenty One Pilots")


def test_create_albums_that_has_no_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "Red")
    page.fill("input[name='release_year']", "2018")
    page.fill("input[name='description']", "okay album")
    page.fill("input[name='artist_id']", "5")
    page.click("text=Create Album")
    
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Red")
    
    release_year = page.locator(".t-release_year")
    expect(release_year).to_have_text("Released on: 2018")
    
    description = page.locator(".t-description")
    expect(description).to_have_text("okay album")

    artist = page.locator(".t-artist_name")
    expect(artist).to_have_text("By: Artist not added yet")

def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release year can't be blank, Description can't be blank, artist id can't be blank")

    

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    list_albums = page.locator('li')
    expect(list_albums).to_have_text([
    'Title: Clancy\nBy: Twenty One Pilots',
    'Title: Blurryface\nBy: Twenty One Pilots',
    'Title: Californication\nBy: Red Hot Chili Peppers',
    'Title: Blood Sugar Sex Magik\nBy: Red Hot Chili Peppers',
    'Title: AM\nBy: Arctic Monkeys',
    'Title: Favourite Worst Nightmare\nBy: Arctic Monkeys',
    'Title: Broken Machine\nBy: Nothing But Thieves',
    'Title: Moral Panic\nBy: Nothing But Thieves'])

def test_get_album_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    h1_tag = page.locator('h1')
    release_year = page.locator(".t-release_year")
    artist = page.locator(".t-artist_name")
    description = page.locator(".t-description")
    
    expect(h1_tag).to_have_text('Blurryface')
    expect(release_year).to_have_text("Released on: 2015")
    expect(artist).to_have_text("By: Twenty One Pilots")
    expect(description).to_have_text("Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.")
    

def test_delete_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    page.click("text=Delete Album")
    list_albums = page.locator('li')
    expect(list_albums).to_have_text([
    'Title: Clancy\nBy: Twenty One Pilots',
    'Title: Californication\nBy: Red Hot Chili Peppers',
    'Title: Blood Sugar Sex Magik\nBy: Red Hot Chili Peppers',
    'Title: AM\nBy: Arctic Monkeys',
    'Title: Favourite Worst Nightmare\nBy: Arctic Monkeys',
    'Title: Broken Machine\nBy: Nothing But Thieves',
    'Title: Moral Panic\nBy: Nothing But Thieves'])




def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.fill("input[name='name']", "Taylor Swift")
    page.fill("input[name='genre']", "Pop")
    page.click("text=Create Artist")
    
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Taylor Swift")
    
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Genre: Pop")

def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")



def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    list_artists = page.locator('li')
    expect(list_artists).to_have_text([
        'Twenty One Pilots',
        'Red Hot Chili Peppers',
        'Arctic Monkeys',
        'Nothing But Thieves'])
    
def test_get_artist_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    h1_tag = page.locator('h1')
    h2_tag = page.locator('h2')
    expect(h1_tag).to_have_text(['Red Hot Chili Peppers'])
    expect(h2_tag).to_have_text(['Genre: Rock'])

def test_delete_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    page.click("text=Delete Artist")
    list_artists = page.locator('li')
    expect(list_artists).to_have_text([
        'Twenty One Pilots',
        'Arctic Monkeys',
        'Nothing But Thieves'])