from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Prueba de google app engine!"

if __name__ == "__main__":
    app.run()
# run with gunicorn -w 1 server:app