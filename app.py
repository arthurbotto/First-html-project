import os
from flask import Flask, redirect, request, render_template, url_for
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)


@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    description = request.form['description']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, description, artist_id)
    if not album.is_valid():
        return render_template('music/newalbum.html', album=album, errors=album.generate_errors()), 400
    album = repository.create_album(album)
    return redirect(f"/albums/{album.id}") 

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repo2 = ArtistRepository(connection)
    albums = repository.all()
    for album in albums:
        id = album.artist_id
        artist = repo2.find(id, 'id')
        album.artist_name = artist.name if artist else "Artist not added yet"
        
    return render_template('music/allalbums.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id, 'id')
    if album is None:
        return "Album not found", 404
    artist_id = album.artist_id
    repo2 = ArtistRepository(connection)
    artist = repo2.find(artist_id, 'id')
    artist_name = artist.name if artist else "Artist not added yet"
    
    return render_template('music/album.html', album=album, artist_name=artist_name)

@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('music/newalbum.html')

@app.route('/albums/<int:id>/delete', methods=['POST'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete_album(id, 'id')
    return redirect(url_for('get_albums'))


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    
    return render_template('music/allartists.html', artists=artists)


@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id, 'id')
    return render_template('music/artist.html', artist=artist)

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    if not artist.is_valid():
        return render_template('music/newalbum.html', artist=artist, errors=artist.generate_errors()), 400
    artist = repo.create(artist)
    return redirect(f"/artists/{artist.id}") 

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('music/newartist.html')

@app.route('/artists/<int:id>/delete', methods=['POST'])
def delete_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.delete(id, 'id')
    return redirect(url_for('get_artists'))




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
