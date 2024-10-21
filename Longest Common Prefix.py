def longest_common_prefix(strs):
    """
    Function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    
    :param strs: List of strings
    :return: Longest common prefix or an empty string if no common prefix exists
    """
    if not strs:
        return ""

    # Sort the list of strings to compare the shortest string with the longest one
    strs.sort()
    
    # Compare characters between the first and last string in the sorted list
    first, last = strs[0], strs[-1]
    i = 0
    
    # Find the common prefix by comparing characters
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    # The substring from the start to index i is the common prefix
    return first[:i]


# Example usage
if __name__ == "__main__":
    sample_strings = ["flower", "flow", "flight"]
    print("Longest Common Prefix:", longest_common_prefix(sample_strings))
