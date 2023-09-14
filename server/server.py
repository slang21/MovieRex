from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__) #creates the Flask app
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET']) #code to run the app
def return_home():
    return jsonify({
        'message': "Hello World!",
        'people': ["Olivia","Spencer","Ellen"]
    })

if __name__ == "__main__":  #routing for the app
    app.run(debug=True, port=8080) #remove in Production