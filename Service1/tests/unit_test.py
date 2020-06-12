import unittest
from unittest import mock

from flask import render_template, redirect, url_for, request
from flask_testing import TestCase

from application import app, db
from application.models import Stories
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

        story = Stories(
            author='Tom Petty', 
            title='Startled',
            story='A sudden loud noise startled the walker who fell and hit her head on a rock.',
            keywords='Forest, Gunshot, Dark theme'
        )

        db.session.add(story)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_stories_view(self):
        response = self.client.get(url_for('stories'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):

    def test_add_story(self):
        retsponse = self.client.post(
            url_for('home'),
            data=dict(
                author="Jane Doe",
                title="Test title",
                story="Generic test story",
                keywords="Beach, screeming, Happy theme"
                ),
            follow_redirects=True
        )
        self.assertIn(b'Created meal', response.data)

    def test_delete_story(self):
        original = Stories.query.count()
        self.client.post(
            '/delete_story/1',
            follow_redirects=True
        )
        assert original != Stories.query.count()

class TestModels(TestBase):

    def test_stories_repr_model(self):
        story = Stories.query.all()
        assert repr(story) == '[Id: 1 Story: A sudden loud noise startled the walker who fell and hit her head on a rock.]'