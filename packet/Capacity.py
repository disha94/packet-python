

class Capacity():
    def __init__(self, data):
        self.capacity = data

    def __str__(self):
        return "%s" % 'Available'

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.capacity)
