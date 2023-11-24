import requests


class Search:

    def __init__(self, request_type, key, value):
        if request_type == 'get':
            self.response = requests.get(f"https://api.deezer.com/search?q={key}:'{value}'", params={'lang': 'en'})
        else:
            raise ValueError(f"Unsupported request type: {request_type}")

    def get_status(self):
        return self.response.status_code

    def get_presented_track_ids(self):
        return [result['id'] for result in self.response.json().get('data', [])]

    def is_track_id_presented(self, result_id):
        return int(result_id) in self.get_presented_track_ids()

    def is_track_title_presented_in_all_results(self, track_title):
        return track_title in [track['title'] for track in self.response.json().get('data', [])]

    def get_track_details_index(self, track_id):
        for index, track in enumerate(self.response.json().get('data', [])):
            if track['id'] == int(track_id):
                return index

    def get_track_title(self, track_id):
        index = self.get_track_details_index(track_id)
        return self.response.json()['data'][index]['title']

    def get_track_artist_name(self, track_id):
        index = self.get_track_details_index(track_id)
        return self.response.json()['data'][index]['artist']['name']

    def is_artist_name_presented_in_all_results(self, artist_name: str) -> bool:
        return artist_name in [artist['artist']['name'] for artist in self.response.json().get('data', [])]
