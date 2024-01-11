# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__) 

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results from the precipitation analysis (i.e. only the last 12 months of data)
       to a dictionary using date as the key and prcp as the value."""
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Convert the query results from the last 12 months of precipitation data into a dictionary
    precip_data_12_months = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date <= '2017-08-23').\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()
    
    session.close()
    
    precip_raw_data = []
    for date, prcp in precip_data_12_months:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_raw_data.append(precip_dict)

    return jsonify(precip_raw_data)


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query all stations
    stations = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def temperature():
    """Query the dates and temperature observations of the most-active station for the previous year of data."""
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Using the most active station id
    # Query the last 12 months of date and temperature observation data for this station
    temp_data_12_months = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date <= '2017-08-23').\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).all()
    
    session.close()
    
    # Return a JSON list of temperature observations for the previous year
    dates_and_temps = list(np.ravel(temp_data_12_months))

    return jsonify(dates_and_temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature 
        for a specified start date, or for a specific date range, or a 404 if date(s) not found."""
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # If no end date is entered
    # Query the minimum temperature, the average temperature, and the maximum temperature for all dates greater than 
    # or equal to a specified date
    
    
    # Search Measurement table for a specific date
    date_picked == session.query(Measurement.date).filter(Measurement.date == start).all()
    
    for date in date_picked:
    if date_picked == start:
        # Query the minimum temperature, the average temperature, and the maximum temperature beginning with a specified date
        min_avg_max_temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), 
                                          func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        order_by(Measurement.date).all()

        session.close()

        # Return a JSON list of the minimum, average, and maximum temperature observations beginning with a specified date
        temp_data = []
        for temps in min_avg_max_temps:
            temp_data.append(temps)

        return print(f"Date selected: {start}")
        return jsonify(temp_data)

    return jsonify({"error": f"Date {start} not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)


