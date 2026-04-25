import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_entrance():
    return render_template('index.html'), 200

@app.route('/backend', methods=['POST'])
def backend():
    my_input = json.loads(request.data)
    
    if isinstance(my_input["num1"],int) and isinstance(my_input["num2"],int):
        return json.dumps({
            "sum": my_input["num1"] + my_input["num2"]
        })
    else:
        return json.dumps({
            "error": "input isnt an integer"
        })

if __name__ == "__main__":
    app.run(debug=True)