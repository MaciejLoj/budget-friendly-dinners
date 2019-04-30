import pytest
from mixer.backend.django import mixer


class TestRecipe:
    def test_model(self):
        obj = mixer.blend('recipes.Recipe')
        assert obj.pk == 1, 'Should create a Recipe instance'

    def test_snippet(self):
        obj = mixer.blend('recipes.Recipe', body='Chicken pie with lemon')
        result = obj.snippet()
        assert result == 'Chicken pie with lemon...', 'Should return first 30 character and ...'

    def test_str(self):
        obj = mixer.blend('recipes.Recipe', title='Pierogi')
        assert str(obj) == 'Pierogi'
