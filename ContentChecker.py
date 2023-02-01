import requests
import json 

class AIContentChecker:
    def __init__(self, text):
        self.text = text
        self.url = 'https://s5.zerogpt.com/detectText'
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.zerogpt.com',
            'Referer': 'https://www.zerogpt.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS'
        }
        self.real = None
        self.fake = None
        self.response = None

    def check_text(self):
        text_to_check = self.text
        text_to_check_dump = json.dumps({"text":text_to_check})
        data = json.loads(text_to_check_dump)
        response = requests.post(self.url, headers=self.headers, json=data).json()
        self.real, self.fake = response['robertaScoreParagraph']['real']*100, response['robertaScoreParagraph']['fake']*100
        self.response = response
        
