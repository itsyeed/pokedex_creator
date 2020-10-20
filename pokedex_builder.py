"""
This module will use pokepy to send REST API requests to the PokeAPI to build
important components for our pokedex.

TODO:
    1) Berry and Item JSON objects
    2) Descriptions
    3) How will we handle evolution chains? Evolution levels? Evolution items and methods?
    4) Characteristics!!! IVs!!!!
    5) Max level and Max experience
    6) Natures?
    7) Encounters? location_area_encounters
    8) Use PokeAPI sprites?
    9) Pokemon move learned at levels?
    10) Pokemon  with different forms?
    11) All of GEN II included?
"""

import json
import re
import pokepy

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
    for i in range(1, 152):
        pokemon_species = requester.get_pokemon_species(i)
        pokemon = requester.get_pokemon(i)
        pokedex[i] = {"name":pokemon.name}
        pokedex[i].update({"height":pokemon.height})
        pokedex[i].update({"weight":pokemon.weight})
        pokedex[i].update({
            "moves":[requester.get_move(move.move.name).id for move in pokemon.moves]
            })
        pokedex[i].update({
            "abilities":[requester.get_ability(ability.ability.name).id for ability in pokemon.abilities]
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
        pokedex[i].update({"capture rate":pokemon_species.capture_rate})
        pokedex[i].update({
            "evolve":re.findall(r"(?<=[\/])[0-9]+(?=[\/])",
                                pokemon_species.evolution_chain.url)[0]
            })
        pokedex[i].update({"habitat":pokemon_species.habitat.name})
        print("[DONE] ID: " + str(i) + " | NAME: " + pokemon.name)
    return pokedex

def main():
    """Main Method"""
    my_pokedex = build_pokedex()
    with open('pokedex.json', 'w') as pokedex:
        json.dump(my_pokedex, pokedex, indent=4)

if __name__ == '__main__':
    main()
