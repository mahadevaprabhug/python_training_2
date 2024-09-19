"""
seaborn: plotting graphs
"""

print("iris data:")
print("-"*20)
# --------------

import pandas as pd
iris_data = pd.read_csv("Iris.csv")
print(iris_data)

print("#"*40, end="\n\n")
################################

print("Violinplot Graph-1")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=iris_data)
plt.show()

print("#"*40, end="\n\n")
################################

print("Graph: Violinplot  Graph-2")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=iris_data, x="Species", y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
################################

print("Graph: Violinplot  Graph-3")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=iris_data, x="SepalWidthCm", y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
################################

print("Graph: scatterplot  Graph-3")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(data=iris_data, x="SepalWidthCm", y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
################################

print("Graph: lineplot  Graph-1")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=iris_data, x="SepalWidthCm", y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
################################

print("Graph: lineplot  Graph-2")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=iris_data, x="Species", y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
################################
