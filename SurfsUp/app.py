# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)


# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create a session
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return """
    <h1>Welcome to the Weather API</h1>
    <ul>
        <li><a href="/api/v1.0/precipitation">Precipitation</a></li>
        <li><a href="/api/v1.0/stations">Stations</a></li>
        <li><a href="/api/v1.0/tobs">Tobs</a></li>
        <li><a href="/api/v1.0/start">Start</a></li>
        <li><a href="/api/v1.0/start/end">Start/End</a></li>
    </ul>
    """

@app.route("/api/v1.0/precipitation")
def precipitation():
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date()

    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Save the query results as a Pandas DataFrame. Explicitly set the column names
    precipitation_df = pd.DataFrame(precipitation_data, columns=['date', 'precipitation'])

    # Sort the dataframe by date
    precipitation_df_sorted = precipitation_df.sort_values(by='date')

    # Ensure the DataFrame has the correct structure with 'date' as the index
    precipitation_df_sorted.set_index('date', inplace=True)

    result = precipitation_df_sorted['precipitation'].to_dict()

    return jsonify(result)

@app.route("/api/v1.0/stations")
def stations():
    # Query the required columns (id, station, name)
    results = session.query(Station.id, Station.station, Station.name).all()

    result = [{'id': row[0], 'station': row[1], 'name': row[2]} for row in results]

    return jsonify(result)

@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date()

    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    tobs_data = session.query(Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()

    result = [result[0] for result in tobs_data]

    return jsonify(result)

@app.route('/api/v1.0/<start>', methods=['GET'])
def get_temp_stats_after_start_date(start):
    # Convert the date strings to datetime objects
    try:
        start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    
    # Query the minimum, average, and maximum temperature for dates greater than or equal to the start date
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    print(temp_stats)

    # Extract the temperature statistics from the query results
    min_temp = temp_stats[0][0]
    avg_temp = temp_stats[0][1]
    max_temp = temp_stats[0][2]

    # Create a dictionary to hold the temperature statistics
    result = {
        "TMIN": min_temp,
        "TAVG": avg_temp,
        "TMAX": max_temp
    }

    return jsonify(result)

@app.route('/api/v1.0/<start>/<end>', methods=['GET'])
def get_temp_stats_between_dates(start, end):
    # Convert the date strings to datetime objects
    try:
        start_date = dt.datetime.strptime(start, '%Y-%m-%d')
        end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    # Query the minimum, average, and maximum temperature for dates greater than or equal to the start date
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all() 

    print(temp_stats)

    # Extract the temperature statistics from the query results
    min_temp = temp_stats[0][0]
    avg_temp = temp_stats[0][1]
    max_temp = temp_stats[0][2]

    # Create a dictionary to hold the temperature statistics
    result = {
        "TMIN": min_temp,
        "TAVG": avg_temp,
        "TMAX": max_temp
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
