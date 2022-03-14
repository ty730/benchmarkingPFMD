import pandas as pd
import os
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error

GROUND_TRUTH_Z = 217.5 # cm


def main():
  directory = "./to_plot/"
  stats_dict = {"file name": [], "z data": [], "z rmse": [], "n": []}
  for path in os.listdir(directory):
    curr = pd.read_csv(directory + path)
    rmse = (((curr["z_cm"] - GROUND_TRUTH_Z)**2).mean())**(1/2)
    print("RMSE (cm): " + str(rmse))
    stats_dict["file name"].append(path)
    stats_dict["z data"].append(curr['z_cm'])
    stats_dict["z rmse"].append(rmse)
    stats_dict["n"].append(len(curr))

  stats_df = pd.DataFrame(stats_dict)
  count = len(stats_df)
  fig, axs = plt.subplots(count)
  
  for i in range(count):
    curr_data = stats_df.iloc[i]
    y_actual = curr_data["z data"]
    y_pred = [GROUND_TRUTH_Z] * len(y_actual)
    y = y_actual - y_pred
    x = [n for n in range(len(y_actual))]
	
    axs[i].plot(x, y)
    axs[i].set_title(curr_data["file name"] + 
				" with RMSE " + 
				f'{curr_data["z rmse"]:.3f}')
    axs[i].set_xlabel("sample")
    axs[i].set_ylabel("z difference (cm)")
  fig.tight_layout()
  plt.show()


if __name__ == "__main__":
    main()
