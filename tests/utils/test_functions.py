from pyturmite.utils.functions import (
    map_unique_states_list_to_digits,
    generate_all_rulesets_of_specified_length,
    nary_to_integer,
    ruleset_to_integer,
    ruleset_to_nary,
)
import pytest

@pytest.mark.parametrize(
    "input_list,expected_output",
    [
        (["L"], {"L": "0"}),
        (["L", "R"], {"L": "0", "R": "1"}),
        (["A", "B", "C"], {"A": "0", "B": "1", "C": "2"}),
    ],
)
def test_map_unique_states_list_to_digits(input_list, expected_output):
    assert map_unique_states_list_to_digits(input_list) == expected_output


@pytest.mark.parametrize(
    "input_states,length,expected_output",
    [
        (["L", "R"], 1, [("L",),("R",)]),
        (["L", "R"], 2, [("L","L"),("L","R"),("R","L"),("R","R"),]),
        (["L", "R"], 3, [
            ("L","L","L",),
            ("L","L","R",),("L","R","L",),("R", "L", "L",),
            ("L","R","R",),("R","L","R",),("R","R","L",),
            ("R","R","R",),
            ]),
    ],
)
def test_generate_all_rulesets_of_specified_length(input_states, length, expected_output):
    actual_output = generate_all_rulesets_of_specified_length(input_states, length)
    assert set(actual_output) == set(expected_output)


@pytest.mark.parametrize(
    "input_ruleset,expected_output",
    [
        ("LR", 2),
        ("LRR", 4),
        ("RRRLRRLLRLRRRRLLRRRLLRLR", 10960183),
    ]
)
def test_ruleset_to_integer(input_ruleset,expected_output):
    unique_states = ["R", "L"]
    input_mapping = map_unique_states_list_to_digits(unique_states)
    actual_output = ruleset_to_integer(input_ruleset,input_mapping)
    assert actual_output == expected_output

@pytest.mark.parametrize(
    "input_ruleset,expected_output",
    [
        ("10", 2),
        ("000", 0),
        ("11", 3),
        ("100", 4),
    ]
)
def test_nary_to_integer(input_ruleset,expected_output):
    actual_output = nary_to_integer(input_ruleset,{"L":"1", "R":0})
    assert actual_output == expected_output

@pytest.mark.parametrize(
    "input_ruleset,expected_output",
    [
        ("LR", "10"),
        ("LLR", "110"),
        ("LRR", "100"),
    ]
)
def test_ruleset_to_nary(input_ruleset,expected_output):
    actual_output = ruleset_to_nary(input_ruleset,{"L":"1", "R":0})
    assert actual_output == expected_output