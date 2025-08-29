"""
A basic consumer script for streaming data.
Author: GitHub Copilot
"""

def consume_data():
    """Simulate consuming streaming data."""
    print("Consumer started. Waiting for data...")
    while True:
        # Simulate receiving data
        # In a real scenario, this would connect to a queue or stream
        input_data = input("Enter data to consume (or 'exit' to quit): ")
        if input_data.lower() == 'exit':
            print("Consumer stopped.")
            break
        print(f"Consumed: {input_data}")

if __name__ == "__main__":
    consume_data()
