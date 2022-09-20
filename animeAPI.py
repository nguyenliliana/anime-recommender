import random
import urllib
import json
from urllib import error, request
id = 2


class AnimeAPI():
    def __init__(self):
        self.url = f'https://api.jikan.moe/v4/random/anime'

    def get_random_anime(self) -> None:
        self.data = self._download_url(self.url)

    def print_data(self):
        # print(self.data['data']['title'])
        # print(self.data['data']['synopsis'])
        list = []
        list.append(self.data['data']['title'])
        list.append(self.data['data']['synopsis'])
        list.append(self.data['data']['rating'])
        list.append(self.data['data']['episodes'])
        list.append(self.data['data']['status'])
        list.append(self.data['data']['year'])
        list.append(self.data['data']['images']['jpg']['image_url'])
        # print(list)
        return list

    def _download_url(self, url: str) -> dict:
        # TODO: Implement web api request code in a way that supports ALL types of web APIs
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            code = e.code
            print('Status code: {}'.format(code))
            if code == 401:
                print('The API key provided is invalid.')
            elif code == 404 or code == 503:
                print('The remote API is unavailable.')
        except urllib.error.URLError as e:
            print('Failed to download contents of URL')
            print('Loss of local connection to the Internet.')

        finally:
            if response != None:
                response.close()

        return r_obj


def grab_data():
    # a = AnimeAPI()
    # a.load_data()
    # list = a.print_data()
    # print(list)
    # return list
    randomizer = AnimeAPI()
    randomizer.get_random_anime()
    list = randomizer.print_data()

    return list


if __name__ == '__main__':
    a = AnimeAPI()
    a.load_data()
    a.print_data()
