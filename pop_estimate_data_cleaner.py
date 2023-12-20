import pandas as pd

#The data we want is contained in the file called "cbsa-est2022(1)"
#It has a lot of extraneous data we don't care about.
#We only want rows that have "Metropolitan Statistical Data" in the "Legal/Statistical Area Description"
#We want to delete columns "CBSA", "MDIV" and "STCOU"

def main():

    #this is the name of the file that has the data we're reading from
    data_frame = pd.read_csv(r"C:\Users\sneed\OneDrive\Desktop\City GDP Data Analytics Project\cbsa-est2022 (1).csv")
    print(data_frame)
    data_frame = data_frame.drop(["CBSA","MDIV","STCOU"], axis = 'columns')

    for data in range(0,len(data_frame)):
        if data_frame.loc[data].at["LSAD"] != "Metropolitan Statistical Area":
           data_frame = data_frame.drop(data) 
    print(data_frame)

    data_frame.to_csv(r"C:\Users\sneed\OneDrive\Desktop\City GDP Data Analytics Project\cleaned_population_data.csv", index=False)

if __name__ == "__main__":
    main()