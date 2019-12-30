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


def save_store(name, store):
    """Save the data in the store, as csv"""
    if store.monitor:
        with open(name, 'w') as csv_file:
            keys = sorted(store.data.keys())
            values = [store.data[k] for k in keys]
            w = csv.writer(csv_file)
            w.writerow(keys)
            for row in zip(*values):
                w.writerow(row)


def load_store(name, store):
    """Load saved data into a store"""
    pass
