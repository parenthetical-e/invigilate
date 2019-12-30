"""Export functions for Stores"""

# This submodule will have several sometimes tedious to install
# external dependencies.
# I want to make them clearly optional.


class Tensorboard():
    """Wrap a store so it seamlessly logs to tensorboard"""
    def __init__(self, store):
        pass


def hdf5(save, store):
    """Export to HDF5"""
    pass


def cdf(save, store):
    """Export to CDF"""
    pass


def json(save, store):
    """Export to json"""
    pass


def delimited(save, store, sep="\t", fmt=None):
    """Export to any kind of delimited table -- csv,tsv,unix

    Offers fine grained control over seperation, the header,
    and fmt
    """
    pass
