"""
A basic producer script for streaming data.
Author: GitHub Copilot
"""

import time
import random

def produce_data():
    """Simulate producing streaming data."""
    while True:
        data = {
            'timestamp': time.time(),
            'value': random.randint(1, 100)
        }
        print(f"Produced: {data}")
        time.sleep(1)

if __name__ == "__main__":
    produce_data()
