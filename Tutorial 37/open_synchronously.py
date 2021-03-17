from open_website import list1, fetch
from timeit import default_timer
import requests

def open_website():
    with requests.Session() as session:
        for website in list1:
            print(fetch(session,website))

if __name__ == "__main__":
    start = default_timer()
    open_website()
    total_time = default_timer() - start
    print(total_time, "seconds")