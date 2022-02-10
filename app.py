from flask import Flask, url_for, request, jsonify, render_template
from handlers.powerplant_handlers import handle_powerplant_post
from helpers.powerplant_json_encoder import PowerPlantJSONEncoder
from flask_socketio import SocketIO
import json

app = Flask(__name__)

# Set custom decoder
app.json_encoder = PowerPlantJSONEncoder
app.logger.info("Starting application...")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.logger.info("Running SocketIO...")
socketio.run(app)


def emit_powerplant_post(data):
    socketio.emit('powerplant-post', data, broadcast=True)


@app.route("/socket")
def socket():
    return render_template("ws_test.html")


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the API!"


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error("app encountered an error: {}".format(e))
    return jsonify({"error_message": str(e)})


@app.route("/", methods=["POST"])
def power_plant():
    app.logger.info("Received POST request on /")
    received, calculated = handle_powerplant_post(request)
    emit_powerplant_post({"received": received, "calculated": json.dumps(
        calculated, cls=PowerPlantJSONEncoder)})
    return jsonify(calculated)
