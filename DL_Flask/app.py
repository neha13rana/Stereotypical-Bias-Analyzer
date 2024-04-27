from flask import Flask, request, render_template
from transformers import pipeline
import re

app = Flask(__name__)

# Load the bias identification pipeline
pipe = pipeline("text-classification", model="PriyaPatel/bias_identificaiton45")

# Define labels mapping
labels = {
    0: "race/color",
    1: "socioeconomic",
    2: "gender",
    3: "disability",
    4: "nationality",
    5: "sexual orientation",
    6: "physical appearance",
    7: "religion",
    8: "age",
    9: "profession",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        output = pipe(text)
        label_number = output[0]["label"]
        label_number = re.findall(r'\d+', label_number)[0]
        label_number = int(label_number)
        label_name = labels[int(label_number)]
        return render_template('result.html', text=text, label=label_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
