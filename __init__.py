from flask import Flask, render_template
import os, json

MASTER = os.path.join("articles", "timeline.json")
ARTICLE_DIR = "articles"

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

    text_data = {}
    for section in timeline_data:
        for event in timeline_data.get(section).get('event_list'):
            print(event)
            text_data[event.get('title')] = {}
            with open(os.path.join(ARTICLE_DIR, event.get('content_file')), "r") as f:
                text_data[event.get('title')]['title'] = event.get('title')
                text_data[event.get('title')]['text'] = f.read()
                text_data[event.get('title')]['anchor'] = event.get('anchor')

    print(text_data)
    return render_template("content.j2", 
                           timeline=timeline_data,
                           content=text_data)

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)