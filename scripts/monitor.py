import docker
import time
import sys
client = docker.from_env()

RUN_ONCE = "--once" in sys.argv
MAX_RUNS = 5

runs = 0

while True:
    containers = client.containers.list(all=True)
    for c in containers:
        print(c.name, c.status)
        
        if c.status != "running":
            c.restart()
            print(c.name, "restarted")
            with open("log.txt", "a") as f:
                f.write(f"{c.name} restarted\n")
    runs += 1
    if runs >= MAX_RUNS:
        print("Completed monitoring cycles, exiting gracefully.")
        break
    time.sleep(5)
