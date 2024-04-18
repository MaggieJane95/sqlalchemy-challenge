# sqlalchemy-challenge
## SQLAlchemy Climate Analysis and Flask API

Welcome to the SQLAlchemy Climate Analysis and Flask API project! This project is a part of a larger task aimed at conducting climate analysis and designing a Flask API based on a provided dataset from Honolulu, Hawaii.

## Project Overview

In this project, we've analyzed the climate data of Honolulu using Python, SQLAlchemy, Pandas, and Matplotlib. The analysis includes exploring precipitation and temperature data over a certain period. Additionally, we've designed a Flask API that provides routes to access this data in JSON format.

## Files Included

--> climate_starter.ipynb: This Jupyter notebook contains the climate analysis and exploration code. It includes SQLAlchemy queries, data visualization with Matplotlib, and summary statistics using Pandas.

--> app.py: This Python script defines the Flask API routes. It handles requests and serves the analysis results in JSON format.

# Resources/:

--> hawaii.sqlite: The SQLite database file containing the climate dataset.
Other necessary data files used for the analysis.

## How to Run
# To run this project:

-> Clone the repository to your local machine.

-> Set up a Python environment.

-> Install the required dependencies.

-> Run the Flask API using the app.py script.

-> Access the API routes through your web browser or API testing tools.

## API Routes
/: Homepage listing all available routes.

/api/v1.0/precipitation: Returns precipitation data for the last year in JSON format.

/api/v1.0/stations: Returns a JSON list of weather stations.

/api/v1.0/tobs: Returns temperature observations for the last year from the most active station.

/api/v1.0/<start> and /api/v1.0/<start>/<end>: Returns temperature statistics for specified date ranges.


## Conclusion
Thank you for checking out this project! Feel free to explore the analysis notebooks and experiment with the Flask API routes. If you have any questions or feedback, don't hesitate to reach out.
