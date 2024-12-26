import psutil
import platform
from datetime import datetime

def check_cpu_usage():
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    return "N/A"

def system_health_check():
    print("System Health Check")
    print("------------------")
    print(f"Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Operating System: {platform.system()} {platform.version()}")
    print(f"CPU Usage: {check_cpu_usage()}%")
    print(f"Memory Usage: {check_memory_usage()}%")
    print(f"Disk Usage: {check_disk_usage()}%")
    print(f"Battery Level: {check_battery()}%")

# Run the health check
system_health_check()
