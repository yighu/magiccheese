from item import Item
from magic_cheese_shop import MagicCheeseShop

from unittest import TestCase, skip

magic_cheese_shop = MagicCheeseShop()

class MagicCheeseShopTest(TestCase):
    def setUp(self):
        self.items = []

    def test_regular_items_decrease_by_one(self):
        self.items.append(Item("Dexterity Vest", 10, 20))
        items = magic_cheese_shop.execute(self.items)
        expected = {'days_until_expiration': 9, 'quality': 19}
        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.days_until_expiration, expected['days_until_expiration'])

    @skip
    def test_quality_goes_up_for_improving_products(self):
        self.items.append(Item("Aged Brie", 20, 30))
        self.items.append(Item("Backstage Passes (Wardruna)", 20, 30))
        items = magic_cheese_shop.execute(self.items)
        expected = [
              {'days_until_expiration': 19, 'quality': 31},
              {'days_until_expiration': 19, 'quality': 31},
            ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_quality_goes_up_by_two_for_improving_products_with_10_days_or_less_left(self):
        self.items.append(Item("Fresh Mozzarella", 10, 34))
        self.items.append(Item("Backstage Passes (Garmarna)", 8, 30))
        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': 9, 'quality': 36},
            {'days_until_expiration': 7, 'quality': 32},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_quality_goes_up_by_three_for_improving_products_with_5_days_or_less_left(self):
        self.items.append(Item("Smoked Gouda", 4, 11))
        self.items.append(Item("Backstage Passes (Otava Yo)", 5, 15))
        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': 3, 'quality': 14},
            {'days_until_expiration': 4, 'quality': 18},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_sulfuras_the_immutable(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", 0, 50))
        items = magic_cheese_shop.execute(self.items)
        expected = {'days_until_expiration': 0, 'quality': 50}
        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.days_until_expiration, expected['days_until_expiration'])

    @skip
    def test_backstage_passes_and_brie_go_to_quality_zero_after_expiration(self):
        self.items.append(Item("Aged Brie", 0, 20))
        self.items.append(Item("Backstage Passes (Grai)", 0, 20))
        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': -1, 'quality': 0},
            {'days_until_expiration': -1, 'quality': 0},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_quality_does_not_increase_past_50(self):
        self.items.append(Item("Aged Brie", 4, 49))
        items = magic_cheese_shop.execute(self.items)
        expected = {'days_until_expiration': 3, 'quality': 50}
        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.days_until_expiration, expected['days_until_expiration'])

    @skip
    def test_quality_decrease_twice_as_fast_after_expiration_for_regular_items(self):
        self.items.append(Item("Dexterity Vest", 0, 20))
        self.items.append(Item("Kamehameha Wave Gauntlets", 0, 6))
        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': -1, 'quality': 18},
            {'days_until_expiration': -1, 'quality': 4},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_conjured_items_decrease_in_quality_twice_as_fast(self):
        self.items.append(Item("Conjured Mana Cake", 3, 6))

        items = magic_cheese_shop.execute(self.items)
        expected = {'days_until_expiration': 2, 'quality': 4}

        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.days_until_expiration, expected['days_until_expiration'])

    @skip
    def test_conjured_items_go_to_zero_in_quality_when_expired(self):
        self.items.append(Item("Conjured Mana Cake", 0, 6))

        items = magic_cheese_shop.execute(self.items)
        expected = {'days_until_expiration': -1, 'quality': 0}

        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.days_until_expiration, expected['days_until_expiration'])

    @skip
    def test_conjured_improving_items_increase_in_quality_twice_as_fast(self):
        self.items.append(Item("Conjured Aged Brie", 20, 8))
        self.items.append(Item("Conjured Backstage Passes (Kino)", 15, 12))

        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': 19, 'quality': 10},
            {'days_until_expiration': 14, 'quality': 14},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_conjured_improving_items_increase_in_quality_4x_as_fast_when_10_days_or_less(self):
        self.items.append(Item("Conjured Smoked Gouda", 6, 8))
        self.items.append(Item("Conjured Backstage Passes (Kino)", 10, 12))

        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': 5, 'quality': 12},
            {'days_until_expiration': 9, 'quality': 16},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])

    @skip
    def test_conjured_improving_items_increase_in_quality_6x_as_fast_when_5_days_or_less(self):
        self.items.append(Item("Conjured Fresh Mozzarella", 5, 9))
        self.items.append(Item("Conjured Backstage Passes (Kino)", 1, 40))

        items = magic_cheese_shop.execute(self.items)
        expected = [
            {'days_until_expiration': 4, 'quality': 15},
            {'days_until_expiration': 0, 'quality': 46},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.days_until_expiration, expectation['days_until_expiration'])
