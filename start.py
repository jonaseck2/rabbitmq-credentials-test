#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import pika
import os

config = {
  'rabbitmq': {
    'host': 'localhost',
    'port': 5672,
    'virtual_host': '/',
    'user': 'guest',
    'password': 'guest',
  }
}

for section in config:
    for key,value in config[section].items():
        env = os.getenv(section.upper() + '_' + key.upper())
        if env:
            print("%s_%s=\"%s\" as %s" % (section.upper(), key.upper(), env, type(value)))
            config[section][key] = type(value)(env)

config['rabbitmq']['credentials'] = pika.PlainCredentials(config['rabbitmq'].pop('user'), config['rabbitmq'].pop('password'))
connection = pika.BlockingConnection(pika.ConnectionParameters(**config['rabbitmq']))
channel = connection.channel()

channel.queue_declare(queue='test')

# publish
body='Hello World!'
print(" [x] Sent %r" % body)
channel.basic_publish(exchange='',
                      routing_key='test',
                      body=body)

# subscribe
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    connection.close()

channel.basic_consume(callback,
                      queue='test',
                      no_ack=True)

channel.start_consuming()
