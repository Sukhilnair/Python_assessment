import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        time.sleep(1)

def main():
    threshold = 80  # Define your threshold here (e.g., 80%)
    monitor_cpu(threshold)

if __name__ == "__main__":
    main()