from flask import Flask, render_template


jobs = [
    {"id": 1, "title":  "Frontend Engineer", "location": "Accra, Ghana", "salary": "230,000"}, 
    {"id": 2, "title":  "Backend Engineer", "location": "Kumasi, Ghana", "salary": "30,000"},
    {"id": 3, "title":  "Senior Frontend Engineer", "location": "Accra, Ghana", "salary": "530,000"}
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)