FROM ubuntu

WORKDIR /agents/
ARG names="1 2 3 4"

RUN for item in ${names}; do LABEL agent.name=agent${item} COPY ./agent.sh . RUN chmod +x agent.sh ENTRYPOINT ["./agent.sh"] ;done