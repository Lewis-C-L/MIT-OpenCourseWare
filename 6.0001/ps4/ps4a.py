# Problem Set 4A
# Name: Lewis
# Collaborators:
# Time Spent: x:xx
import itertools
flatten = itertools.chain.from_iterable


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

    letters = [x for x in sequence]
    pos = 1
    new_sequences = [sequence[0]]
    while pos<len(letters):
        l = [[y[:x]+letters[pos]+y[x:] for x in range(pos+1)] for y in new_sequences]
        new_sequences = list(flatten(l))
        pos+=1
    return new_sequences
    
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print('input: "a"')
    print('Actual Output:',get_permutations('a'))
    print('input: "ab"')
    print('Actual Output:',get_permutations('ab'))
    print('input: "abc"')
    print('Actual Output:',get_permutations('abc'))

