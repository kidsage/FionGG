from pathlib import Path
import os
import json
import requests


# config
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = os.path.join(BASE_DIR, 'config.json')

with open(JSON_PATH, 'r') as f:
    json_data = json.load(f)


# API
class FionApi:

    def __init__(self, nickname, matchtype) -> None:
        self._headers = {'Authorization':json_data['API_KEY']}
        self._nickname = nickname
        self._matchtype = matchtype
        self._offset = 0
        self._limit = 100

        
    def PlayerList(self):
        req = requests.get(f'https://static.api.nexon.co.kr/fifaonline4/latest/spid.json', headers=self._headers)
        data = req.json()
        return data

    def MatchList(self):
        req = requests.get(f'https://static.api.nexon.co.kr/fifaonline4/latest/matchtype.json', headers=self._headers)
        data = req.json()
        


    def UserInfomation(self):
        req = requests.get(f'https://api.nexon.co.kr/fifaonline4/v1.0/users?nickname={self._nickname}', headers=self._headers)
        data = req.json()
        return data

    def UserMatchInformation(self):
        api = FionApi(self._nickname)
        api_data = api.UserInfomation()

        req = requests.get(f'https://api.nexon.co.kr/fifaonline4/v1.0/users/{api_data["accessid"]}\
                            /matches?matchtype={self._matchtype}&offset={self._offset}&limit={self._limit}',
                            headers=self._headers)
        data = req.json()





    
# if __name__ == '__main__':
#     api = FionApi('매기구이')
#     print(api.UserInfomation())