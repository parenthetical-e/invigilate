"""Export functions for Stores"""

# This submodule will have several sometimes tedious to install
# external dependencies.
# I want to make them clearly optional.


class Tensorboard():
    """Wrap a store so it seamlessly logs to tensorboard"""
    def __init__(self, name, store):
        pass


def save_hdf5(name, store):
    """Export to HDF5"""
    pass


def load_hdf5(name):
    """Load an HDF5 based store"""
    pass


def save_cdf(name, store):
    """Export to CDF"""
    pass


def load_cdf(name):
    """Load an CDF based store"""
    pass


def save_json(name, store):
    """Export to json"""
    pass


def load_json(name):
    """Load a json based store"""
    pass


def save_pkl(name, store):
    """Export to cloudpickle"""
    pass


def load_pkl(name):
    """Load a cloudpickle based store"""
    pass


def save_delimited(name, store, sep="\t", fmt=None):
    """Export to any kind of delimited table -- csv,tsv,unix

    Offers fine grained control over seperation, the header,
    and fmt
    """
    pass


def load_delimited(name, sep="\t", fmt=None):
    """Load a table based store"""
    pass