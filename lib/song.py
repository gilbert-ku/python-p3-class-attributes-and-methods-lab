class Song:
    # Class-level attributes to keep track of counts, genres, artists, and counts per genre/artist
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Initialize attributes for each song
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @staticmethod
    def get_song_count():
        return Song.count

    @staticmethod
    def get_genres():
        return Song.genres

    @staticmethod
    def get_artists():
        return Song.artists

    @staticmethod
    def get_genre_count(genre):
        return Song.genre_count.get(genre, 0)

    @staticmethod
    def get_artist_count(artist):
        return Song.artist_count.get(artist, 0)

# Creating instances of the Song class
song1 = Song("Song 1", "Artist 1", "Genre 1")
song2 = Song("Song 2", "Artist 2", "Genre 1")
song3 = Song("Song 3", "Artist 1", "Genre 2")


print("Total songs:", Song.get_song_count())


print("Genres:", Song.get_genres())


print("Artists:", Song.get_artists())


print("Genre 1 count:", Song.get_genre_count("Genre 1"))


print("Artist 1 count:", Song.get_artist_count("Artist 1"))
