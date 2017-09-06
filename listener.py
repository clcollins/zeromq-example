#!/usr/bin/env python3

import zmq
import argparse

parser = argparse.ArgumentParser(description="ZMQ listener")
parser.add_argument('--conn',
                    '-c',
                    action='store',
                    dest='connection',
                    default="tcp://localhost:5556",
                    type=str,
                    help=('connection information in the format'
                          '"tcp://hostname:port"; default is '
                          'tcp://localhost:5556')
                    )

parser.add_argument('--queue',
                    '-q',
                    action='store',
                    dest='queue',
                    default="",
                    type=str,
                    help=('message queue to listen to'
                          '(really just a filter); default is all ')
                    )

args = parser.parse_args()

context = zmq.Context()
socket = context.socket(zmq.SUB)

connection = "tcp://localhost:5556"

print("Connecting to %s" % args.connection)
socket.connect(args.connection)

print("Listening for \"%s\" events" % args.queue)
socket.setsockopt_string(zmq.SUBSCRIBE, args.queue)

while True:
    print("received event: " + socket.recv_string())
