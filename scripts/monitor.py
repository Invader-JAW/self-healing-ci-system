import docker
import time
import sys
client = docker.from_env()

RUN_ONCE = "--once" in sys.argv

while True:
    containers = client.containers.list(all=True)
    for c in containers:
        print(c.name, c.status)
        
        if c.status != "running":
            c.restart()
            with open("log.txt", "a") as f:
                f.write(f"{c.name} restarted\n")
    if RUN_ONCE:
        break
    time.sleep(5)
