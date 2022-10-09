from pathlib import Path
import os
import json
import requests


# config
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = os.path.join(BASE_DIR, 'config.json')

with open(JSON_PATH, 'r') as f:
    json_data = json.load(f)

def get_data(func):
    pass


# API
class FionApi:

    def __init__(self, nickname, matchtype) -> None:
        self._headers = {'Authorization':json_data['API_KEY']}
        self._nickname = nickname
        self._matchtype = matchtype
        self._offset = 0
        self._limit = 100

    ## Get metadata
    def MetaData(self, type: str):
        '''
        type = 'matchtype', 'spid', 'seasonid', 'spposition', 'division', 'division_volta' 중 한개 선택
        '''
        req = requests.get(f'https://static.api.nexon.co.kr/fifaonline4/latest/{type}.json', headers=self._headers)
        data = req.json()
        return data

    def GetActionShot(self, id: int):
        '''
        type = spid, pid 중 하나 선택.  
                     -> pid는 spid의 뒤 6자리.
        '''
        try: # action shot
            req = requests.get(f'https://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/p{id}.png', headers=self._headers)
            data = req.json()
        except Exception as e: # error 발생 시 normal shot
            req = requests.get(f'https://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/players/p{id}.png', headers=self._headers)
            data = req.json()
        return data

    ## Get user data
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
        return data




    
# if __name__ == '__main__':
#     api = FionApi('매기구이')
#     print(api.UserInfomation())


# decorator를 쓰기에는 좀 복잡한데 차라리 상속을 받아 쓰는게 나은가?