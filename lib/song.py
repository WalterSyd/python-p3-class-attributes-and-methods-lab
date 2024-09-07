class Song:
    
    count = 0
    genres = []

    def __init__(self, name, artist, genre):
        #"""instantiates with a name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre

        #implement s
        self.add_song_to_count()
        self.add_to_genres(genre)

#increases song count by 1 on creating a new song
    @classmethod
    def add_song_to_count(cls):
        Song.count +=1

#adds a new genre to the genre list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

#
    # @classmethod


Infamous = Song("Infamous", "Mobb Deep", "Rap")




print(Infamous.name)
print(Infamous.artist)
print(Infamous.genre)