# Problem 1: Duplicate Tracker
def has_duplicates(product_ids):
    """
    We use a set because it enforces uniqueness and provides O(1) average-time lookups.
    As we iterate through product_ids, we check if an element is already in the set.
    If yes, return True immediately; otherwise add it. This is efficient compared to nested loops.
    Overall runtime: O(n), space: O(n).
    """
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False


# Problem 2: Order Manager
from collections import deque

class TaskQueue:
    """
    We use a queue (collections.deque) because tasks must be processed in the order added (FIFO).
    Adding to the back and removing from the front are both O(1) operations in deque, unlike a list
    which would take O(n) for front removals.
    """
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)  # O(1)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()  # O(1)
        return None


# Problem 3: Unique Value Counter
class UniqueTracker:
    """
    We use a set to maintain only unique values from the stream.
    Adding an element and checking for existence are O(1) on average.
    The unique count is simply the size of the set, which is O(1) to retrieve.
    """
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)
