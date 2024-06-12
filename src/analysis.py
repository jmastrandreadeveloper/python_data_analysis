import matplotlib.pyplot as plt
import seaborn as sns

class Analyzer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column])
        plt.show()

    def calculate_statistics(self):
        return self.data.describe()
