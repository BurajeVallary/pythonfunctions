#Question 1

#A function named concatenate_args that takes
# any number of string arguments in positional 
#arguments format and concatenates them into a single string



def concatenate_args(*args):
    empty=(" ")
    for b in args:
        empty+=b

    return empty    

#Question2
#A function named concatenate_kwargs that 
# takes any number of string arguments in keyword
#  arguments  format and concatenates them into a single string
def concatenate_kwargs(**str):
    strings=""
    for key,value in str.items():
        str +=(f"{key},{value}, ")

    return strings    