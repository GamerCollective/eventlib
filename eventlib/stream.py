"""Stream module"""


class Stream(object):
    def __init__(self, name, stream, serialization):
        self.name = name
        self.stream = stream
        self.serialization = serialization
