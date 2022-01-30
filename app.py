import os
from App import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app()

# 集成数据库Migrate管控
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(
        host='localhost',
        port= 9528,
        debug=True
    )
