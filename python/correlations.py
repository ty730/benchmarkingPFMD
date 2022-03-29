import sys
import pandas as pd
import os
from matplotlib import pyplot as plt

def main():
	x = sys.argv[1]
	y = sys.argv[2]
	
	directory = "./data/"
	for path in os.listdir(directory):
		curr = pd.read_csv(directory + path)
		if (x not in curr.columns) & (y not in curr.columns):
			print("Invalid x or y input")
		else:
			plt.plot(curr[x], curr[y], label=path)
			plt.title(x + " v.s. " + y)
			plt.xlabel(x)
			plt.ylabel(y)
	plt.legend()
	plt.show()


if __name__ == "__main__":
    main()