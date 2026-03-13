from models.models import GithubActivity
from views.views import GithubActivityView

class GithubActivityController:

    @staticmethod
    def get_github_activity(username):
        try:
            activity = GithubActivity.get_github_activity(username)
            GithubActivityView.display_success("Github activity succefully fetched !")
            return activity

        except Exception as e:
            GithubActivityView.display_error(e)
            return None