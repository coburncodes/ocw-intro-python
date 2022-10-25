# Problem Set 4A
# Name: Joe Coburn
# Collaborators: n/a
# Time Spent: 400 mins

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

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''



    # Create list from sequence
    sequence = list(sequence)
    # Container to pass data
    container = []

    # Base case
    if len(sequence) == 1:
        return [sequence]
    # Recursive case
    for i in range(len(sequence)):
        # Save current letter and the rest of the sequence
        current = sequence[i]
        remaining = sequence[:i] + sequence[i+1:]

        for j in get_permutations(remaining):
            container.append([current] + remaining)

    return container

x = 'abc'
for item in get_permutations(x):
    print([item][0])

    

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

