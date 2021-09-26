#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""
ENQUEUE = 1
DEQUEUE = 2
PRINT_TOP = 3


class Stack:
    def __init__(self):
        self.stack_list = []
        
    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

        
class Queue:
    """
    Main idea to tackle corner cases (that cause the execution taking too long) 
    is to keep a "buffer stack" (stack1) for recently enqueued items, 
    and transfer items from "buffer stack" to stack2 only when stack2 is empty.
    Obs: stack2 will always have items sorted as LIFO, making it fast (O(1)) to dequeue and get front_element.
    """
    def __init__(self):
        self.stack1 = Stack() # sorted by LIFO 
        self.stack2 = Stack() # sorted by FIFO

    def enqueue(self, element):
        self.stack1.push(element)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                item = self.stack1.pop()
                self.stack2.push(item)

        return self.stack2.pop()    
    
    def front_element(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                item = self.stack1.pop()
                self.stack2.push(item)

        return self.stack2.peek()


def processQueries(queue, queries):
    for query in queries:
        operation = query[0]

        if operation == ENQUEUE:
            element = query[1]
            queue.enqueue(element)
        elif operation == DEQUEUE:
            queue.dequeue()
        elif operation == PRINT_TOP:
            print(queue.front_element())
    

if __name__ == '__main__':
    number_of_queries = int(input())
    
    queries = []
    for _ in range(number_of_queries):
        queries.append(list(map(int, input().split())))
        
    queue = Queue()

    processQueries(queue, queries)
