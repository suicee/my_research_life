from matplotlib import pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))


def plot_success():
    """Plot a temporary success."""
    raise NotImplementedError("Success is not implemented yet.")
    # plt.imshow(plt.imread(os.path.join(path,'failure.png')))
    # plt.axis('off')


plot_success()