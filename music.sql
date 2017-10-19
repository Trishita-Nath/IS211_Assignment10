CREATE TABLE artist (artist_id INTEGER PRIMARY KEY, artist TEXT);
		
CREATE TABLE album (album_id INTEGER PRIMARY KEY, album TEXT, artistID INTEGER);

CREATE TABLE album_song (id INTEGER PRIMARY KEY, album_id, song_id);	

CREATE TABLE song (song_id INTEGER PRIMARY KEY, song TEXT, artistID INTEGER, trackNum INTEGER, trackLen INTEGER);


