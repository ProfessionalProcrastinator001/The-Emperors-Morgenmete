import unittest
from the_emperors_morgenmete import Egg, Paratha, Tea, MenuItem, Order

class TestMenuItem(unittest.TestCase):

    def test_egg_base_price(self):
        egg = Egg()
        self.assertEqual(egg.base_price, 50)

    def test_add_additive(self):
        tea = Tea()
        sugar = MenuItem.Additive("Sugar", 15)
        tea.add_additive(sugar)
        self.assertEqual(len(tea.additives), 1)
        self.assertEqual(tea.total_price(), 75)

    def test_additive_list(self):
        paratha = Paratha()
        butter = MenuItem.Additive("Butter", 20)
        paratha.add_additive(butter)
        self.assertIn("Butter", paratha.additive_list())

class TestOrder(unittest.TestCase):

    def test_order_add_item(self):
        order = Order()
        egg = Egg()
        order.add_item(egg)
        self.assertEqual(len(order.items), 1)

    def test_total_price_without_discount(self):
        order = Order()
        tea = Tea()
        order.add_item(tea)
        self.assertEqual(order.total_price(), 60)

    def test_total_price_with_discount(self):
        order = Order()
        for _ in range(10):
            order.add_item(Paratha())  # 80 * 10 = 800
        discounted = order.total_price()
        self.assertAlmostEqual(discounted, 800 - 800 * 0.10)

