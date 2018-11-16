FROM rabbitmq

COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

RUN rabbitmq-server & \
    rabbitmqctl wait --timeout 35 /var/run/rabbitmq/pid; \
    rabbitmqctl add_user user pass; \
    rabbitmqctl add_vhost vhost; \
    rabbitmqctl set_permissions -p vhost user ".*" ".*" ".*"; \
    rabbitmqctl stop
