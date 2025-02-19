import requests
import concurrent.futures

TOKEN_FILE = "tokens.txt"
VALID_TOKENS_FILE = "valid.txt"
FLAGGED_TOKENS_FILE = "flagged.txt"

def get_headers(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

def check_token(token):
    url = "https://discord.com/api/v9/users/@me"
    response = requests.get(url, headers=get_headers(token))

    if response.status_code == 200:
        print(f"✅ Valid token: {token[:20]}...")
        with open(VALID_TOKENS_FILE, "a") as f:
            f.write(token + "\n")
    elif response.status_code == 403:
        print(f"⚠ Flagged token: {token[:20]}...")
        with open(FLAGGED_TOKENS_FILE, "a") as f:
            f.write(token + "\n")
    else:
        print(f"❌ Invalid token: {token[:20]}...")

def check_tokens():
    with open(TOKEN_FILE, "r") as f:
        tokens = [line.strip() for line in f.readlines()]

    print(f"🔍 Checking {len(tokens)} token...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_token, tokens)

    print("✅ Done! saved all results to `valid.txt` and `flagged.txt`.")

if __name__ == "__main__":
    check_tokens()