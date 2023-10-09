from matplotlib import pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))


def plot_failure():
    """Plot a failure."""
    plt.imshow(plt.imread(os.path.join(path,'failure.png')))
    plt.axis('off')


plot_failure()