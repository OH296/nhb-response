import os

from flask import Flask, render_template

from .config import Config


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    '''app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )'''

    app.config.from_object(Config)


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    print("basic function")
    @app.route('/intro')
    def intro():
        components = [
            {
                "id": "intro",
                "label": "Introduction",
                "subsections": [
                    {"id": "intro_sub1", "label": "Background"},
                    {"id": "intro_sub2", "label": "Purpose"}
                ]
            },
            {
                "id": "facts",
                "label": "Statement of Facts",
                "subsections": []
            },
            {
                "id": "grounds",
                "label": "Grounds of Defence",
                "subsections": [
                    {
                        "id": "grounds_sub1",
                        "label": "Legal Grounds"
                    },
                    {"id": "grounds_sub2", "label": "Procedural Grounds"}
                ]
            },
            {
                "id": "evidence",
                "label": "Supporting Evidence",
                "subsections": []
            },
            {
                "id": "conclusion",
                "label": "Conclusion",
                "subsections": []
            }
        ]
        return render_template('intro.html', components=components)

    @app.route('/')
    def hello():
        return render_template('intro.html')

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return "404";

    return app
