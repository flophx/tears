#!/usr/bin/env python

#
class Task:

    #
    def __init__(self, name, wcet, deadline, period):
        self.name = name
        self.wcet = int(wcet)
        self.deadline = int(deadline)
        self.period = int(period)

    #
    def processorUtilisation(self):
        pU =  (1.0 *self.wcet)/self.period
        return pU

