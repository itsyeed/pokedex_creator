"""
This module will use pokepy to send REST API requests to the PokeAPI to build
important components for our pokedex.

TODO:
    1) Abilties and Evolution JSON objects
"""

import json
import re
import pokepy
import jsbeautifier

def build_pokedex():
    """
    Args:
        None.
    Returns:
        An object that contains all infortmation we will be containing in our
        pokedex.
    Throws:
        TBD
    """

    pokedex = {}
    requester = pokepy.V2Client()
    for i in range(1, 252):
        pokemon_species = requester.get_pokemon_species(i)
        pokemon = requester.get_pokemon(i)
        pokedex[i] = {"name":pokemon.name}
        pokedex[i].update({"height":pokemon.height})
        pokedex[i].update({"weight":pokemon.weight})
        pokedex[i].update({
            "moves":[
                [requester.get_move(move.move.name).id,
                 move.version_group_details[0].level_learned_at,
                 move.version_group_details[0].move_learn_method.name] for move in pokemon.moves]
            })
        pokedex[i].update({
            "abilities":[
                requester.get_ability(ability.ability.name).id for ability in pokemon.abilities
                ]
            })
        pokedex[i].update({"stats":{}})
        for stat in pokemon.stats:
            pokedex[i]["stats"].update({
                "{0}".format(stat.stat.name):{"base":stat.base_stat, "ev":stat.effort}
                })
        pokedex[i].update({
            "types":[p_type.type.name for p_type in pokemon.types]
            })
        pokedex[i].update({"growth":pokemon_species.growth_rate.name})
        pokedex[i].update({"gender":pokemon_species.gender_rate})
        pokedex[i].update({"egg":[egg.name for egg in pokemon_species.egg_groups]})
        pokedex[i].update({"happiness":pokemon_species.base_happiness})
        pokedex[i].update({"hatch":pokemon_species.hatch_counter})
        pokedex[i].update({"gender_diff":pokemon_species.has_gender_differences})
        pokedex[i].update({"capture_rate":pokemon_species.capture_rate})
        pokedex[i].update({
            "evolve":re.findall(r"(?<=[\/])[0-9]+(?=[\/])",
                                pokemon_species.evolution_chain.url)[0]
            })
        pokedex[i].update({"habitat":pokemon_species.habitat.name})
        pokedex[i].update({
            "desc":pokemon_species.flavor_text_entries[0].flavor_text.replace("\n", " ")
            })
        print("[DONE] ID: " + str(i) + " | NAME: " + pokemon.name)
    return pokedex

def main():
    """Main Method"""
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    my_pokedex = build_pokedex()
    with open('output/pokedex.json', 'w') as pokedex:
        pokedex.write(jsbeautifier.beautify(json.dumps(my_pokedex)))

    with open('output/pokedex_min.json', 'w') as pokedex_min:
        json.dump(my_pokedex, pokedex_min)
if __name__ == '__main__':
    main()
