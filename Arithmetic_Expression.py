__author__ = 'Hamrick'

import abc


class Arithmetic_Expression(object):

    def __init__(self):
        '''
        Constructor
        '''

    @abc.abstractmethod
    def evaluate(self):
        return