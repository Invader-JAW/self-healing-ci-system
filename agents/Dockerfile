FROM ubuntu

WORKDIR /agents/
ARG names="agent1 agent2 agent3 agent4"

RUN for item in ${names}; do LABEL agent.name=${names} COPY ./agent.sh . RUN chmod +x agent.sh ENTRYPOINT ["./agent.sh"] ;done