import time
import yaml
from monitor import check_movie

with open("config/movies.yaml") as f:
    config = yaml.safe_load(f)

print("🚀 BMS Alert Bot Started")

while True:
    for movie in config["movies"]:
        check_movie(movie)

    time.sleep(300)  # 5 min
