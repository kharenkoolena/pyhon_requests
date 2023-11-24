import requests


class Artist:

    def __init__(self, request_type, artist_name_or_id):
        if request_type == 'get':
            self.response = requests.get(f"https://api.deezer.com/artist/{artist_name_or_id}")
        elif request_type == 'post':
            pass
        elif request_type == 'delete':
            pass
        else:
            raise ValueError(f"Unsupported request type: {request_type}")

    def get_status(self):
        return self.response.status_code

    def get_artist_id(self):
        return self.response.json()['id']

    def get_artist_name(self):
        return self.response.json()['name']
