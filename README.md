---

Discord Token Checker

A fast and efficient Discord token checker that validates tokens, detects flagged ones, and sorts them into separate files.

Features

Multi-threaded for high-speed checking
Detects valid, flagged, and invalid tokens
Saves results automatically
Easy to use – just run the script!


---

Installation

1. Clone the repository

git clone https://github.com/long191910/discord-token-checker.git

cd discord-token-checker


2. Install dependencies

pip install requests




---

Usage

1. Add your tokens

Save your tokens in a file named tokens.txt (one token per line).



2. Run the script

python check.py


3. View results

Valid tokens → valid.txt

Flagged tokens → flagged.txt





---

Example Output

Checking 100 tokens...
Valid token: MzA1NDY3ODkwMTIzN...
Flagged token: NzQyNTY3MDI5MTIzN...
Invalid token: MzA1NDY3ODkwMTIzN...
Done! Saved all results to `valid.txt` and `flagged.txt`.


---

How It Works

Reads tokens from tokens.txt

Uses multi-threading to check multiple tokens simultaneously

Queries Discord API to determine token status

Saves valid and flagged tokens separately



---

Notes

Avoid checking too many tokens too fast to prevent rate limits.

This script is for educational purposes only. Misuse may result in account suspension.



---

License

MIT License – Free to use and modify.


---
