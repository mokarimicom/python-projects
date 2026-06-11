import psutil
import GPUtil
import os
import time

def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    print(f"CPU Usage: {cpu_percent}%")
    if cpu_freq:
        print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    print(f"CPU Cores: {cpu_cores}")
    print(f"CPU Threads: {cpu_threads}")
    print("-" * 30)

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        print("No GPU detected.")
    for gpu in gpus:
        print(f"GPU Name: {gpu.name}")
        print(f"GPU Load: {gpu.load * 100:.1f}%")
        print(f"GPU Memory Free: {gpu.memoryFree}MB")
        print(f"GPU Memory Used: {gpu.memoryUsed}MB")
        print(f"GPU Memory Total: {gpu.memoryTotal}MB")
        print(f"GPU Temperature: {gpu.temperature} °C")
        print("-" * 30)

if __name__ == "__main__":
    os.system('cls')  # Clear CMD window (for Windows)
    print("=== System Performance Monitor ===")
    get_cpu_info()
    get_gpu_info()
while True:
    os.system('cls')
    print("=== System Performance Monitor ===")
    get_cpu_info()
    get_gpu_info()
    time.sleep(2)