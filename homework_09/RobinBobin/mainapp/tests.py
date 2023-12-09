import django.test
from .models import Profile, Product, ProfilesProducts


# Create your tests here.
class ProfilesProductsTest(django.test.TestCase):
    def setUp(self):
        profiles = [
            {'name': 'User1', 'username': 'user1', 'weight_initial': 100, 'weight_goal': 80, 'daily_ccal': 1800},
            {'name': 'User2', 'username': 'user2', 'weight_initial': 200, 'weight_goal': 100, 'daily_ccal': 1500},
        ]
        products = [
            {'name': 'product1', 'ccal': 111},
            {'name': 'product2', 'ccal': 222},
        ]
        for profile in profiles:
            # self.client.post()
            Profile.objects.create(
                name=profile['name'],
                username=profile['username'],
                weight_initial=profile['weight_initial'],
                weight_goal=profile['weight_goal'],
                daily_ccal=profile['daily_ccal'],
            )
        for product in products:
            # self.client.post()
            Product.objects.create(
                name=product['name'],
                ccal=product['ccal'],
            )
        self.ProfilesProductsTest = [
            {'name': 'eating1', 'profile': 'user1', 'product': 'product1'},
            {'name': 'eating2', 'profile': 'user1', 'product': 'product2'},
            {'name': 'eating3', 'profile': 'user2', 'product': 'product1'},
        ]



    def test_create_profilesproducts(self):
        profilesproducts_cnt = ProfilesProducts.objects.count()
        self.assertEqual(profilesproducts_cnt, 0)
        profile = Profile.objects.get(username='user1')
        product = Product.objects.get(name='product1')
        response = self.client.post(
            path='/profilesproducts/add_profilesproducts/',
            data={
                'eat_date': '2020-01-01',
                'name': 'breakfast1',
                'profile': profile.pk,
                'product': product.pk
            }
        )
        self.assertEquals(302, response.status_code)
        profilesproducts_cnt = ProfilesProducts.objects.count()
        self.assertEqual(profilesproducts_cnt, 1)


class ProductAddTest(django.test.TestCase):
    def test_succ_product_add(self):
        products_cnt = Product.objects.count()
        response = self.client.post(
            path='/products/add/',
            data={
                'name': 'cucumber',
                'ccal': 55
            }
        )
        self.assertEqual(302, response.status_code)
        products_cnt = Product.objects.count()
        self.assertEqual(products_cnt, 1)


class ProfileAddTest(django.test.TestCase):
    def test_succ_profile_add(self):
        profile_cnt = Profile.objects.count()
        response = self.client.post(
            path='/profiles/add_profile/',
            data={
                'name': 'Tester The One',
                'username': 'Tester1',
                'contact': '-',
                'weight_initial': 111,
                'weight_goal': 88,
                'daily_ccal': 1800,
            }
        )
        self.assertEqual(302, response.status_code)
        profiles_cnt = Profile.objects.count()
        self.assertEqual(profiles_cnt, 1)
