#!/usr/bin/env python

#
class TaskSet:

    #
    def __init__(self, taskList):
        self.taskList = taskList

    #
    def addTask(self, task):
        self.taskList.append(task)

    #
    def processorUtilisation(self):
        init = 0.0
        for task in self.taskList:
            init = init + task.processorUtilisation()

        return init


