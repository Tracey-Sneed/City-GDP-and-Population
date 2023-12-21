# U.S. City and GDP Analytics 2020 - 2022 

## Overview

This was an exploratory project to familiarize myself with using Python, SQL, and Power BI to clean data, transform data for querying, and present data gathered concisely. Data was collected from the U.S. Census Bureau and the Bureau of Economic Analysis. I cleaned the data using the Pandas library in Python, Pandas was used to generate new CSV files which were read into a SQLite database. I connected Power BI to the SQLite database to visualize the data.

## Data Sources

-   U.S. Census Bureau: [Metropolitan and Micropolitan Statistical Areas Totals: 2020-2022 (census.gov)](https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-metro-and-micro-statistical-areas.html)
-   Bureau of Economic Analysis: [BEA Interactive Data Application](https://apps.bea.gov/itable/?ReqID=70&step=1&_gl=1*xiubuz*_ga*MTQxNDUwMjUyNi4xNzAzMDAxNzEw*_ga_J4698JNNFT*MTcwMzExMzk4Ny4zLjEuMTcwMzExNDM4OS4yNy4wLjA.#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyOSwyNSwzMSwyNiwyNywzMF0sImRhdGEiOltbIlRhYmxlSWQiLCI1MzMiXSxbIk1ham9yX0FyZWEiLCI1Il0sWyJTdGF0ZSIsWyI1Il1dLFsiQXJlYSIsWyJYWCJdXSxbIlN0YXRpc3RpYyIsWyIzIl1dLFsiVW5pdF9vZl9tZWFzdXJlIiwiTGV2ZWxzIl0sWyJZZWFyIixbIi0xIl1dLFsiWWVhckJlZ2luIiwiLTEiXSxbIlllYXJfRW5kIiwiLTEiXV19)

## Technologies Used

-   Python
-   Pandas Library
-   SQLite3
-   PowerBI

## Data Processing

1.  **Data Collection:**
    
    -   Downloaded population and GDP data from the U.S. Census Bureau and the Bureau of Economic Analysis.
2.  **Data Cleaning:**
    
    -   Used Python and Pandas to clean and preprocess the data from the two departments.
    -   Formatted the data into new CSV files for better usability.
3.  **Database Operations:**
    
    -   Utilized SQLite to read in the CSV files generated from Python.
    -   Executed specific queries to create new tables with information about the fastest-growing metro areas or fastest-growing metros by GDP.

## PowerBI Dashboard

-   Created a PowerBI dashboard with the following steps:
    1.  Connected PowerBI to the SQLite3 database.
    2.  Imported the relevant tables and data.
    3.  Designed visualizations to represent information about the fastest-growing metro areas or metros by GDP.
    4.  Customized the dashboard for better insights.

## How to Use

1.  **Requirements:**
    
    -   Python
    -   Pandas
    -   SQLite3
    -   PowerBI
2.  **Setup:**
    
    -   Clone the repository.
    -   Install the required dependencies.
3.  **Execution:**
    
    -   Run the Python script to clean and format the data.
    -   Use SQLite3 to execute queries and generate new tables.
    -   Open the PowerBI file to view the dashboard.

## Additional Notes
The schema of the database contains only two tables. Most for the Power BI file used views created in the database.

The file paths in "gdp_estimate_data_cleaner" and "pop_estimate_data_cleaner" may need to be changed if you're attempting to run those two programs. The "Table.csv" contains the Metropolitan GDP data from the Bureau of Economic Analysis. The "cbsa-est2022(1).csv" file contains the population data from the U.S. Census Bureau. The "CBSA-EST2022.pdf" file contains notes and methodologies published by the U.S. Census Burea on "cbsa-est2022(1).csv" and similar datasets. 

The files "gdp_estimate_data_cleaner.py" and "pop_estimate_data_cleaner.py" are the python programs written to generate the files "cleaned_gdp_data.csv" and "cleaned_population_data.csv". The files "schema.sql" and "city_gdp_pop.db" are the SQL schema and database that contains the structure and database used to generate the Power BI report. The file "City GDP and Population Dashbaord.pbix" is the Power BI dashboard created using the SQL database.

Acknowledgements to The Power BI Guy and Alex the Analyst for informative Power BI and Pandas tutorials. 

> Written with [StackEdit](https://stackedit.io/).
