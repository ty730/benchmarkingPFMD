import pandas as pd

def main():
    """
    Main function for running code
    """
    # RMSE = sqrt(1/n sum( (z-z')^2 ) )
    groundTruthZ = 217.5
    df = pd.read_csv('./pfmdData/2022-03-10_19-17-07.csv')
    n = len(df['z_cm'])
    rmse = (((df['z_cm'] - groundTruthZ)**2).mean())**(1/2)
    print(rmse)


if __name__ == "__main__":
    main()