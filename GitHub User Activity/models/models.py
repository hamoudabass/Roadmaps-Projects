import urllib.request
import urllib.parse
import json

class GithubActivity:

    @staticmethod
    def get_github_activity(username):
        with urllib.request.urlopen(f"https://api.github.com/users/{username}/events/public?per_page=100&page=1") as response:
            # contenu = json.dumps(json.loads(response.read().decode('UTF-8')),indent=4)
            contenu =json.loads(response.read().decode('UTF-8'))
        return contenu








