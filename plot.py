import matplotlib.pyplot as plt
from recaman import get_recaman_seq


def plot_recaman_circle(max_size=100, arcs=True, circles=False):
    seq = get_recaman_seq(max_size=max_size)
    plt.axes()

    for i, value in enumerate(seq):
        print(i, value)
        circle = plt.Circle(
            (value, 0), radius=i/2, fill=False)
        plt.gca().add_patch(circle)

    plt.axis('scaled')
    plt.show()


plot_recaman_circle(max_size=1000)
