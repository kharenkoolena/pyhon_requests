import config
from endpoints.search import Search


def test_search_track_by_track_title():
    response = Search('get', 'track', config.track_title)
    assert response.get_status() == 200
    assert response.is_track_title_presented_in_all_results(config.track_title)
    assert response.get_track_title(config.track_id) == config.track_title
    assert response.is_track_id_presented(config.track_id)
    assert response.get_track_artist_name(config.track_id) == config.track_artist_name


def test_search_track_by_artist_name():
    response = Search('get', 'artist', config.artist_name_beatles)
    assert response.get_status() == 200
    assert response.is_artist_name_presented_in_all_results(config.artist_name_beatles)
    assert response.get_track_title(config.artist_track_id_beatles) == config.artist_track_title_beatles
    assert response.is_track_id_presented(config.artist_track_id_beatles)
    assert response.get_track_artist_name(config.artist_track_id_beatles) == config.artist_name_beatles


if __name__ == "__main__":
    pass
