import requests

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
answer = {'answer': open('answer.json', 'rb')}

submit = requests.post(url=url+token, files=answer)

print(submit.status_code, submit.text)