Overview
The Rice Production Forecast (Yearly) tool is designed to predict rice output based on climate and environmental data for various provinces. It utilizes user-input data such as temperature, humidity, rainfall, sun duration, and wind speed to calculate rice production for a specified four-month period (January to April).

This application helps researchers, agricultural planners, and policymakers estimate rice yield productivity based on the average first 4 months of the year and the last 3 months of last year climate data.

How to Run the Application:
1. Navigate to the Work Folder

    Open your terminal and change the directory to the work folder: cd work

    Activate Virtual Environment: source env/bin/activate

    Run Flask Application
        Start the Flask development server with the following command: flask run --reload
            The --reload flag ensures that the server automatically updates whenever you make changes to the code.

    Access the Application:
        Open your browser and navigate to the URL provided by Flask (http://127.0.0.1:5000).

Have fun & enjoy!

How to Use:

1. Province Selection
    Use the dropdown menu under "Province" to select the area for which you want to predict rice production (e.g., "North Sumatra").

2. Input Climate Data
    Maximum Recorded Temperature: Enter the maximum temperature recorded during the specified period (January to April).
    Minimum Recorded Temperature: Enter the minimum temperature recorded during the same period.
    Average Temperature: Input the average temperature for the four months.
    Relative Humidity: Provide the average relative humidity (as a percentage) for the time period.
    Average Rainfall: Input the average rainfall (in millimeters) over the period.
    Sun Duration: Enter the average sun duration as a fraction (e.g., 0.5 for 50% of daylight hours).
    Maximum Recorded Wind Speed: Input the maximum recorded wind speed (in km/h or m/s).
    Average Wind Speed: Provide the average wind speed during the same timeframe.
    
    Note: If you do not have a specific data point, enter 0.

3. Calculate Rice Output
    After entering all the required data, click the Calculate Rice Output button.
    The tool will process your inputs and return an estimated rice output for the selected province and time period.

Input Guidelines:

1. Province: Ensure the correct province is selected, as climate data can vary widely between regions.
2. Temperature, Humidity, Rainfall: Use accurate and up-to-date measurements where possible. Use average values for large datasets.
3. Sun Duration: Input this as a fraction of total daylight hours (e.g., 0.8 for 80% of daylight).
4. Wind Speed: Measurements should be consistent (e.g., all in km/h or m/s) for accurate predictions.

Outputs Guidelines:
- The tool calculates a predicted rice productivity in quintals/hectare
- Estimated Total Production: You can manually calculate the total production (quintals) using the formula:
            Total Production = Predicted Productivity × Cultivated Area (in hectares) 

Use Case Example:
Suppose you want to forecast rice production for North Sumatra for the a certain year. Here’s an example input:

    Maximum Temperature: 35°C
    Minimum Temperature: 20°C
    Average Temperature: 27°C
    Relative Humidity: 85%
    Average Rainfall: 2 mm
    Sun Duration: 0.6
    Maximum Wind Speed: 4 m/s
    Average Wind Speed: 2 m/s
After entering this data, click Calculate Rice Output to view the prediction.

Notes and Limitations
- Incomplete Data: If exact data is unavailable, input 0 as a placeholder. However, this may reduce prediction accuracy.
- Precision: The tool’s accuracy depends on the quality of the climate data and the model used for prediction.