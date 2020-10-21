"""
This module will use pokepy to send REST API requests to the PokeAPI to build
important components for our pokedex.

TODO:
    1) Abilties and Evolution JSON objects
"""

import json
from beckett import exceptions as beckett_except
import pokepy
import jsbeautifier

def build_items():
    """
    Args:
        None.
    Returns:
        An object that contains all infortmation we will be containing in our
        pokedex.
    Throws:
        beckett.exceptions.InvalidStatusCodeError
    """

    items = {}
    client = pokepy.V2Client()
    i = 1
    while True:
        try:
            item = client.get_item(i)
        except beckett_except.InvalidStatusCodeError:
            break
        items[i] = {}
        items[i].update({"name":item.name})
        items[i].update({"attr":[attr.name for attr in item.attributes]})
        items[i].update({"cat":item.category.name})
        items[i].update({
            "fling":[item.fling_power,
                     item.fling_effect.name if item.fling_effect is not None else None]
            })
        items[i].update({"cost":item.cost})
        print("[DONE] ID: " + str(i) + " | NAME: " + item.name)
        i += 1
    return items

def main():
    """MAIN FUNCTION"""
    my_items = build_items()
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    with open('../output/items.json', 'w') as items:
        items.write(jsbeautifier.beautify(json.dumps(my_items)))

    with open('../output/items_min.json', 'w') as items_min:
        json.dump(my_items, items_min)

if __name__ == '__main__':
    main()
