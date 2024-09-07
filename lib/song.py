class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        #"""instantiates with a name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre

        #update attributes accordingly
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        

#increases song count by 1 on creating a new song
    @classmethod
    def add_song_to_count(cls):
        Song.count +=1

#adds a new genre to the genre list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

#adds a new artist to the artist list
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

#add to genre count for each genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


# Adds an artist count for all artists in the list
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


Infamous = Song("Infamous", "Mobb Deep", "Rap")




print(Infamous.name)
print(Song.artists)
print(Infamous.genre)