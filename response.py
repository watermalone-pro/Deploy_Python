from flask import Flask, render_template, request, jsonify
import json
import random
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
@app.get("/place")
def index_get():
    return render_template("response.html")

CORS(app)
@app.post("/predict")
def get_response(msg):
    msg = request.json
    print(msg)
    
    # with open('ai.json', 'r') as f:
    #     intents = json.load(f)
    # check = msg.split()
    # max = 0
    # for intent in intents['intents']:
    #     count=0
    #     for word in check:
    #         for words in intent['patterns']:
    #             if word in words:
    #                 count = count + 1
    #                 if count > max:
    #                     max = count
    #                     response = intent['responses']
    #                     response = random.choice(response)
    # if count == max:
    #     response = "Sorry, could not generate a response. Please be more specific."
    # return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)

    






            
            
        


