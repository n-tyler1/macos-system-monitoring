# macOS System Metrics Monitor (Prometheus + Grafana)

A Docker-based monitoring stack that collects system metrics (CPU, memory, disk) from your **macOS host machine** and visualizes them using Prometheus and Grafana.

> 📝 **Note**: This setup monitors the macOS host system where Docker is running. The metrics reflect your Mac's actual CPU, memory, and disk usage.

## Architecture

- **Python Exporter**: Custom metrics exporter that collects system metrics using `psutil`
- **Prometheus**: Time-series database that scrapes and stores metrics
- **Grafana**: Visualization platform for creating dashboards

## Prerequisites

- Docker Desktop for Mac
- Docker Compose (`docker compose` command)  
- macOS (tested on macOS 10.15+)

## Project Structure

```
.
├── docker-compose.yml
├── exporter/
│   ├── Dockerfile
│   ├── system_metrics_exporter.py
│   └── requirements.txt
└── prometheus/
    └── prometheus.yml
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/n-tyler1/macos-system-monitoring.git
   cd macos-system-monitoring
   ```

2. **Start the stack**:
   ```bash
   docker compose up -d
   ```

3. **Verify services are running**:
   ```bash
   docker compose ps
   ```
   
   You should see three services running: `exporter`, `prometheus`, and `grafana`.

## Accessing the Services

- **Metrics Exporter**: http://localhost:8080/metrics
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000

### Prometheus Metrics & Query Examples

| Metric Name | Description | Unit |
|-------------|-------------|------|
| `system_cpu_usage_percent` | Current CPU usage | Percent |
| `system_memory_usage_percent` | Current memory usage | Percent |
| `system_disk_usage_percent` | Current disk usage (root partition) | Percent |


In Prometheus (http://localhost:9090), try these queries:

```promql
# Current CPU usage
system_cpu_usage_percent

# Average CPU usage over 5 minutes
avg_over_time(system_cpu_usage_percent[5m])

# Memory usage trend
rate(system_memory_usage_percent[1m])
```

### Change Grafana Admin Credentials

> ⚠️ Security Note: The default Grafana login is admin / admin.
Change these credentials before deploying publicly.

Edit `docker-compose.yml`:
```yaml
grafana:
  environment:
    - GF_SECURITY_ADMIN_USER=your_username
    - GF_SECURITY_ADMIN_PASSWORD=your_secure_password
```
Or change them after logging in at http://localhost:3000

### Setting Up Dashboards

1. Log in to Grafana at http://localhost:3000
2. Go to **Configuration** → **Data Sources** → **Add Data source**
3. Choose **Prometheus**
4. Set URL to: `http://prometheus:9090`
5. Click **Save & Test**
6. Create a new dashboard and add panels for:
    - `system_cpu_usage_percent`
    - `system_memory_usage_percent`
    - `system_disk_usage_percent`

## Stopping the Stack
To stop:
```bash
docker compose down
```

To remove all containers and data volumes:
```bash
docker compose down -v
```
⚠️ Note: Without persistent volumes, metrics and dashboards reset after down -v.

## Contributing

Feel free to open issues or submit pull requests for improvements!