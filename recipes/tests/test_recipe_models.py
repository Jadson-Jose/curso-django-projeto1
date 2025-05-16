from django.forms import ValidationError
from .test_recipe_base import RecipeTestBase 
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        super().setUp()
        self.recipe = self.make_recipe()
            
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            # Comente a linha abaixo para não executar a validação
            self.recipe.full_clean()
            