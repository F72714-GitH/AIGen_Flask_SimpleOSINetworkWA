from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

PACKETS = {
    "HTTP": [
        {"device": "PC", "layers": [7, 6, 5, 4]},
        {"device": "Switch", "layers": [2, 1]},
        {"device": "Router", "layers": [3, 2, 1]},
        {"device": "Server", "layers": [7, 6, 5, 4]}
    ],
    "ICMP": [
        {"device": "PC", "layers": [3]},
        {"device": "Router", "layers": [3]},
        {"device": "Server", "layers": [3]}
    ],
    "ARP": [
        {"device": "PC", "layers": [2]},
        {"device": "Switch", "layers": [2]},
        {"device": "PC", "layers": [2]}
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/path")
def path():
    packet_type = request.args.get("type", "HTTP")
    return jsonify(PACKETS.get(packet_type, []))

if __name__ == "__main__":
    app.run(debug=True)
