from lib.album import *
#from album import *



class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums ORDER BY id ASC')
        #print(rows)
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row['description'], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, parameter, column):
        rows = self._connection.execute(f'SELECT * from albums WHERE {column} = %s', [parameter])
        if not rows:
            return None
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row['description'], row["artist_id"])
        

    def create_album(self, album):
        # self._connection.execute(
        #     'INSERT INTO albums (title, release_year, description, artist_id) VALUES (%s, %s, %s, %s)',
        #     [album.title, album.release_year, album.description, album.artist_id])
        rows = self._connection.execute(
            'INSERT INTO albums (title, release_year, description, artist_id) VALUES (%s, %s, %s, %s) RETURNING id',
            [album.title, album.release_year, album.description, album.artist_id])
        row = rows[0]
        album.id = row["id"]
        return album
    
    def delete_album(self, parameter, column):
        self._connection.execute(
            f'DELETE FROM albums WHERE {column} = %s', [parameter])
        return None
    
    def update_album(self, album):
        self._connection.execute('UPDATE albums SET title = %s, release_year = %s, description = %s, artist_id = %s WHERE id = %s',
                                 [album.title, album.release_year, album.description, album.artist_id, album.id]
        )
        return None
    
    def delete_all_albums(self):
        self._connection.execute('DELETE FROM albums')
        return 'All albums deleted successfuly!'
    
    
        