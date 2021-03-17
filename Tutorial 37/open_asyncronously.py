from open_website import list1, fetch
from timeit import default_timer
import requests
import asyncio

async def open_website():
    with requests.Session() as session:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(None,fetch,session,website) for website in list1]
        for response in await asyncio.gather(*tasks):
            print(response)

if __name__ == "__main__":
    start = default_timer()
    asyncio.run(open_website())
    total_time = default_timer() - start
    print(total_time, "seconds")