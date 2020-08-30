"""
$ python3 gpt.py
{'predictions': [[765, 1681, 1359, 1061, 1624, 6294, 5511, 5675, 2741, 3117, 1646, 5626, 729, 611, 1645, 1856, 2037, 2843, 246, 6354, 6362, 6352, 3367, 2355]]}
"""
import re
import requests 
from tokenizers import BertWordPieceTokenizer


tokenizer = BertWordPieceTokenizer('clue-vocab.txt', lowercase=True)
 

def gpt(text,
        length=20,
        SERVER_URL='http://localhost:8506/v1/models/gpt:predict'):
    token = tokenizer.encode(text, add_special_tokens=False).ids
    r = requests.post(SERVER_URL, json={
        'instances': [{
            'inp': token,
            'length': length
        }]
    })
    return tokenizer.decode(r.json()['predictions'][0])


if __name__ == '__main__':
    print(gpt('你好啊'))

