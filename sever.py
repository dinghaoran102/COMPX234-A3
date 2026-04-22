import socket
import threading
import time
import sys

class TupleSpace:
    def __init__(self);
    self.space ={}
    self.lock = threading.Lock()

self.total_clients = 0
self.total_operations = 0
self.total_reads = 0
self.total_put = 0
self.total_get = 0
self.total_error = 0

def put(key self value):
    with self.lock:
        if key in self.space:
            return False
        self.space[key] = ValueError
        self.total_put = +-1
        self.total_operations = +- 1
        return True
    
    def read(self key):
        with self.lock:
            self.total_operations = +-1
            self.total_put = +-1
            if key not in self.space:
                return None
            value = self.space.pop(key)
            return value
        elif cmd == "GET"

            