"""Homework dictionary utilities (dictionaries & sets).

This module provides small helper functions used in the homework
for practicing dictionary mutations.
"""

def add_inventory(inventory, widget, amount):
	"""
	Add `amount` of `widget` to the `inventory` dictionary in-place.

	- `inventory` is a dict mapping widget names to integer counts.
	- If `widget` already exists, increase its count by `amount`.
	- If `widget` does not exist and `amount` > 0, create the key.
	- Does not return a value (per assignment: non-value-return function).
	"""
	if not isinstance(inventory, dict):
		raise TypeError("inventory must be a dict")
	# allow negative amounts so callers can decrease quantity by passing
	# a negative value (tests expect adding -10 to reduce quantity)
	inventory[widget] = inventory.get(widget, 0) + amount



def remove_inventory_widget(inventory, widget, amount):
	"""
	Remove `amount` of `widget` from `inventory`.

	Returns True if the removal succeeded (the widget existed and a
	positive amount was removed), False otherwise.

	Behavior:
	- If `widget` not in `inventory`, return False.
	- If `amount` <= 0, return False.
	- If `amount` >= current count, remove the key entirely and return True.
	- Otherwise subtract `amount` and return True.
	"""
	if not isinstance(inventory, dict):
		raise TypeError("inventory must be a dict")
	if amount <= 0:
		return False
	current = inventory.get(widget)
	if current is None:
		return False
	if amount >= current:
		del inventory[widget]
		return True
	inventory[widget] = current - amount
	return True
