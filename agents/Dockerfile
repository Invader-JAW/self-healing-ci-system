FROM ubuntu

WORKDIR /agents/

COPY ./agent.sh . 
RUN chmod +x agent.sh   
ENTRYPOINT ["./agent.sh"]