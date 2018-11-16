FROM rabbitmq


COPY rabbitmq.conf /etc/rabbitmq/
COPY rabbitmq-init.sh /

ENV RABBITMQ_PID_FILE=/rabbitmq-pid NODENAME=rabbit@localhost
RUN touch /rabbitmq-pid; \
    mkdir -p /var/log/rabbitmq/log; \
    touch /var/log/rabbitmq/log/crash.log; \
    chmod +666 /rabbitmq-pid /var/log/rabbitmq/log/crash.log;

CMD ["./rabbitmq-init.sh"]
