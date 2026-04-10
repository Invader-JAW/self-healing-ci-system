# Self-Healing CI/CD Agent System

## 🚀 Overview
This project simulates a distributed CI/CD agent environment with automated monitoring and self-healing capabilities. It is designed to demonstrate how infrastructure automation can improve system reliability by detecting and recovering failed agents without manual intervention.

The system continuously monitors containerized agents, identifies failures, and automatically restarts unhealthy instances.

## 🎯 Problem
In CI/CD environments, build agents can fail due to:
- Resource exhaustion
- Crashes or unresponsive processes
- Infrastructure instability

These failures often require manual intervention, leading to:
- Increased downtime
- Slower development cycles
- Operational overhead

## 💡 Solution
This project implements a **self-healing monitoring system** that:

- Continuously inspects agent health
- Detects failed or stopped containers
- Automatically restarts unhealthy agents
- Logs system activity for visibility and debugging

## 🏗️ Architecture
+---------------------+
| CI/CD Agents |
| (Docker Containers) |
+----------+----------+
|
v
+---------------------+
| Monitoring Service |
| (Python Script) |
+----------+----------+
|
v
+---------------------+
| Docker Engine |
| (Restart / Control) |
+---------------------+

## ⚙️ Technologies Used
- Python
- Docker
- GitHub Actions (CI/CD)
- Bash scripting

## 🔧 Features
- ✅ Simulated distributed agent system using Docker containers  
- ✅ Randomized failure injection to mimic real-world instability  
- ✅ Automated detection of failed agents  
- ✅ Self-healing via automatic container restart  
- ✅ Logging system for observability  
- ✅ CI/CD pipeline integration for validation  

## ▶️ Getting Started

### Prerequisites
- Docker installed
- Python 3.10+
- Git

### 1. Clone the Repository
git clone https://github.com/your-username/self-healing-ci-system.git
cd self-healing-ci-system

2. Build Docker Image
docker build -t self-healing-system .

3. Run the System
docker run -v /var/run/docker.sock:/var/run/docker.sock self-healing-system

4. Run in Test Mode (CI)
docker run self-healing-system python monitor.py --once

📊 How It Works
1. Multiple agent containers simulate CI/CD workers
2. Agents randomly fail to simulate real-world issues
3. The monitoring service:
. Checks container health
. Identifies stopped or failed agents
4. Failed agents are automatically restarted
5. Events are logged for tracking and debugging

🔁 CI/CD Integration
- A GitHub Actions pipeline is included to:
 . Validate the monitoring script
 . Run automated checks on each commit
 . Ensure consistent behavior across environments

🧠 Key Learnings
Designing self-healing systems improves reliability and reduces manual operations
Containerization enables consistent and scalable infrastructure
Monitoring and automation are critical for modern DevOps workflows

🚀 Future Improvements
Add metrics and visualization (Grafana/Prometheus)
Deploy system using Kubernetes
Implement alerting (Slack/Email)
Scale to dynamic agent pools

💬 Author
Josh Fabrizio
DevOps Engineer | Automation & Infrastructure
---
## 📸 Demo / Output
Example log output:
Agent1 stopped
Agent1 restarted
Agent1 running