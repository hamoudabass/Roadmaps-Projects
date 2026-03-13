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

    @staticmethod
    def get_events_types(result):
        try :
            temp = []

            for i in result:
                temp.append(i["type"])

            tuple_ = tuple(temp)
            events = []

            for eachEvent in tuple_:
                if eachEvent not in events:
                    events.append(eachEvent)

            GithubActivityView.display_events_types(events)

            return events

        except Exception as e:
            GithubActivityView.display_error(e)
            return None