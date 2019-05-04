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
        req = RequestFactory().get('/wege/przekaski')
        resp = views.VeganAppetizersView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_appetizers_five(self):
        req = RequestFactory().get('/wege/przekaski/do-5-zl')
        resp = views.VeganAppetizersFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_appetizers_ten(self):
        req = RequestFactory().get('/wege/przekaski/do-10-zl')
        resp = views.VeganAppetizersTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_appetizers_fifteen(self):
        req = RequestFactory().get('/wege/przekaski/do-15-zl')
        resp = views.VeganAppetizersFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_appetizers(self):
        req = RequestFactory().get('/z-miesem/przekaski')
        resp = views.MeatAppetizersView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_appetizers_five(self):
        req = RequestFactory().get('/z-miesem/przekaski/do-5-zl')
        resp = views.MeatAppetizersFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_appetizers_ten(self):
        req = RequestFactory().get('/z-miesem/przekaski/do-10-zl')
        resp = views.MeatAppetizersTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_appetizers_fifteen(self):
        req = RequestFactory().get('/z-miesem/przekąski/do-15-zl')
        resp = views.MeatAppetizersFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_dinners(self):
        req = RequestFactory().get('/wege/obiady')
        resp = views.VeganDinnersView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_dinners_five(self):
        req = RequestFactory().get('/wege/obiady/do-5-zl')
        resp = views.VeganDinnersFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_dinners_ten(self):
        req = RequestFactory().get('/wege/obiady/do-10-zl')
        resp = views.VeganDinnersTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_dinners_fifteen(self):
        req = RequestFactory().get('/wege/obiady/do-15-zl')
        resp = views.VeganDinnersFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_dinners(self):
        req = RequestFactory().get('/z-miesem/obiady')
        resp = views.MeatDinnersView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_dinners_five(self):
        req = RequestFactory().get('/z-miesem/obiady/do-5-zl')
        resp = views.MeatDinnersFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_dinners_ten(self):
        req = RequestFactory().get('/z-miesem/obiady/do-10-zl')
        resp = views.MeatDinnersTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_dinners_fifteen(self):
        req = RequestFactory().get('/z-miesem/obiady/do-15-zl')
        resp = views.MeatDinnersFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_desserts(self):
        req = RequestFactory().get('/wege/desery')
        resp = views.VeganDessertsView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_desserts_five(self):
        req = RequestFactory().get('/wege/desery/do-5-zl')
        resp = views.VeganDessertsFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_desserts_ten(self):
        req = RequestFactory().get('/wege/desery/do-10-zl')
        resp = views.VeganDessertsTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_vegan_desserts_fifteen(self):
        req = RequestFactory().get('/wege/desery/do-15-zl')
        resp = views.VeganDessertsFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_desserts(self):
        req = RequestFactory().get('/z-miesem/desery')
        resp = views.MeatDessertsView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_desserts_five(self):
        req = RequestFactory().get('/z-miesem/desery/do-5-zl')
        resp = views.MeatDessertsFiveView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_desserts_ten(self):
        req = RequestFactory().get('/z-miesem/desery/do-10-zl')
        resp = views.MeatDessertsTenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_meat_desserts_fifteen(self):
        req = RequestFactory().get('/z-miesem/desery/do-15-zl')
        resp = views.MeatDessertsFifteenView.as_view()(req)
        assert resp.status_code == 200, "Should be callable by anyone"
