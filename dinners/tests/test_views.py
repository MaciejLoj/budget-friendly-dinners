from django.test import RequestFactory

from .. import views


class TestHomepageView:
    def test_homepage(self):
        req = RequestFactory().get('/')
        resp = views.HomepageView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'


class TestContactView:
    def test_homepage(self):
        req = RequestFactory().get('/kontakt')
        resp = views.ContactView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

