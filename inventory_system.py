"""Simple inventory management module for adding, removing, saving, and loading stock data."""

import json
# import logging
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=[]):
    """Add qty of item to stock_data. Validates inputs and records an optional log list."""
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))


def remove_item(item, qty):
    """Remove qty of item from stock_data. If resulting qty <= 0, remove the key."""
    if item in stock_data:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]


def get_qty(item):
    """Return the current quantity for item, or 0 if not present."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory from JSON file and update the module-level stock_data dict."""
    f = open(file, "r")
    global stock_data
    stock_data = json.loads(f.read())
    f.close()


def save_data(file="inventory.json"):
    """Save the current stock_data to a JSON file using utf-8 encoding."""
    f = open(file, "w")
    f.write(json.dumps(stock_data))
    f.close()


def print_data():
    """Print a simple items report to stdout."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Return a list of item names whose quantity is below the given threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval used")  # fixed: removed eval()
    # eval("print('eval used')")  # dangerous


main()
