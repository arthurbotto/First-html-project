import os
from flask import Flask, request, render_template
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
    if has_invalid_album_parameters(request.form):
        return 'You must submit a title, release_year and artist_id', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create_album(album)
    return "Album added successfully"

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('music/main.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id, 'id')
    artist_id = album.artist_id
    repo2 = ArtistRepository(connection)
    artist = repo2.find(artist_id, 'id')
    return render_template('music/album.html', album=album, artist=artist)

@app.route('/albums/<id>', methods=['DELETE'])
def delete(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete_album(id, 'id')
    return "Album deleted"

@app.route('/albums/reset', methods=['POST'])
def reset_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete_all_albums()
    return "All albums deleted"

def has_invalid_album_parameters(form):
    return 'title' not in form or \
    'release_year' not in form \
    or 'artist_id' not in form

def is_invalid_artist_parameters(form):
    return 'name' not in form or 'genre' not in form


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    return ", ".join([str(artist.name) for artist in artists])

@app.route('/artists', methods=['POST'])
def post_artist():
    if is_invalid_artist_parameters(request.form):
        return 'You must submit an artist name and genre', 400
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    artist = repo.create(artist)
    return 'Artist added'


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
