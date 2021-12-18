from .Tool import tool


def init_view(app):
    app.register_blueprint(tool)
