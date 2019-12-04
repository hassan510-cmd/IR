from flask import Flask,render_template
from datetime import datetime, timedelta
import pygal
from math import cos

app = Flask(__name__)
@app.route('/')
@app.route('/Line')
def Line():
    try:
        # Line:
        line_chart = pygal.Line()
        # line_chart = pygal.HorizontalLine()
        # line_chart = pygal.StackedLine(fill=False)
        # Bar:
        # line_chart = pygal.Bar()
        # line_chart = pygal.StackedBar()
        # line_chart = pygal.HorizontalStackedBar()
        # line_chart = pygal.HorizontalBar()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2013))
        line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('حسونة',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        graph_data = line_chart.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))

@app.route('/Time')
def Time():
    try:
        date_chart = pygal.Line(x_label_rotation=20)
        date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
            datetime(2013, 1, 2),datetime(2013, 1, 12),
            datetime(2013, 2, 2),datetime(2013, 2, 22)])
        date_chart.add("Visits", [300, 412, 823, 672])
        graph_data = date_chart.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))


@app.route('/Histogram')
def Histogram():
    try:
        hist = pygal.Histogram()
        hist.add('Wide bars', [(5, 0, 10), (4, 5, 13), (2, 0, 15)])
        hist.add('Narrow bars',  [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)])
        graph_data = hist.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))
@app.route('/XY')
def XY():
    try:
        xy_chart = pygal.XY()
        # xy_chart = pygal.XY(stroke=True)
        xy_chart.title = 'XY Cosinus'
        xy_chart.add('x = cos(y)', [(cos(x / 10.0), x / 10.0) for x in range(-50, 50, 5)])
        xy_chart.add('y = cos(x)', [(x / 10.0, cos(x / 10.0)) for x in range(-50, 50, 5)])
        xy_chart.add('x = 1',  [(1, -5), (1, 5)])
        xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
        xy_chart.add('y = 1',  [(-5, 1), (5, 1)])
        xy_chart.add('y = -1', [(-5, -1), (5, -1)])
        xy_chart.add('xy', [(-2, -1), (-1, 0),(0,2),(1,3),(2,5),(3,0)])
        # xy_chart.add('xy', [(-2, -1), (-1, 0),(0,2),(1,3),(2,5),(3,0)],stroke=False)
        graph_data = xy_chart.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))

@app.route('/Pie')
def Pie():
    try:
        pie_chart = pygal.Pie()
        pie_chart.title = 'Browser usage in February 2012 (in %)'
        pie_chart.add('IE', 19.5)
        pie_chart.add('Firefox', 36.6)
        pie_chart.add('Chrome', 36.3)
        pie_chart.add('Safari', 4.5)
        pie_chart.add('Opera', 2.3)

        # # Multi-series pie :Same pie but divided in sub category
        # pie_chart.add('IE', [5.7, 10.2, 2.6, 1])
        # pie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
        # pie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
        # pie_chart.add('Safari', [4.4, .1])
        # pie_chart.add('Opera', [.1, 1.6, .1, .5])

        # # Donut
        # pie_chart = pygal.Pie(inner_radius=.4)
        
        # # Ring
        # pie_chart = pygal.Pie(inner_radius=.75)
        
        # # Half Pie
        # pie_chart = pygal.Pie(half_pie=True)
        # pie_chart.add('IE', 19.5)
        # pie_chart.add('Firefox', 36.6)
        # pie_chart.add('Chrome', 36.3)
        # pie_chart.add('Safari', 4.5)
        # pie_chart.add('Opera', 2.3)
        
        graph_data = pie_chart.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))



@app.route('/Gauge')
def Gauge():
    try:
        gauge_chart = pygal.Gauge()
        gauge_chart.title = 'DeltaBlue V8 benchmark results'
        gauge_chart.range = [0, 10000]
        gauge_chart.add('Chrome', 8212)
        gauge_chart.add('Firefox', 8099)
        gauge_chart.add('Opera', 2933)
        gauge_chart.add('IE', 41)
        graph_data = gauge_chart.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))

@app.route('/SolidGauge')
def SolidGauge():
    try:
        gauge = pygal.SolidGauge(inner_radius=0.70)
        # gauge = pygal.SolidGauge(inner_radius=0.70,half_pie=True)
        percent_formatter = lambda x: '{:.10g}%'.format(x)
        dollar_formatter = lambda x: '{:.10g}$'.format(x)
        gauge.value_formatter = percent_formatter

        gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}],
                formatter=dollar_formatter)
        gauge.add('Series 2', [{'value': 70, 'max_value': 100}])
        gauge.add('Series 3', [{'value': 3}])
        gauge.add('Series 4', [
                    {'value': 51, 'max_value': 100},
                    {'value': 12, 'max_value': 100}])
        gauge.add('Series 5', 95)
        
        graph_data = gauge.render_data_uri()
        return render_template("graphing.html", graph_data = graph_data)
    except Exception as e:
        return(str(e))
if __name__ == '__main__':
	app.run(debug = True)