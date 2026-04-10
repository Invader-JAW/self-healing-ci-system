FROM ubuntu

WORKDIR /scripts/

# RUN -d --name agent1 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
# RUN -d --name agent2 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
# RUN -d --name agent3 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
# RUN -d --name agent4 ubuntu bash -c "chmod +x /bin/agent.sh & /bin/agent.sh"
#RUN find . -name "agent.sh" -printf "%h\n"
COPY . .
#RUN find / -name "agent.sh" ls -R
RUN ls -R
# COPY /home/runner/work/self-healing-ci-system/self-healing-ci-system/scripts/agent.sh agent1:/bin/agent.sh
# COPY /home/runner/work/self-healing-ci-system/self-healing-ci-system/scripts/agent.sh agent2:/bin/agent.sh
# COPY /home/runner/work/self-healing-ci-system/self-healing-ci-system/scripts/agent.sh agent3:/bin/agent.sh
# COPY /home/runner/work/self-healing-ci-system/self-healing-ci-system/scripts/agent.sh agent4:/bin/agent.sh