import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):

	def test_add_inventory(self):
		inv = {}
		add_inventory(inv, 'Widget1', 10)
		self.assertIn('Widget1', inv)
		self.assertEqual(inv['Widget1'], 10)

		add_inventory(inv, 'Widget1', 25)
		self.assertEqual(inv['Widget1'], 35)

		add_inventory(inv, 'Widget1', -10)
		self.assertEqual(inv['Widget1'], 25)


	def test_remove_inventory_widget(self):
		inv = {}
		add_inventory(inv, 'widget1', 5)
		add_inventory(inv, 'widget2', 7)

		# remove widget1 entirely
		removed = remove_inventory_widget(inv, 'widget1', 5)
		self.assertTrue(removed)
		self.assertEqual(len(inv), 1)
		self.assertIn('widget2', inv)


if __name__ == '__main__':
	unittest.main()
 