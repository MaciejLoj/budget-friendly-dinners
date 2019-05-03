from django.test import RequestFactory

from .. import views


class TestRecipesView:
    def test_recipes(self):
        req = RequestFactory().get('/przepisy')
        resp = views.NewRecipes.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_five_zlotys(self):
        req = RequestFactory().get('/do-5-zl')
        resp = views.FiveZlotysRecipesView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_ten_zlotys(self):
        req = RequestFactory().get('/do-10-zl')
        resp = views.TenZlotysRecipesView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_fifteen_zlotys(self):
        req = RequestFactory().get('/do-15-zl')
        resp = views.FifteenZlotysRecipesView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_recipes(self):
        req = RequestFactory().get('/wege')
        resp = views.VeganRecipesView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_five(self):
        req = RequestFactory().get('/wege/do-5-zl')
        resp = views.VeganFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_ten(self):
        req = RequestFactory().get('/wege/do-10-zl')
        resp = views.VeganTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_fifteen(self):
        req = RequestFactory().get('/wege/do-5-zl')
        resp = views.VeganFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_recipes(self):
        req = RequestFactory().get('/z-miesem')
        resp = views.MeatRecipesView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_five(self):
        req = RequestFactory().get('/z-miesem')
        resp = views.MeatFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_ten(self):
        req = RequestFactory().get('/z-miesem')
        resp = views.MeatTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_fifteen(self):
        req = RequestFactory().get('/z-miesem')
        resp = views.MeatFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_appetizers(self):