from timeit import default_timer
list1 = ["http://www.ndpma.org","http://www.nd.edu","http://www.google.com","http://www.youtube.com","http://www.yahoo.com","http://www.bing.com","http://www.github.com","http://www.discord.com","http://www.amazon.com","http://www.espn.com"]

def fetch(session,url):
    start = default_timer()
    with session.get(url) as response:
        total = default_timer() - start
        data = response.text
        return f"{response.status_code} {url} {len(data)} bytes read {total} seconds"
