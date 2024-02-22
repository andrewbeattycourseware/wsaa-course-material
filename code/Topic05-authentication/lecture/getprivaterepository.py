import requests
import json
#from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# this token is no longer valid, becuase it has been pushed to GitHub
# GitHub detects it and invalidates it automatically for security
apikey='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'
# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

#apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
