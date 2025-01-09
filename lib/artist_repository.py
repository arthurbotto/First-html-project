from lib.artist import Artist

class ArtistRepository:

    
    def __init__(self, connection):
        self._connection = connection

   
    def all(self):
        rows = self._connection.execute('SELECT * from artists ORDER BY id ASC')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    
    def find(self, parameter, column):
        rows = self._connection.execute(
            f'SELECT * from artists WHERE {column} = %s', [parameter])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                 artist.name, artist.genre])
        return None

   
    def delete(self, parameter, column):
        self._connection.execute(
            f'DELETE FROM artists WHERE {column} = %s', [parameter])
        return None
    
    def update(self, artist):
        self._connection.execute(
            'UPDATE artists SET name = %s, genre = %s WHERE id = %s',
            [artist.name, artist.genre, artist.id])
