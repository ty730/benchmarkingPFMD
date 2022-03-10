import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Main function for running code
    """
    # RMSE = sqrt(1/n sum( (z-z')^2 ) )
    groundTruthZ = 217.5
    df = pd.read_csv('./pfmdData/2022-03-10_19-17-07.csv')
    n = len(df['z_cm'])
    rmse = (((df['z_cm'] - groundTruthZ)**2).mean())**(1/2)
    print('RMSE:')
    print(rmse)

    gtLine = [groundTruthZ] * n
    plt.figure()
    plt.plot(df['z_cm'].index, df['z_cm'].values)
    plt.plot(df['z_cm'].index, gtLine)
    plt.legend(['PFMD', 'Ground Truth'])
    plt.title('Z axis of rotator_35')
    plt.xlabel("frames")
    plt.ylabel("z values")
    plt.show()
    

if __name__ == "__main__":
    main()