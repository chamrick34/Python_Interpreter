__author__ = 'Chris'

import abc

class Statement(object):

    @abc.abstractmethod
    def __init__(self):
        '''
        Constructor
        '''

    @abc.abstractmethod
    def execute(self):
        return