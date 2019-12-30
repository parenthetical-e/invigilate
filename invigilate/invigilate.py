import csv


class Store():
    """Monitor some variables."""
    def __init__(self, monitor=None, update_every=1):
        self.update_every = update_every
        self.monitor = self.monitor
        self.data = {}
        for k in self.monitor:
            self.data[k] = list()

    def update(self, step, locals_dict):
        """Update the store"""
        if self.monitor:
            if (int(step) % self.update_every) == 0:
                for k in self.data:
                    self.data[k].append(locals_dict[k])


class StoreBest():
    """Monitor variables, update conditionally."""
    def __init__(self, monitor=None, intial_score=0):
        self.best_score = intial_score
        self.monitor = self.monitor
        self.data = {}
        for k in self.monitor:
            self.data[k] = list()

    def update(self, score, locals_dict):
        """Update the store, if the score has gotten better."""
        if self.monitor:
            if score > self.best_score:
                for k in self.data:
                    self.data[k].append(locals_dict[k])
