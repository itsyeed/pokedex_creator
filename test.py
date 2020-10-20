import pokepy
import re

def main():
    """Main Method"""
    client = pokepy.V2Client()
    pokemon = client.get_pokemon(123)
    print(re.findall(r"(?<=[\/])[0-9]+(?=[\/])",
                     client.get_pokemon_species(150).evolution_chain.url)[0])
    # print(pokemon.name)                                                 #NAME
    # print(pokemon.height)                                               #HEIGHT
    # print(pokemon.weight)                                               #WEIGHT
    # print(client.get_move(pokemon.moves[0].move.name).id)               #MOVE ID
    # print(client.get_ability(pokemon.abilities[0].ability.name).id)     #ABILITY ID
    # print(pokemon.stats[0].stat.name)                                   #STAT NAME
    # print(pokemon.stats[0].base_stat)                                   #BASE VAL
    # print(pokemon.stats[0].effort)                                      #EFFORT VAL
    # print(pokemon.types[0].type.name)                                   #TYPES
    # print(client.get_growth_rate(1).name)                               #GROWTH RATE
    # print(client.get_gender(2).pokemon_species_details)                 #MFR IN 1/8THS
    # print(client.get_egg_group(1).name)                                 #EGG GROUP



if __name__ == '__main__':
    main()
