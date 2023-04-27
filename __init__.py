from flask import Flask, render_template
import os, json

MASTER = os.path.join("articles", "timeline.json")

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
    timeline_data = {}
    with open(MASTER, "r") as f:
        timeline_data = json.loads(f.read())

    return render_template("content.j2", timeline=timeline_data)

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)