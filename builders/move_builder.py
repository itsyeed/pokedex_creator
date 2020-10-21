"""
This module will use pokepy to send REST API requests to the PokeAPI to build
important components for our pokedex.

TODO:
    1) Abilties and Evolution JSON objects
"""

import json
import os
from beckett import exceptions as beckett_except
import pokepy
import jsbeautifier

def build_moves():
    """
    Args:
        None.
    Returns:
        An object that contains all infortmation we will be containing in our
        pokedex.
    Throws:
        TBD
    """

    moves = {}
    client = pokepy.V2Client()
    for i in range(1, 729):
        try:
            move = client.get_move(i)
        except beckett_except.InvalidStatusCodeError:
            break
        moves[i] = {}
        moves[i].update({"name":move.name})
        moves[i].update({"acc":move.accuracy})
        moves[i].update({"effect_chance":move.effect_chance})
        moves[i].update({"pp":move.pp})
        moves[i].update({"priority":move.priority})
        moves[i].update({"power":[move.power, move.damage_class.name]})
        moves[i].update({"ailment":move.meta.ailment.name})
        moves[i].update({"cat":move.meta.category.name})
        moves[i].update({"hits":[move.meta.min_hits, move.meta.max_hits]})
        moves[i].update({"turns":[move.meta.min_turns, move.meta.max_turns]})
        moves[i].update({"drain":move.meta.drain})
        moves[i].update({"heal":move.meta.healing})
        moves[i].update({"crit":move.meta.crit_rate})
        moves[i].update({"ail_chance":move.meta.ailment_chance})
        moves[i].update({"flinch":move.meta.flinch_chance})
        moves[i].update({"stat_chance":move.meta.stat_chance})
        moves[i].update({
            "stat_change":[[stat.change, stat.stat.name] for stat in move.stat_changes]
            })
        moves[i].update({"target":move.target.name})
        moves[i].update({"type":move.type.name})
        print("[DONE] ID: " + str(i) + " | NAME: " + move.name)
    return moves

def main():
    """MAIN FUNCTION"""
    my_moves = build_moves()
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    with open('../output/moves.json', 'w') as moves:
        moves.write(jsbeautifier.beautify(json.dumps(my_moves)))

    with open('../output/moves_min.json', 'w') as moves_min:
        json.dump(my_moves, moves_min)

if __name__ == '__main__':
    main()
