import matplotlib.pyplot as plt


class Essentials:
    def __init__(self) -> None:
        pass

    def make_plt(self, plot_parameters: tuple, data: tuple, location: str, visibility: tuple):
        """Create the axces system for the input data frames"""
        
        ax = plt.subplot2grid(*plot_parameters[:2], rowspan=plot_parameters[2], colspan=plot_parameters[3])
        s1, = ax.plot(data[0]["cm-1"], data[0]["%T"], '-r', label=1, antialiased=True)
        s2, = ax.plot(data[1]["cm-1"], data[1]["%T"], '-g', label=2, antialiased=True)
        s3, = ax.plot(data[2]["cm-1"], data[2]["%T"], '-b', label=3, antialiased=True)
        s1.set_visible(visibility[0])
        s2.set_visible(visibility[1])
        s3.set_visible(visibility[2])
        # s4.set_visible(True)
        ax.set_xlabel("cm-1")
        ax.set_ylabel("%T")
        ax.set_title(f"Transmition vs wave number ({location})")
        ax.legend(loc="lower right")
        ax.grid()
        plt.tight_layout()
        return ax
