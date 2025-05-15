from django.urls import reverse, resolve
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase



        
class RecipeViwesTest(RecipeTestBase):
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes here!!</h1>', response.content.decode('utf-8'))
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)
        
    def test_recipe_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        
        self.assertIn('<h1>No recipes here!!</h1>', content)
        
    
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        test_category = self.make_category(name='Test Category')
        self.make_recipe(
            category=test_category,
            is_published=False
        )
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': test_category.id})
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        test_category = self.make_category(name='Empty Category')
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': test_category.id})
        )
        self.assertEqual(response.status_code, 404)
        
    
        
    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)
        
         
    def test_recipe_detail_template_loads_the_correct_recipe(self):
            needed_title = 'This is a detail page - It load one recipe'
            recipe = self.make_recipe(
                title=needed_title,
                is_published=True 
            )
            response = self.client.get(
                reverse('recipes:recipe', kwargs={'id': recipe.id})
            )
            content = response.content.decode('utf-8')
            self.assertIn(needed_title, content)
        
 