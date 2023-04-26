from flask import Flask, render_template
import os, json

DATA_FILE = ""

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='')
    # Configure app key & DB location
    app.config.from_mapping(
        SECRET_KEY = os.urandom(32),
    )

    # Ensure the DB location exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

@app.route("/", methods=['GET', 'POST'])
def resume():
    data = {}
   #  with open(DATA_FILE, "r") as f:
   #      data = json.loads(f.read())
   
    return render_template("content.j2")

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)