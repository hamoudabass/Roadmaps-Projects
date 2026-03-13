class GithubActivityView :
    @staticmethod
    def display_events_types(eventpush):
        for e in eventpush:
            print(f"    → {e}")

    @staticmethod
    def display_success(message):
        """Affiche un message de succès"""
        print(f"\n✓ {message}\n")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur"""
        print(f"\n✗ Erreur: {message}\n")


def main():
    pass


if __name__ == '__main__':
    main()