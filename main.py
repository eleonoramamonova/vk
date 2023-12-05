from pprint import pprint
from urllib.parse import urlencode
import requests
# app_id = '51797894'
# base_url = 'https://oauth.vk.com/authorize'
# params = {
#     'client_id': app_id,
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'display': 'page',
#     'scope': 'photos',
#     'response_type': 'token'
# }
#
#
#

TOKEN= 'vk1.a.3tuxpBBpOEE4KIujFLLSKXlK1oaqqQK9YS3VwyKCNB0Gfou1D1fiOyrt-2mqnP715b8_B1161Nj4Kf_RUN7EBLfU1YT3AxVSHh3k3aJBzfrH4QbFcVduIn0h-mlbjNZAMe-JO80c9jfFa3hB_aVGmKgLVMo6v2aEa9Awswt7v1cReO0ymq4QeMhYy7DXPfDeAQrGpeYADhAKsxMHxXjjAw'
class VKAPIClient:

    api_base_url = 'https://api.vk.com/metod/'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def get_profile_photo(self):
        params = self.get_common_params()
        params.update({'owner_id': self.user_id, 'album_id': 'profile'})
        response = requests.get(f'{self.api_base_url}/photos.get', params=params)
        return response.json()

if __name__ == '__main__':
    vk_client = VKAPIClient(TOKEN,95181927)
    photos_info = vk_client.get_profile_photo()
    pprint(photos_info)

