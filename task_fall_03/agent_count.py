#!/usr/bin/env python
import pika
import sys
import datetime
from threading import Timer

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = ["info", "warn", "error"]

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

clients = []
n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
e = 0.01

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    t = datetime.datetime.now()
    for i in range(len(clients)):
        # print abs(t - datetime.timedelta(seconds= n) - clients[i])
        if abs(t - datetime.timedelta(seconds= n) - clients[i]) < datetime.timedelta(seconds= e):
            clients[i] = t
            break
    else:
        clients.append(t)
        print("Number of clients: %d" % len(clients))

def check_clients():
    t = datetime.datetime.now()
    num = len(clients)
    Timer(n, check_clients).start()

    for el in clients:
        if (t - el) > datetime.timedelta(seconds= n + e):
            clients.remove(el)
    if num != len(clients):
        print("Number of clients: %d" % len(clients))

check_clients()

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()