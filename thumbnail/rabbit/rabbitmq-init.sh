rabbitmq-server & wait
rabbitmqctl wait --timeout 35 /rabbitmq-pid
rabbitmqctl add_user user pass
rabbitmqctl add_vhost vhost
rabbitmqctl set_permissions -p vhost user ".*" ".*" ".*"
rabbitmqctl set_user_tags user administrator
