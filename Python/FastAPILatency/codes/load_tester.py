# load_tester.py
import asyncio
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np
import aiohttp
from collections import defaultdict

class LoadTester:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.endpoints = {
            "fast": "/fast",
            "medium": "/medium",
            "slow": "/slow",
            "variable": "/variable"
        }
        self.results = defaultdict(list)
    
    async def make_request(self, session, endpoint):
        """Makes an HTTP request and measures response time"""
        url = f"{self.base_url}{self.endpoints[endpoint]}"
        start_time = time.time()
        
        try:
            async with session.get(url) as response:
                await response.json()
                response_time = (time.time() - start_time) * 1000  # in milliseconds
                self.results[endpoint].append(response_time)
                return response_time
        except Exception as e:
            print(f"Error in request to {url}: {e}")
            return None
    
    async def generate_load(self, endpoint, num_requests, concurrency):
        """Generates load for a specific endpoint"""
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(num_requests):
                tasks.append(self.make_request(session, endpoint))
                if len(tasks) >= concurrency:
                    await asyncio.gather(*tasks)
                    tasks = []
            
            if tasks:
                await asyncio.gather(*tasks)
    
    def calculate_percentiles(self, endpoint):
        """Calculates percentiles for response times"""
        if not self.results[endpoint]:
            return {}
        
        data = sorted(self.results[endpoint])
        return {
            "min": min(data),
            "p50": statistics.median(data),
            "p90": np.percentile(data, 90),
            "p95": np.percentile(data, 95),
            "p99": np.percentile(data, 99),
            "p999": np.percentile(data, 99.9) if len(data) >= 1000 else None,
            "max": max(data),
            "mean": statistics.mean(data),
            "stdev": statistics.stdev(data) if len(data) > 1 else 0
        }
    
    def plot_results(self):
        """Generates charts to visualize the results"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14))
        
        # Percentile bar chart
        endpoints = list(self.results.keys())
        metrics = ["p50", "p90", "p95", "p99"]
        
        x = np.arange(len(endpoints))
        width = 0.2
        
        for i, metric in enumerate(metrics):
            values = [self.calculate_percentiles(ep)[metric] for ep in endpoints]
            ax1.bar(x + i*width, values, width, label=f'{metric}')
        
        ax1.set_ylabel('Response Time (ms)')
        ax1.set_title('Response Time Percentiles by Endpoint')
        ax1.set_xticks(x + width * 1.5)
        ax1.set_xticklabels(endpoints)
        ax1.legend()
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Histogram for the variable endpoint
        if "variable" in self.results and self.results["variable"]:
            data = self.results["variable"]
            # Use logarithmic scale for data
            bins = np.logspace(np.log10(min(data)), np.log10(max(data)), 50)
            ax2.hist(data, bins=bins, alpha=0.7, color='green')
            ax2.set_xscale('log')
            ax2.set_title('Response Time Distribution (variable endpoint)')
            ax2.set_xlabel('Response Time (ms) - logarithmic scale')
            ax2.set_ylabel('Number of Requests')
            
            # Add vertical lines for percentiles
            percentiles = self.calculate_percentiles("variable")
            for metric, value in [(k, v) for k, v in percentiles.items() 
                                if k in ["p50", "p90", "p95", "p99"] and v is not None]:
                ax2.axvline(x=value, color='red', linestyle='--', alpha=0.6, 
                           label=f"{metric}: {value:.2f}ms")
            
            ax2.legend()
        
        plt.tight_layout()
        plt.savefig('latency_results.png', dpi=300)
        plt.close()
    
    def print_summary(self):
        """Prints a summary of the results"""
        for endpoint in self.results:
            print(f"\n=== Endpoint: {endpoint} ({len(self.results[endpoint])} requests) ===")
            percentiles = self.calculate_percentiles(endpoint)
            for metric, value in percentiles.items():
                if value is not None:
                    print(f"{metric}: {value:.2f} ms")

async def main():
    tester = LoadTester()
    
    # Generate load for each endpoint
    print("Starting load tests...")
    
    for endpoint in tester.endpoints:
        requests = 1000 if endpoint == "variable" else 200
        print(f"Testing endpoint '{endpoint}' with {requests} requests...")
        await tester.generate_load(endpoint, requests, concurrency=50)
    
    # Print results and generate charts
    tester.print_summary()
    tester.plot_results()
    print("Tests completed. Results saved in 'latency_results.png'")

if __name__ == "__main__":
    asyncio.run(main())