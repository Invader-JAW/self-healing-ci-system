import docker
import time
client = docker.from_env()

while True:
    containers = client.containers.list(all=True)
    for c in containers:
        print(c.name, c.status)
        
        if c.status != "running":
            c.restart()
            with open("log.txt", "a") as f:
                f.write(f"{c.name} restarted\n")
    time.sleep(5)
