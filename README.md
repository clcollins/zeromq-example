ZMQ Example
===========

Sample Docker containers implementing a ZeroMQ PUB/SUB model. The publisher script creates dummy events with "queues" named "SPINACH", "CARROT", "PICKLE", & "LEEK", on which the subscriber can listen.

How to build
------------

    docker-compose build


How to run
----------

To run the default setup (Subscriber listens to "PICKLE" queue/filter):

    docker-compose up


The `listener.py` script takes arguments:

    /listener.py -h
    usage: listener.py [-h] [--conn CONNECTION] [--queue QUEUE]
    
    ZMQ listener
    
    optional arguments:
      -h, --help            show this help message and exit
      --conn CONNECTION, -c CONNECTION
                            connection information in the
                            format"tcp://hostname:port"; default is
                            tcp://localhost:5556
      --queue QUEUE, -q QUEUE
                            message queue to listen to(really just a filter);
                            default is all

The arguments can be changed in the docker-compose file.
