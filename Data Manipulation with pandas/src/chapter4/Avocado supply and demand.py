import matplotlib.pyplot as plt
import pandas as pd

avocados = pd.read_pickle("../../Datasets/avoplotto.pkl")

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
