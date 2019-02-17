# RabbitMQ Credentials tests

Runs a simple loopback test

## Usage

example shows default values

```
docker run -it --rm \
-e RABBITMQ_HOST="localhost" \
-e RABBITMQ_PORT="5672" \
-e RABBITMQ_VIRTUAL_HOST="/" \
-e RABBITMQ_USER="guest" \
-e RABBITMQ_PASSWORD="guest"  \
jonaseck/rabbitmq-credentials-test
```