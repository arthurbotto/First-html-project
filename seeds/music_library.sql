
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;


CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);


INSERT INTO artists (name, genre) VALUES ('Twenty One Pilots', 'Alternative');
INSERT INTO artists (name, genre) VALUES ('Red Hot Chili Peppers', 'Rock');
INSERT INTO artists (name, genre) VALUES ('Arctic Monkeys', 'Indie Rock');
INSERT INTO artists (name, genre) VALUES ('Nothing But Thieves', 'Alternative Rock');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Clancy', 2024, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Blurryface', 2015, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Californication', 1999, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Blood Sugar Sex Magik', 1991, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('AM', 2013, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Favourite Worst Nightmare', 2007, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Broken Machine', 2017, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Moral Panic', 2020, 4);



