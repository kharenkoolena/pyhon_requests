import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

artist_name_eminem = config.get("ARTISTS", "ARTIST_NAME_EMINEM")
artist_id_eminem = config.get("ARTISTS", "ARTIST_ID_EMINEM")
artist_name_beatles = config.get("ARTISTS", "ARTIST_NAME_BEATLES")
artist_id_beatles = config.get("ARTISTS", "ARTIST_ID_BEATLES")
artist_track_title_beatles = config.get("ARTISTS", "ARTIST_TRACK_TITLE_BEATLES")
artist_track_id_beatles = config.get("ARTISTS", "ARTIST_TRACK_ID_BEATLES")

track_title = config.get("TRACKS", "TRACK_TITLE")
track_id = config.get("TRACKS", "TRACK_ID")
track_artist_name = config.get("TRACKS", "TRACK_ARTIST_NAME")
