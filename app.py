from cityW import get_city

from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/scatter")
def rick():

    data = get_city()
    print(data)
    lat= data['lat']
    temp_max= data['temp_max']
    temp_min= data['temp_min']
    Humidity= data['humidity']
    wind_speed= data['wind_speed']
    # @TODO: Build a dictionary of the lyric data that you can use to
    # build a plotly pie chart



    trace1 = { "x": lat,
               "y": temp_max,
               "type": "scatter",
               "mode": 'markers',
               "marker": {"size": 3, "color":temp_min, "colorscale": 'Bluered', "type": 'heatmap', "colorbar":{}, "size":wind_speed, "sizeref": 1}
               }
    data = [trace1]
    print(data)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
