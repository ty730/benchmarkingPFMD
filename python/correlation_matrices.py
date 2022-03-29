import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

GROUND_TRUTH_Z = 217.5

def main():	
	directory = "./data/"
	for path in os.listdir(directory):
		curr = pd.read_csv(directory + path)
		curr.dropna(inplace=True)
		curr.drop(["id", "datetime"], axis=1, inplace=True)
		curr["rmse"] = (((curr["z_cm"] - GROUND_TRUTH_Z)**2).mean())**(1/2)
		col = curr.columns
		curr = curr.to_numpy()
		
		print("Correlation matrix for " + path)
		print()
		print(col)
		matrix = np.corrcoef(curr, rowvar=False)
		matrix = pd.DataFrame(matrix, columns=col, index=col)
		print(matrix)
		print(matrix['rmse'])
		print()
		print()


if __name__ == "__main__":
    main()