

class Capacity():
    def __init__(self, data):
        self.capacity = data['capacity']

    def __str__(self):
        return "%s" % self.capacity

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.capacity)