FROM ubuntu

WORKDIR /agents/

LABEL agent.name="agent1"
COPY ./agent.sh .
RUN chmod +x agent.sh
ENTRYPOINT ["./agent.sh"]
