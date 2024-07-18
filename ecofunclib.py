from math import sqrt, log

# This file is a library of ecologic indices.
# a and b mean number of species at first and second trial site respectively
# c means number of joint species for both sites

species_sets = dict()


# Creates list of joint species using generator
# Returns jakkard index of two lists of species
def jakkard_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return c / (a + b - c)


# Returns Kulczinsky index of two lists of species
def kulczinsky_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return (c / 2) * ((1 / a) + (1 / b))


# Returns a Sorensen index of two sets of species
def sorensen_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return (2 * c) / (a + b)


# Returns an Ochiai index of two sets of species
def ochiai_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return c / (sqrt(a * b))


# Returns a Szymkiewicz-Simpson index of two sets if species
def szymkiewicz_simpson_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return c / min(a, b)


# Returns a Braun-Blanquet index of two sets of species
def braun_blanquet_index(first_species, second_species):
    joint_species = {item for item in first_species if item in second_species}
    a, b, c = len(first_species), len(second_species), len(joint_species)
    return c / max(a, b)


def shannon_weaver_index(species: dict):
    total_species_covering = sum(species.values())
    result = 0
    for i in species.keys():
        result -= (species[i] / total_species_covering) * log(species[i] / total_species_covering)
    return result


def simpson_index(species: dict):
    total_species_covering = sum(species.values())
    result = 1
    for i in species.keys():
        result -= (species[i] / total_species_covering)**2
    return result


def inverse_simpson_index(species: dict):
    total_species_covering = sum(species.values())
    total = 0
    for i in species.keys():
        total += (species[i] / total_species_covering)**2
    return 1 / total

def beta_whittaker_measure(sites) -> float:
    total_species = 0
    for species_list in sites:
        total_species += len(species_list)
    average_species = total_species / len(sites)
    return total_species / average_species



def convert_drude_to_projective_covering(drude_uranov: str in ['soc', 'cop3', 'cop2', 'cop1', 'sp', 'sol', 'un']) -> int:
    projective_covering: dict = {
        'soc' : 0.95,
        'cop3' : 0.75,
        'cop2' : 0.50,
        'cop1' : 0.25,
        'sp' : 0.03,
        'sol' : 0.02,
        'un' : 0.005
    }
    return projective_covering[drude_uranov]


def convert_braun_blanquet_to_projective_covering(braun_blanquet: str in ['soc', 'cop3', 'cop2', 'cop1', 'sp', 'sol', 'un']) -> int:
    projective_covering: dict = {
        '5' : 0.85,
        '4' : 0.50,
        '3' : 0.25,
        '2' : 0.03,
        '1' : 0.02,
        '+': 0.02,
        'r' : 0.005
    }
    return projective_covering[braun_blanquet]