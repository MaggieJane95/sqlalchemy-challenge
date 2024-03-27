# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
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
    return (f"Welcome to my Climate App API <br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/percipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start<br/>"
            f"/api/v1.0/start/end<br/>")



@app.route("/api/v1.0/percipitation")
def percipitation():
     # Create our session (link) from Python to the DB
    session = Session(engine)
    previous_year = dt.date(2017, 8, 23) - dt.timedelta(365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > previous_year).all()
    session.close()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

   
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the database to calculate TMIN, TAVG, and TMAX for the specified date range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    # Convert the results to a list of dictionaries
    temp_data = []
    for min_temp, avg_temp, max_temp in results:
        temp_data.append({
            "Minimum Temperature": min_temp,
            "Average Temperature": avg_temp,
            "Maximum Temperature": max_temp
        })

    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
#@app.route("/api/v1.0/<start>")
def first(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    dt.datetime.strptime()
    

   
    # Query all stations

    results =  session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)) \
                                    .filter() \
                                    .all()


    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

if __name__ == "__main__":
    app.run(debug=True)