import unittest

from flask import render_template, redirect, url_for, request
from flask_testing import TestCase

from Service1.application import app, db
from Service1.application.models import Stories
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('STORYTESTINGDBURI'),
                SECRET_KEY=getenv('TESTSECRETKEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        story = Stories('Tom Petty', 'Startled', 'A sudden loud noise startled the walker who fell and hit her head on a rock.')

        db.session.add(story)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('/'))
        self.assertEqual(response.status_code, 200)