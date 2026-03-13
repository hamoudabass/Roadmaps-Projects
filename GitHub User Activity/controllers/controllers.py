

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

    @staticmethod
    def get_events_detail(data,event_type : str):
        # Avoir tous les repos que l'utilisateur a fait PushEvent
        temp = []
        events = ['PushEvent', 'CreateEvent', 'WatchEvent', 'ForkEvent']

        type_ev = (event_type.strip()).lower()


        for e in events:
            if e.lower() == type_ev :
                event_type = e


        if event_type == 'PushEvent':

            for i in data:
                if i["type"] == event_type:
                    temp.append(i["repo"]["name"])

            tuple_ = tuple(temp)
            eventpush = []

            for eachEvent in tuple_:
                if eachEvent not in eventpush:
                    eventpush.append(eachEvent)

            nombre = 0
            for e in eventpush:
                for val in tuple_:
                    if val == e:
                        nombre += 1
                print(f"Pushed {nombre} commits to {e}")
                nombre = 0

        elif event_type == 'ForkEvent':
            for i in data:
                if i["type"] == event_type:
                    temp.append(i["payload"]["forkee"]["full_name"])

            tuple_ = tuple(temp)
            forked_repos = []

            for eachEvent in tuple_:
                if eachEvent not in forked_repos:
                    forked_repos.append(eachEvent)

            nombre = 0
            for e in forked_repos:
                for val in tuple_:
                    if val == e:
                        nombre += 1
                print(f"  → Forked {nombre} time(s) : {e}")
                nombre = 0

        elif event_type == 'CreateEvent':
            for i in data:
                if i["type"] == event_type:
                    ref_type = i["payload"]["ref_type"]  # "repository", "branch", ou "tag"
                    ref = i["payload"]["ref"]  # nom de la branche/tag (None si repository)
                    repo = i["repo"]["name"]
                    temp.append((repo, ref_type, ref))

            tuple_ = tuple(temp)
            created_repos = []

            for eachEvent in tuple_:
                if eachEvent not in created_repos:
                    created_repos.append(eachEvent)

            for e in created_repos:
                repo, ref_type, ref = e
                if ref_type == "repository":
                    print(f"  → Created repository : {repo}")
                elif ref_type == "branch":
                    print(f"  → Created branch [{ref}] in {repo}")
                elif ref_type == "tag":
                    print(f"  → Created tag [{ref}] in {repo}")

        elif event_type == 'WatchEvent':
            for i in data:
                if i["type"] == event_type:
                    repo = i["repo"]["name"]
                    created_at = i["created_at"][:10]
                    temp.append((repo, created_at))

            tuple_ = tuple(temp)
            watched_repos = []

            for eachEvent in tuple_:
                if eachEvent[0] not in [r[0] for r in watched_repos]:
                    watched_repos.append(eachEvent)

            nombre = 0
            for repo, date in watched_repos:
                for val_repo, _ in tuple_:
                    if val_repo == repo:
                        nombre += 1
                print(f"  → Starred {repo} ({nombre} time(s) — last on {date})")
                nombre = 0

        elif event_type == 'CommitCommentEvent':
            for i in data:
                if i["type"] == event_type:
                    repo = i["repo"]["name"]
                    comment = i["payload"]["comment"]["body"]
                    commit = i["payload"]["comment"]["commit_id"][:7]  # SHA court
                    temp.append((repo, commit, comment))

            for repo, commit, comment in temp:
                print(f"  → Commented on commit [{commit}] in {repo}")
                print(f"     \"{comment[:60]}{'...' if len(comment) > 60 else ''}\"")


        elif event_type == 'DeleteEvent':
            for i in data:
                if i["type"] == event_type:
                    repo = i["repo"]["name"]
                    ref_type = i["payload"]["ref_type"]  # "branch" ou "tag"
                    ref = i["payload"]["ref"]
                    temp.append((repo, ref_type, ref))

            for repo, ref_type, ref in temp:
                print(f"  → Deleted {ref_type} [{ref}] in {repo}")


        elif event_type == 'IssueCommentEvent':
            for i in data:
                if i["type"] == event_type:
                    repo = i["repo"]["name"]
                    action = i["payload"]["action"]  # "created", "edited", "deleted"
                    issue = i["payload"]["issue"]["title"]
                    comment = i["payload"]["comment"]["body"]
                    temp.append((repo, action, issue, comment))

            for repo, action, issue, comment in temp:
                print(f"  → {action.capitalize()} comment on issue \"{issue}\" in {repo}")
                print(f"     \"{comment[:60]}{'...' if len(comment) > 60 else ''}\"")


        elif event_type == 'PullRequestEvent':
            for i in data:
                if i["type"] == event_type:
                    repo = i["repo"]["name"]
                    action = i["payload"]["action"]  # "opened", "closed", "merged"...
                    title = i["payload"]["pull_request"]["head"]["repo"]["name"]
                    number = i["payload"]["pull_request"]["number"]
                    merged = i["payload"]["pull_request"]["merged"]
                    temp.append((repo, action, title, number, merged))

            for repo, action, title, number, merged in temp:
                if action == "closed" and merged:
                    label = "Merged"
                else:
                    label = action.capitalize()
                print(f"  → {label} PR #{number} \"{title}\" in {repo}")