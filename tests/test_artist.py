from config import artist_name_eminem, artist_id_eminem, artist_name_beatles, artist_id_beatles
from endpoints.artist import Artist


def test_artist_eminem():
    response = Artist('get', artist_name_eminem)
    assert response.get_status() == 200
    assert response.get_artist_id() == int(artist_id_eminem)
    assert response.get_artist_name() == artist_name_eminem


def test_artist_beatles():
    response = Artist('get', artist_id_beatles)
    assert response.get_status() == 200
    assert response.get_artist_id() == int(artist_id_beatles)
    assert response.get_artist_name() == artist_name_beatles


if __name__ == "__main__":
    pass
