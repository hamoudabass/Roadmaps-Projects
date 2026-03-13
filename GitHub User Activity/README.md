# GitHub Activity CLI

GitHub Activity CLI is a command line interface that allows you to fetch and explore the recent public activity of any GitHub user directly in your terminal.

## 📦 Installation

```bash
git clone https://github.com/hamoudabass/github-activity-cli.git
```

## 🛠 Usage

```bash
python main.py
```

Example menu :

```
======================== GitHub User Activity ========================

  Enter GitHub username : hamoudabass

1. Fetch user activity
2. Show event details
3. Change GitHub user
4. Exit

Select an option :
```

Example output :

```
  Select an option : 1

==================================================

✓ Github activity succefully fetched !

  Username : hamoudabass
  Events   : 70
  Since    : 2026-02-18
  Types    :
    → PushEvent
    → CreateEvent
    → WatchEvent
    → ForkEvent

    Press Enter to continue...
──────────────────────────────────────────────────

  Select an option : 2

  Enter event type : PushEvent

──────────────────────────────────────────────────
  Details — PushEvent
──────────────────────────────────────────────────

  → Pushed 6 commits to hamoudabass/Roadmaps-Projects
  → Pushed 9 commits to hamoudabass/Computer-Science
  → Pushed 12 commits to hamoudabass/Task-Tracker-CLI
  → Pushed 7 commits to hamoudabass/hamoudabass
  → Pushed 7 commits to hamoudabass/Drapeau-de-DJibouti

──────────────────────────────────────────────────
```

## 🎯 Features

- Fetch recent public activity of any GitHub user
- Filter activity by event type (PushEvent, ForkEvent, CreateEvent, WatchEvent, etc.)
- Show detailed information per event type
- Change GitHub user without restarting the program

## 📂 Project Structure

```
github-activity-cli/
├── main.py
├── controllers/
│   └── controllers.py
├── models/
│   └── models.py
└── views/
    └── views.py
```

## 🧰 Tech Stack

* Python 3.11
* GitHub REST API — `https://api.github.com/users/{username}/events`

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/name`)
3. Commit your changes (`git commit -m 'Adding a feature'`)
4. Push to the branch (`git push origin feature/name`)
5. Open a Pull Request

## 🙌 Credits

Inspired by [RoadMap.sh](https://roadmap.sh) — [GitHub User Activity Project](https://roadmap.sh/projects/github-user-activity)

## 👤 Author

**Hamoud Abass** – Passionate Developer!
