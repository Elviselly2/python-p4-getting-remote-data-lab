import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Sends a GET request to the initialized URL and returns the response body as text."""
        response = requests.get(self.url)
        return response.content

    pass

    def load_json(self):
        """Parses the response body as JSON and returns a Python dictionary or list."""
        response_body = self.get_response_body()
        return json.loads(response_body)

    pass