
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
    title TEXT,
    release_year INTEGER,
    description TEXT,
    artist_id INTEGER
);


INSERT INTO artists (name, genre) VALUES ('Twenty One Pilots', 'Alternative');
INSERT INTO artists (name, genre) VALUES ('Red Hot Chili Peppers', 'Rock');
INSERT INTO artists (name, genre) VALUES ('Arctic Monkeys', 'Indie Rock');
INSERT INTO artists (name, genre) VALUES ('Nothing But Thieves', 'Alternative Rock');

INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Clancy', 2024, 'Clancy is the seventh studio album by American musical duo Twenty One Pilots, released on May 24, 2024, through Fueled by Ramen and Elektra Records.', 1);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Blurryface', 2015, 'Blurryface is the fourth studio album by American musical duo Twenty One Pilots. It was released on May 17, 2015, through Fueled by Ramen.', 1);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Californication', 1999, 'Californication is the seventh studio album by U.S. rock band Red Hot Chili Peppers, released on June 8, 1999, on Warner Bros. Records. It was produced by Rick Rubin. Along with Blood Sugar Sex Magik, Californication is one of the bands best-selling albums.', 2);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Blood Sugar Sex Magik', 1991, 'Blood Sugar Sex Magik is the fifth studio album by American rock band Red Hot Chili Peppers, released on September 24, 1991, by Warner Bros. Records.', 2);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('AM', 2013, 'AM is the fifth studio album by English rock band Arctic Monkeys. It was produced by longtime collaborator James Ford and co-produced by Ross Orton.', 3);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Favourite Worst Nightmare', 2007, 'Favourite Worst Nightmare is the second studio album by English rock band Arctic Monkeys, first released in Japan on 18 April 2007', 3);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Broken Machine', 2017, 'Broken Machine is the second studio album by English rock band Nothing but Thieves. It was released on 8 September 2017 under RCA and Sony Music and produced by Mike Crossey.', 4);
INSERT INTO albums (title, release_year, description, artist_id) VALUES ('Moral Panic', 2020, 'Moral Panic is the third studio album by English alternative rock band Nothing but Thieves. The album was released on 23 October 2020 through Sony Music UK.', 4);



