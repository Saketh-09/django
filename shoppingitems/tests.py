from django.urls import reverse
from django.test import TestCase, Client
from shoppingitems.models import ShopingItem
# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = ShopingItem.objects.create(
            name='cup', price='100', discount='5')

    def test_create_get(self):
        response = self.client.get(reverse('create_view'))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'signup.html')

    def test_detail_get(self):
        response = self.client.get(reverse('detail_view',  args=[3]))
        self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'template/detail_view.html')

    def test_update_get(self):
        response = self.client.get(reverse('update_view', args=[3]))
        self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'template/update_view.html')

    def test_delete_get(self):
        response = self.client.get(reverse('delete_view', args=[3]))
        self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'template/delete_view.html')

    def test_create_post(self):
        response = self.client.post(reverse('create_view'), {
                                    'name': 'cup', 'price': '100', 'discount': '5'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.item.name, 'cup')

    def test_update_post(self):
        response = self.client.post(reverse('update_view', args=[1]), {
                                    'name': 'cup', 'price': '50', 'discount': '5'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.item.price, '50')

    def test_delete_post(self):
        response = self.client.post(reverse('delete_view', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ShopingItem.objects.all().count(), 0)
