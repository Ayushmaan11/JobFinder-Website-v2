from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {
        'id' : 1,
        'title': 'Data Analyst',
        'location' : 'Bengaluru, India',
        'salary' : 'Rs. 12,00,000'
    },
    {
        'id' : 2,
        'title': 'Web-developer',
        'location' : 'Andheri, India',
        'salary' : 'Rs. 2,00,000'
    },
    {
        'id' : 3,
        'title': 'Cloud Developer',
        'location' : 'Hyderabad, India',
        'salary' : 'Rs. 25,00,000'
    },
    {
        'id' : 4,
        'title': 'Backend Developer',
        'location' : 'Gujarat, India',
        
    },
    {
        'id' : 4,
        'title': 'Cybersecurity Engineer',
        'location' : 'Varanasi, India',
        
    }
]

@app.route("/")
def hellpw_world():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True, use_reloader=True, reloader_type="stat")