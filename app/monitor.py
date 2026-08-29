import json
from scraper import get_showtimes
from notifier import send_message

STATE_FILE = "data/state.json"

def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def check_movie(movie):
    state = load_state()

    name = movie["name"]
    current = get_showtimes(movie["url"], movie.get("theatre_filter"))

    old = set(state.get(name, []))
    new = set(current) - old

    if new:
        send_message(f"🎬 {name}\nNew shows added:\n" + "\n".join(new))

    state[name] = list(current)
    save_state(state)
