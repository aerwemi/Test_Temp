import pandas as pd

def get_city():
    df=pd.read_csv("data/city_data_mrg.csv", encoding = "ISO-8859-1", index_col=0)
    dfcolumns=df.columns
    data={}
    for column in dfcolumns:
        data[column]=df[column].tolist()
    return data


if __name__ == '__main__':
    data = get_city()
    print(data)
