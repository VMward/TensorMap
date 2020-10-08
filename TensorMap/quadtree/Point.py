import numpy as np

class Point:
    """A point located at (x,y) in 2D space.

    Each Point object may be associated with a payload object.

    """

    def __init__(self, x, y, payload=None):
        self.x, self.y = x, y
        self.payload = payload

    def __repr__(self):
        return '{}: {}'.format(str((self.x, self.y)), repr(self.payload))
    def __str__(self):
        return 'P({:.2f}, {:.2f})'.format(self.x, self.y)

    def distance_to(self, other):
        try:
            other_x, other_y = other.x, other.y
        except AttributeError:
            other_x, other_y = other
        return np.hypot(self.x - other_x, self.y - other_y)
