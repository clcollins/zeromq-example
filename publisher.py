#!/usr/bin/env python3

import zmq
import random
import string
import time
import argparse
import json

def randword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


parser = argparse.ArgumentParser(description="ZMQ listener")
parser.add_argument('--conn',
                    '-c',
                    action='store',
                    dest='connection',
                    default="tcp://*:5556",
                    type=str,
                    help=('connection information in the format'
                          '"tcp://hostname:port"; default is '
                          'tcp://localhost:5556')
                    )

args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.PUB)

print("Binding to %s" % args.connection)
socket.bind(args.connection)

while True:
    # Simulate events

    # Pick a random queue
    queues = ['SPINACH', 'CARROT', 'PICKLE', 'LEEK']
    queue = queues[random.randint(0,3)]

    # Generate a random message
    actions = ['chop', 'eat', 'cook', 'compost']
    action = actions[random.randint(0,2)]
    randaction = randword(8)

    message = {}
    message = {'action': action, 'item': randaction}

    # Send the message to the queue
    event = ("{0} {1}".format(queue, message))

    print("sending event: " + event)
    socket.send_string(event)

    # Sleep a bit or we'll just peg out the CPU
    time.sleep(random.randint(1,5))

