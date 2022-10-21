# Problem Set 4A
# Name: Joe Coburn
# Collaborators: n/a
# Time Spent: 2:15pm - 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    ['012', '021', '102', '120', '201', '210']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Start with the last letter
        # [ "C" ]
    # For each list, Take each entry and append next-last letter in sequence
    # to ith position in a loop
        # [ "BC" ] && [ "CB" ]
    # For each list, Take each entry and append next-last letter in sequence
    # to ith position in a loop
        #  [ "ABC" ] [ "BAC" ] [ "BCA" ] && [ "ACB" ] [ "CAB" ] [ "CBA" ]
    # Take each entry and add to new list
    # print each entry in list

    # Start with any letter
    # Add another letter (any) into every position
    # Repeat above until nno more letters
    # Print all entries 

    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

