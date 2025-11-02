from flask import Flask, render_template, request
from datetime import datetime, timedelta
import func

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    """får formelärdatan, säkerhetsteller datum och tar fram elpriser"""
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    price_class = request.form.get("price_class")

    # säkerhetsställer datum
    try:
        chosen_date = datetime(int(year), int(month), int(day))
    except ValueError:
        return render_template("result.html", error="Felaktigt datumformat!")

    today = datetime.now()
    max_future = today + timedelta(days=1)
    min_date = datetime(2022, 11, 1)

    if chosen_date > max_future:
        return render_template("result.html", error="Datumet får vara högst 1 dag framåt i tiden!")
    elif chosen_date < min_date:
        return render_template("result.html", error="Datumet får inte vara före 2022-11-01!")

    # hämatar från apin data
    data = func.get_prices(year, month, day, price_class)
    if isinstance(data, str):
        return render_template("result.html", error=data)

    return render_template("result.html", prices=data, date=chosen_date.strftime("%Y-%m-%d"))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Sidan hittades inte</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)
