"""
  Simple buffer class implemenation.
  Example usages:
    buf = Buffer(5)
    buf.add(1, 2, 3)
    print(buf.get_current_part())
"""


class Buffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.buff = []

    def add(self, *a):
        self.buff.extend(a)
        self.flush()

    def flush(self):
        while len(self.buff) >= self.capacity:
            head = self.buff[:self.capacity]
            print("Sum: {} Min: {} Max: {} Avg: {} Values: {}".format(
                sum(head), min(head), max(head), sum(head) // self.capacity, head))
            self.buff = self.buff[5:]

    def get_current_part(self):
        return self.buff


if __name__ == "__main__":
    buf = Buffer(5)
    buf.add(1, 2, 3)
    print(buf.get_current_part())
    buf.add(4, 5, 6)
    print(buf.get_current_part())
    buf.add(7, 8, 9, 10)
    print(buf.get_current_part())
