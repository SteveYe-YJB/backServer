from .Tool import tool
from .sql_test import sql

def init_view(app):
    app.register_blueprint(tool)
    app.register_blueprint(sql)
