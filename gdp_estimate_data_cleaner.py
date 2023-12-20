import pandas as pd

#The data we want is contained in the file called "Table"
#We just want to reformat the data so SQL can easily perform a join.
#We want to strip "(Metropolitan Statistical Area)" from the Geo name
#We want to delete columns "2017", "2018" and "2019"

def main():

    #this is the name of the file that has the data we're reading from
    data_frame = pd.read_csv(r"C:\Users\sneed\OneDrive\Desktop\City GDP Data Analytics Project\Table.csv", skiprows=3)
    print(data_frame)

    #deleting the years we don't want
    data_frame = data_frame.drop(["2017","2018","2019"], axis = 'columns')

    #This makes it easier for SQL to work with the Data
    for data in range(0,len(data_frame)):
        if "(Metropolitan Statistical Area)" in str(data_frame.loc[data].at["GeoName"]):
           data_frame.replace(data_frame.loc[data].at["GeoName"], data_frame.loc[data].at["GeoName"].split(" (")[0], inplace=True)
        else:
            data_frame = data_frame.drop(data) 
    print(data_frame)

    data_frame.to_csv(r"C:\Users\sneed\OneDrive\Desktop\City GDP Data Analytics Project\cleaned_gdp_data.csv", index=False)

if __name__ == "__main__":
    main()