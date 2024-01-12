# sqlalchemy-challenge

# Analyzing and Exploring Climate Data
* Used SQLAlchemy to create an engine to connect to the SQLite database and explore the 'climate_starter' and 'hawaii' files.

* Reflected the tables into the 'station' and 'measurement' classes using the automap_base function.

* Created a SQLAlchemy session to link Python to the database.

## Precipitation Analysis
1. Found the most recent date in the dataset.

2. Utilized AskBCS to create a query to obtain the previous 12 months of precipitation data.

3. Selected only the 'date' and 'prcp' values, loaded the query results into a Pandas DataFrame, and explicitly set the column names.

4. Utilized AskBCS properly format the plot method to show the results. 

5. Calculated and printed the summary statistics.

## Station Analysis
1. Created a query to calculate the total number of stations in the dataset.

2. Created a query to find the most active stations, then listed them in order, and displayed the station with the greatest number of observations.

3. Created a query to calculate the lowest, highest, and average temperatures of the most active station.

4. Created a query to get the previous temperature observatio (TOBS) data.

5. closed the session.

# Designing the Climate App
* Designed a Flask API based on queries to:
1. Start at the homepage and list all available routes.

2. Convert the results from the precipitation analysis into a dictionary using the 'date' and 'prcp' as the key:value pair.

3. Return a JSON list of the stations in the dataset.

4. Obtain the dates and temperature observations of the most active station for the previous year of data and return a JSON list of those temperature observations.

5. Worked with a tutor to return a JSON list of minimum, average, annd maximum temperatures for a specific start or start-end range.
* Values calculated for specified start - for all dates greater than or equal to the start date.
* Values calculated for specified start and end dates - for all dates from start date to end date, inclusive.

