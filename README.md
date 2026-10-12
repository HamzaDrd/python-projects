# 🐍 Python Projects

A collection of small Python projects I'm building to learn the language — one concept at a time,
with tests and clean code for each.

![CI](https://github.com/HamzaDrd/python-projects/actions/workflows/ci.yml/badge.svg)

## Progress

<!-- PROGRESS:START -->
| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 01 | [hello-world](projects/01-hello-world) | functions, f-strings, testing | ✅ Done |
<!-- PROGRESS:END -->

## Repository layout

```
python-projects/
├── projects/
│   └── 01-hello-world/
│       ├── README.md        # what the project does + what I learned
│       ├── main.py          # entry point
│       └── test_main.py     # tests
├── new_project.py           # scaffolds the next project
├── conftest.py              # lets each project test its own main.py
├── pyproject.toml           # shared tooling config (pytest, ruff)
├── requirements-dev.txt     # dev dependencies
└── .github/workflows/ci.yml # runs lint + tests on every push
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

python new_project.py "number guessing game"   # create the next project
pytest                                          # run every test
ruff check . && ruff format .                   # lint + format
```

## Roadmap

Ordered from easiest to hardest. Projects that call an online service need an API key —
keep those in a `.env` file (already ignored by git), never in the code.

### 1. Beginner — games & small utilities
- [x] Hello world
- [ ] Number guessing game
- [ ] Word guessing game
- [ ] Hangman
- [ ] 21 number game
- [ ] Rock paper scissors
- [ ] Higher-lower game
- [ ] Cows and bulls
- [ ] Mastermind
- [ ] Flames game
- [ ] 2048
- [ ] Pokémon training game
- [ ] Fun fact generator
- [ ] Countdown timer
- [ ] Convert emoji into text
- [ ] Compare two PDFs
- [ ] Creating payment receipts
- [ ] Attendance tracker
- [ ] Taking screenshots
- [ ] Screen recorder
- [ ] Voice recorder
- [ ] Desktop notifier
- [ ] Live weather notifications
- [ ] Global hotkey listener (pynput)

### 2. Tkinter — desktop GUIs
- [ ] First GUI application
- [ ] Calculator
- [ ] Loan calculator
- [ ] Compound interest calculator
- [ ] Rank-based percentile calculator
- [ ] Age calculator
- [ ] Unit converter
- [ ] Weight conversion
- [ ] Digital clock
- [ ] Countdown timer (GUI version)
- [ ] Calendar
- [ ] Create table
- [ ] Registration form
- [ ] Marksheet
- [ ] To-do application
- [ ] Notepad
- [ ] File explorer
- [ ] Image viewer
- [ ] Slideshow application
- [ ] Voice recorder (GUI version)
- [ ] Color game
- [ ] Switch between page frames
- [ ] Spell corrector
- [ ] Sentiment detector
- [ ] Weather forecast
- [ ] Live USD/INR rate
- [ ] COVID-19 data representation
- [ ] Extract lyrics from a song
- [ ] Search installed applications
- [ ] Shutdown, restart and log out from PC
- [ ] Screen rotation
- [ ] Text detection
- [ ] Visiting card scanner

### 3. Web scraping
- [ ] Email ID extractor
- [ ] Scraping weather data
- [ ] Scraping Reddit
- [ ] COVID-19 vaccine tracker
- [ ] Automating scrolling
- [ ] Scrape content from dynamic websites
- [ ] Scrape most-reviewed news and tweet it
- [ ] Extraction of tweets
- [ ] Scraping data from Google Maps
- [ ] Fetch data from Jira
- [ ] Predicting air quality index

### 4. Automation
- [ ] Automate backups
- [ ] Send automated emails
- [ ] Birthday mail
- [ ] Google search
- [ ] Software testing
- [ ] Convert Python 2 code to Python 3
- [ ] Hotword detection
- [ ] WhatsApp messages
- [ ] WhatsApp Web without scanning the QR code
- [ ] Instagram messages
- [ ] Birthday post on Facebook
- [ ] Bulk posting on Facebook
- [ ] LinkedIn connections
- [ ] Trading

### 5. Bots & advanced tools
- [ ] Auto clicker
- [ ] Auto-typer (PyAutoGUI)
- [ ] Auto-login bot
- [ ] Product availability checker
- [ ] File sharing app
- [ ] Hotel management system
- [ ] Fetch Gmail of a user
- [ ] Telegram bot
- [ ] Send message to a Telegram user
- [ ] WhatsApp bot
- [ ] WhatsApp birthday bot
- [ ] Twitter bot
- [ ] Twitter sentiment analysis
- [ ] Instagram bot
- [ ] Corona help bot
