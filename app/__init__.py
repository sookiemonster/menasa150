from flask import Flask, render_template
import os, json

JSON_FNAME = "timeline.json"
MASTER = os.path.join("articles", JSON_FNAME)
ARTICLE_DIR = "articles"

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static')
    # Configure app key & DB location
    app.config.from_mapping(
        SECRET_KEY = os.urandom(32),
    )
    return app

app = create_app()

@app.route("/")
def landing():
    return render_template('index.html')

@app.route("/history")
def content():
    timeline_data = {}
    with open(MASTER, "r", encoding='utf-8') as f:
        timeline_data = json.loads(f.read())
    
    text_data = {}
    for section in timeline_data:
        for event in timeline_data.get(section).get('event_list'):
            # print(event)
            text_data[event.get('title')] = {}
            with open(os.path.join(ARTICLE_DIR, event.get('content_file')), "r", encoding='utf-8') as f:
                text_data[event.get('title')]['title'] = event.get('title')
                text_data[event.get('title')]['text'] = f.read()
                text_data[event.get('title')]['anchor'] = event.get('anchor')

    # print(text_data)
    return render_template("content.j2", 
                           timeline=timeline_data,
                           content=text_data)

if __name__ == "__main__":
    app.debug = True
    app.run()