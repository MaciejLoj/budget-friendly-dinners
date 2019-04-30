from django.test import RequestFactory

from .. import views


class TestRecipesView:
    def test_recipes(self):
        req = RequestFactory().get('/przepisy')
        resp = views.NewRecipes.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_five_zlotys(self):
        req = RequestFactory().get('/do-5-zl')
        resp = views.FiveZlotysRecipes.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_ten_zlotys(self):
        req = RequestFactory().get('/do-10-zl')
        resp = views.TenZlotysRecipes.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_fifteen_zlotys(self):
        req = RequestFactory().get('/do-15-zl')
        resp = views.FifteenZlotysRecipes.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

