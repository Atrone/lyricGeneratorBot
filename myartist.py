import lyricsgenius
import re

class MyArtist:
    def __init__(self,artist:str="",max_songs:int=100,sort:str="title"):
        self.genius = lyricsgenius.Genius("hNM7GziL7k_2_zIM4uFBeJaHpAU03Yr0dAYgR0scvuWMpGxkvAFzHXcgHXgeAwaH")
        self.artist = self.genius.search_artist(artist, max_songs=max_songs, sort=sort)
        self.lyrics_for_artist = []
        self.artist_name = artist
        self.max_songs = max_songs

    def populate_lyrics_for_artist(self):
        for song in self.artist.songs:
            for songLyric in iter(song.lyrics.splitlines()):
                if not re.match("\[.*\]",songLyric):
                    if songLyric:
                        self.lyrics_for_artist.append(((songLyric.replace("Embed","")).replace("URL","").replace("Copy","")))
        self.lyrics_for_artist = list(filter(None,self.lyrics_for_artist))
        print(self.lyrics_for_artist)

