"""
Words Concatenation (hard) #
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""


def find_word_concatenation(str, words):
    word_length = len(words[0])
    total_words = len(words)
    word_freq = {}

    # Initialize the word frequency dictionary
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    result_indices = []

    for i in range(len(str) - total_words * word_length + 1):
        words_seen = {}
        for j in range(total_words):
            next_word_index = i + j * word_length
            word = str[next_word_index:next_word_index + word_length]

            # If the current word is not in word_freq, we can't form a concatenation
            if word not in word_freq:
                break

            # Add the word to the words_seen dictionary
            if word in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1
           
                

            # If the frequency of the current word is more than required, break
            if words_seen[word] > word_freq.get(word, 0):
                break

            # If all words are seen with the right frequency, add the index to the result
            if j + 1 == total_words:
                result_indices.append(i)

    return result_indices


# Test cases
print(find_word_concatenation("catfoxcat", ["cat", "fox"]))  # Output: [0, 3]
print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))  # Output: [3]
