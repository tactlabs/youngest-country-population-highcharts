import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    #print(df['states'].tolist())

    country                                     = df['Country'].tolist()
    population                                  = df['Population'].tolist()
    data_list =[]
    for row in df.values:
        print(row[0])
        curent_dict = {
            "name" : row[0],
            "y" : row[1]
        }
        data_list.append(curent_dict)
    
    result = {
        "data_list" : data_list 

    }
    return result
    # result_dict = {
    #     'Country'                                    : country,
        
    #      'data_list'              : [{
    #          "name":"Population",
    #          "y":population
    #      }
    #      ]
    # }

    # print(result_dict)

    # return result_dict

def add_row(country, population):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Country'       : country, 
        'Population'        : population
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()