__author__ = 'Chris'


class IllegalArgumentException(Exception):

    def __init__(self, msg):

        self.msg = msg