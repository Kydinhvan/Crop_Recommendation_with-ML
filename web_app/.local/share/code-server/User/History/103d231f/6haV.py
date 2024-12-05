from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class AgriOutput(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String, nullable=False)
    maximumTemperature = db.Column(db.Float, nullable=False)
    minimumTemperature = db.Column(db.Float, nullable=False)
    averageTemperature = db.Column(db.Float, nullable=False)
    humidityRelative = db.Column(db.Float, nullable=False)
    averageRainfall = db.Column(db.Float, nullable=False)
    sunshineDuration = db.Column(db.Float, nullable=False)
    maximumWindspeed = db.Column(db.Float, nullable=False)
    averageWindspeed = db.Column(db.Float, nullable=False)
    predictedOutput = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self): 
        return "New agricultural output level created." 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        provOptions = {"1": "North Sumatra", "2": "Central Kalimantan", "3": "Aceh", "4": "Banten", "5": "Papua"}
        provName = provOptions[request.form['prov']]
        provNumber = int(request.form['prov'])
        maxTemp = float(request.form['maxTemp'])
        minTemp = float(request.form['minTemp'])
        avgTemp = float(request.form['avgTemp'])
        humRel = float(request.form['humRel'])
        avgRain = float(request.form['avgRain'])
        sunDur = float(request.form['sunDur'])
        maxWind = float(request.form['maxWind'])
        avgWind = float(request.form['avgWind'])
        pred = predictOutput(provNumber, maxTemp, minTemp, avgTemp, humRel, avgRain, sunDur, maxWind, avgWind)
        new_task = AgriOutput(province=provName, maximumTemperature=maxTemp, minimumTemperature=minTemp, averageTemperature=avgTemp,
                              humidityRelative=humRel, averageRainfall=avgRain, sunshineDuration=sunDur, 
                              maximumWindspeed=maxWind, averageWindspeed=avgWind, predictedOutput=pred
                              )
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    else:        
        agriOutput = AgriOutput.query.order_by(AgriOutput.id).all()
        return render_template('index.html', AgriOutputs=agriOutput)

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

def predictOutput(provNumber, maxTemp, minTemp, avgTemp, humRel, avgRain, sunDur, maxWind, avgWind):
    # Feature ranges for normalization
    maxTemp_min, maxTemp_max = 30, 40
    minTemp_min, minTemp_max = 20, 30
    avgTemp_min, avgTemp_max = 25, 35
    humRel_min, humRel_max = 77, 85
    avgRain_min, avgRain_max = 3, 7
    sunDur_min, sunDur_max = 0.5, 0.65
    maxWind_min, maxWind_max = 3.8, 5.2
    avgWind_min, avgWind_max = 1.93, 2

    # Normalize inputs
    maxTemp = normalize(maxTemp, maxTemp_min, maxTemp_max)
    minTemp = normalize(minTemp, minTemp_min, minTemp_max)
    avgTemp = normalize(avgTemp, avgTemp_min, avgTemp_max)
    humRel = normalize(humRel, humRel_min, humRel_max)
    avgRain = normalize(avgRain, avgRain_min, avgRain_max)
    sunDur = normalize(sunDur, sunDur_min, sunDur_max)
    maxWind = normalize(maxWind, maxWind_min, maxWind_max)
    avgWind = normalize(avgWind, avgWind_min, avgWind_max)
    
    output = 0
    if provNumber == 1:  # North Sumatra
        output = 50.41 - 0.29 * humRel * humRel - 0.40 * (maxTemp - minTemp) - 2.17 * math.log(avgWind) + 0.86 * maxWind
    elif provNumber == 2:  # Central Kalimantan
        output = 31.95 - 0.6 * avgTemp - 1.71 * avgWind + 0.04 * avgRain * avgRain * avgRain - 1.51 * sunDur
    elif provNumber == 3:  # Aceh
        output = 48.83 + 0.43 * avgTemp - 0.68 * (maxTemp - minTemp) - 0.44 * humRel - 2.01 * avgRain - 1.04 * sunDur * sunDur - 0.22 * maxWind - 0.07 * avgWind
    elif provNumber == 4:  # Banten
        output = 53.71 + 1.18 * humRel * humRel + 1.86 * avgTemp * avgTemp - 0.82 * maxWind
    elif provNumber == 5:  # Papua
        output = 42.81 + 1.71 * humRel * humRel + 1.16 * avgTemp * avgTemp * avgTemp - 0.8 * avgTemp * avgTemp - 0.35 * (maxTemp - minTemp) - 1.09 * maxWind + 0.95 * avgRain * avgRain - 2.01 * sunDur 
    
    return round(output, 2)

if __name__ == "__main__":
    app.run(debug=True)