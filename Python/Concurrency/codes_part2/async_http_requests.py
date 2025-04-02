import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """Fetch a URL asynchronously"""
    start = time.time()
    async with session.get(url) as response:
        data = await response.text()
        elapsed = time.time() - start
        return {
            'url': url,
            'status': response.status,
            'size': len(data),
            'time': elapsed
        }

async def fetch_all(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    # List of URLs to fetch
    urls = [
        'https://www.python.org',
        'https://docs.python.org',
        'https://www.github.com',
        'https://www.google.com',
        'https://www.wikipedia.org',
    ]
    
    # Sequential fetching for comparison
    start = time.time()
    async with aiohttp.ClientSession() as session:
        results = []
        for url in urls:
            results.append(await fetch_url(session, url))
    sequential_time = time.time() - start
    
    print(f"Sequential fetching: {sequential_time:.2f} seconds")
    
    # Concurrent fetching
    start = time.time()
    results = await fetch_all(urls)
    concurrent_time = time.time() - start
    
    print(f"Concurrent fetching: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time/concurrent_time:.2f}x")
    
    # Display results
    for result in results:
        print(f"{result['url']}: {result['status']} ({result['size']} bytes, {result['time']:.2f}s)")

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())

# Sequential fetching: 2.26 seconds
# Concurrent fetching: 0.80 seconds
# Speedup: 2.83x
# https://www.python.org: 200 (51012 bytes, 0.12s)
# https://docs.python.org: 200 (17129 bytes, 0.11s)
# https://www.github.com: 200 (281297 bytes, 0.80s)
# https://www.google.com: 200 (16957 bytes, 0.46s)
# https://www.wikipedia.org: 200 (88783 bytes, 0.36s)