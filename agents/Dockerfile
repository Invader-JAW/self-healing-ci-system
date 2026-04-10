FROM ubuntu

RUN -d --name agent1 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
RUN -d --name agent2 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
RUN -d --name agent3 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
RUN -d --name agent4 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"

COPY ./agent.sh agent1:/bin/agent.sh
COPY ./agent.sh agent2:/bin/agent.sh
COPY ./agent.sh agent3:/bin/agent.sh
COPY ./agent.sh agent4:/bin/agent.sh