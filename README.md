# sqlalchemy-challenge

# Climate Analysis and Flask API

- [Overview](#overview)
- [Part 1: Climate Data Analysis](#part-1-climate-data-analysis)
- [Part 2: Flask API](#part-2-flask-api)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Overview

This project involves performing a climate analysis on the Honolulu, Hawaii region using Python and SQLAlchemy. The analysis is followed by the development of a Flask API to expose the results via various endpoints.

The project is divided into two main parts:
1. **Climate Data Analysis**: Using SQLAlchemy ORM, Pandas, and Matplotlib.
2. **Flask API**: To make the results of the analysis accessible via web routes.

---

## Part 1: Climate Data Analysis

### 1. Precipitation Analysis

<img width="785" alt="Screenshot 2024-09-06 at 3 53 16 PM" src="https://github.com/user-attachments/assets/81247202-e286-4b00-9b65-e624acfccfd1">


In this analysis, the last 12 months of precipitation data were retrieved and analyzed. The steps included:
- **Query**: The most recent date in the dataset, 2017-8-23, was identified, and the precipitation data for the previous 12 months was retrieved.
- **Results**: The data was organized and plotted to show precipitation levels over time.
- **Visualization**: The plot highlights variations in rainfall, with noticeable peaks indicating heavy rainfall on certain days noticeably in August and lighter precipitation on others.

### 2. Station Analysis

<img width="793" alt="Screenshot 2024-09-06 at 5 56 44 PM" src="https://github.com/user-attachments/assets/b1f3dd99-5e46-4935-a5d8-e2859b06bd56">


This analysis focused on identifying the most active station and analyzing its temperature observations.
- **Query**: The most active station (i.e., the one with the most observations) was identified from the dataset.
- **Temperature Analysis**: The temperature observations for the most active station over the last 12 months were retrieved.
- **Visualization**: A histogram was plotted to show the distribution of temperatures, which revealed that most temperatures ranged between 70°F and 75°F, typical of the warm climate in Hawaii.

---

## Part 2: Flask API

A Flask API was developed to expose the climate analysis results. The following routes are available:

### Available Routes:

1. **Home Route** (`/`)
   - Displays all the available API routes.

<img width="968" alt="Screenshot_weather_api_home" src="https://github.com/user-attachments/assets/8cd8f63a-2336-4b7e-bfb8-6af0b93c609a">

2. **Precipitation Route** (`/api/v1.0/precipitation`)
   - Retrieves the last 12 months of precipitation data, 2016-2017.
   - Returns a JSON dictionary where the keys are dates and the values are precipitation amounts.
  
<img width="968" alt="Screenshot_weather_api_precipitation" src="https://github.com/user-attachments/assets/3d85d8f6-d8bf-4ed4-adaa-f6f925cd287a">

3. **Stations Route** (`/api/v1.0/stations`)
   - Retrieves a list of all weather stations in the dataset.
   - Returns a JSON list with station details including station ID, station code, and station name.
  
<img width="884" alt="Screenshot_weather_api_stations" src="https://github.com/user-attachments/assets/a4bc5cd8-bf5f-4033-9fee-e389b413fab9">


4. **Temperature Observations Route** (`/api/v1.0/tobs`)
   - Retrieves temperature observations from the most active station for the last 12 months, 2016-2017.
   - Returns a JSON list of temperature observations.
  
<img width="968" alt="Screenshot_weather_api_tobs" src="https://github.com/user-attachments/assets/d5db6a48-0c30-4121-bcce-c9b8e92150f0">


5. **Start Date Route** (`/api/v1.0/<start>`)
   - Start date should be specified in YYYY-MM-DD format immediately following the '/' (e.g. /api/v1.0/2013-01-19)
   - Retrieves the minimum, average, and maximum temperatures for all dates greater than or equal to the specified start date.
   - Returns a JSON list with temperature statistics.

<img width="884" alt="Screenshot_weather_api_start" src="https://github.com/user-attachments/assets/c033bda5-cac7-440c-93d0-5fed1568a62d">


6. **Start-End Date Route** (`/api/v1.0/<start>/<end>`)
   - Start and end date should be specified in YYYY-MM-DD format immediately following the '/' (e.g. /api/v1.0/2013-01-19/2016-03-20)
   - Retrieves the minimum, average, and maximum temperatures for the specified date range.
   - Returns a JSON list with temperature statistics for the date range.

<img width="884" alt="Screenshot_weather_api_start_end" src="https://github.com/user-attachments/assets/a58d0eab-6827-4d7c-bc7c-03e956f42a50">

---

# Contact
Rinal Shastri - rinal.shastri@outlook.com, rinaljoginshastri@gmail.com

# Acknowledgements

**Tutor - Justin Moore**

**Xpert Learning Assistant in Bootcamp spot**

**ChatGPT**
