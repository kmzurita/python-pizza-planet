

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
from app.seeder.seeder_script import seed_database


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


@manager.command('seed_db')
def seed_db():
    seed_database()
    print('Database seeded successfully')

if __name__ == '__main__':
    manager()
