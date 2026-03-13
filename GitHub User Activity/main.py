
from controllers.controllers import GithubActivityController

def main():
    print("="*25,'GitHub User Activity',"="*25)
    username = input("username : ")

    # Avoir les evenments publics depuis le dernier
    result = GithubActivityController.get_github_activity(username)
    oldest_event = result[-1]['created_at']
    print(f"Events   : {len(result)}")
    print(f"Since    : {oldest_event[0:10]}")
    print(f"Types    :")

    temp = []

    for i in result:
        temp.append(i["type"])

    tuple_ = tuple(temp)
    eventpush = []

    for eachEvent in tuple_:
        if eachEvent not in eventpush:
            eventpush.append(eachEvent)
    for e in eventpush:
        print(f"    → {e}")

    # Avoir tous les repos que l'utilisateur a fait PushEvent
    # temp = []
    #
    # for i in result:
    #     if i["type"] == "PushEvent":
    #         temp.append(i["repo"]["name"])
    #
    # tuple_ = tuple(temp)
    # eventpush = []
    #
    # for eachEvent in tuple_:
    #     if eachEvent not in eventpush:
    #         eventpush.append(eachEvent)
    #
    #
    # print("Voici une liste des repos que vous avez commit :")
    # nombre = 0
    # for e in eventpush:
    #     for val in tuple_:
    #         if val == e:
    #             nombre += 1
    #     print(f"Pushed {nombre} commits to {e}")
    #     nombre = 0





if __name__ == '__main__':
    main()
