"""
A "binary ant" uses only L (1) and R (0), so the ruleset LR can be
 written `10`, which in binary is 2, so "LR" is also known as ant #2
 
This script generates and saves images of the movement of all
 binary ants up to a user defined number N
 
"""

from pyturmite.utils.functions import (
    map_unique_states_list_to_digits,
    generate_all_rulesets_of_specified_length,
)

IMAGE_SAVE_PATH = './scripts/images/'

## Generate rulesets for all L,R combinations between these lengths
GENERATE_FROM_ANT_NUMBER = 2
GENERATE_TO_ANT_NUMBER = 4
UNIQUE_STATES_LIST = ["L", "R"] # unique states that define the ruleset space

unique_states_mapped_to_digits = map_unique_states_list_to_digits(UNIQUE_STATES_LIST)

for ruleset_length in range(GENERATE_FROM_ANT_NUMBER, GENERATE_TO_ANT_NUMBER+1):
    print(f"ruleset_length={ruleset_length}") 
    rulesets = generate_all_rulesets_of_specified_length(UNIQUE_STATES_LIST, length=ruleset_length)
    print(rulesets)


    ### TODO: What to do with rulesets of "RRRR.." type
    ### since this is 0000 in binary and thus equal to 0