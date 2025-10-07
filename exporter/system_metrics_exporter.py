from prometheus_client import start_http_server, Gauge
import psutil
import time

# Prometheus metrics
# system_cpu_usage_percent
# system_memory_usage_percent
# system_disk_usage_percent
CPU_USAGE = Gauge("system_cpu_usage_percent", "Current CPU usage")
MEMORY_USAGE = Gauge("system_memory_usage_percent", "Current memory usage")
DISK_USAGE = Gauge("system_disk_usage_percent", "Current disk usage")

def collect_metrics():
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage("/").percent)

if __name__ == "__main__":
    start_http_server(8080)  # container listens on 8080
    print("Exporter running on port 8080")
    while True:
        collect_metrics()
        time.sleep(5)