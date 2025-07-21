import matplotlib.pyplot as plt
import os


class Plotter:
    '''
    The class is for making the graphs of temperature and wind data.
    '''
    @staticmethod
    def plot(df, column, title, ylabel, filename):
        '''
        plot function will plot the graph
        '''
        plt.figure(figsize=(10, 6))
        plt.plot(df["time"], df[column], marker='o', linestyle='-')
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel(ylabel)
        plt.grid(True)
        os.makedirs("output/plots", exist_ok=True)
        plt.savefig(f"output/plots/{filename}")
        plt.close()
