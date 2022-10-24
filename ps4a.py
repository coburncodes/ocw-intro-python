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

    # Start with any letter
    # Add another letter (any) into every position
    # Repeat above until no more letters
    # Print all entries 

    # Recursive case:
    # Take sequence:
    # Take letter
        # "A"
    # Include next letter before and after
        # "BA" && "AB"
    # Run program on new orders

    x = "bust"

    #   l = len(sequence)

    #   for i in range(l):
    #     if l > 1:
    #       sequence_next = sequence[1:l]
    #       get_permutations(sequence_next)
        
    #     else:
    #       print(list(sequence))
    #       return sequence


    # Base case: 
    # If seqeuence is single char, 
    if len(sequence) == 1:
        # Return singleton list containing sequence
        return list(sequence)
    # Recursive case:
    else:
        # Method that can give us a list of all permutations
        # of all but the first character in the sequence
        
        

    

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

