import itertools

def map_unique_states_list_to_digits(unique_states_list)->dict[str, str]:
    unique_states_mapped_to_digits = {s: str(x) for x, s in enumerate(unique_states_list)}
    return unique_states_mapped_to_digits


def generate_all_rulesets_of_specified_length(unique_state_list, length)->list[tuple]:
    return list(itertools.product(unique_state_list, repeat=length))


def ruleset_to_nary(ruleset, mapping)->str:
    """
    Take a ruleset e.g. RL and convert it to a -nary string 
    (-nary would be bi-nary in this example)
    """
    return ''.join([str(mapping[x]) for x in ruleset])


def nary_to_integer(nary_string, mapping)->int:
    radix = len(mapping)
    return int(nary_string, radix)


def ruleset_to_integer(ruleset, mapping)->int:
    ruleset_as_nary = ruleset_to_nary(ruleset, mapping)
    return nary_to_integer(ruleset_as_nary, mapping)