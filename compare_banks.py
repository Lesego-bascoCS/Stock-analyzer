import pandas as pd
import matplotlib.pyplot as plt

def load_csv(path, label):
    df = pd.read_csv(path, parse_dates=['Date'])
    df = df.sort_values('Date').set_index('Date')
    df = df[['Close']].rename(columns={'Close': label})
    return df

def compare_fnbb_absa(fnbb_csv, absa_csv):
    df_fn = load_csv(fnbb_csv, 'FNBB')
    df_ab = load_csv(absa_csv, 'ABSA')
    df = pd.concat([df_fn, df_ab], axis=1).dropna()

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['FNBB'], label='FNBB (BWP)')
    plt.plot(df.index, df['ABSA'], label='ABSA (BWP)', linestyle='--')
    plt.title('FNBB vs ABSA Share Prices (Botswana Stock Exchange)')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (BWP)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    print("\nBasic Stats:")
    print(df.describe())

if __name__ == '__main__':
    # Replace with your actual CSV filenames after download
    fnbb_csv = 'fnb_history.csv'
    absa_csv = 'absa_history.csv'
    compare_fnbb_absa(fnbb_csv, absa_csv)
