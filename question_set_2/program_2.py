"""
Write a program to create a circular queue using dictionaries in python Maximum length of the queue is 5:
if it crosses the maximum length it has to delete the latest added element in the queue and add the new element to the queue

"""

class CircularQueueUsingDict:
    """Circular queue using dictionary"""
    def __init__(self):
        self.cir_queue = {}
        self.latest_elem = None
        self.index = 0
    def add_elem(self, elem):
        if self.index<5:
            self.cir_queue[self.index] = elem
            self.index += 1
            print("Current Queue Elements")
            print(self.cir_queue)
        else:
            self.index -= 1
            self.cir_queue[self.index] = elem
            print("Current Queue Elements")
            print(self.cir_queue)
            self.index +=1

    def demo_cir_queue_working(self):
        self.add_elem("one")
        self.add_elem("two")
        self.add_elem("three")
        self.add_elem("four")
        self.add_elem("five")
        self.add_elem("six")
        self.add_elem("seven")


