import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    #print(df['states'].tolist())

    country                                     = df['Country'].tolist()
    population                                  = df['Population'].tolist()
   

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'country'                                    : country,
        'population'                                :  population,
        
       
        # 'data_list'         : list_of_tuples
    }

    # print(result_dict)

    return result_dict

# def add_row(Lake, Area):

#     df = pd.read_csv('data.csv') 

#     new_row = {
    
#         'Lake'       : Lake, 
#         'Area'        : Area
#     }

#     print(df)

#     df = df.append(new_row, ignore_index=True)

#     print(df)

#     df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()