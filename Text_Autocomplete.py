"""
Q2: catGPT
"""
import math


class Node:
    def __init__(self, data=None, size=27):
        """
        Function description: To initialise the attributes of a node

        Input:
            self: the instance of Node
            data: data which stores the sentence
            size: the size of link, default is 27 because of 26 letters + $
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        # terminal $ at index 0
        self.link = [None] * size
        # data payload
        self.data = data
        self.frequency = 0
        self.isEnd = False


class CatsTrie:
    def __init__(self, sentences):
        """
        Function description: To initialise the Trie data structure

        Input:
            self: the instance of CatsTrie
            sentences: a list of timelines represented as a list of string
        Return:
            None

        Time complexity:
            Best: O(1)
            Worst: O(1)
        Space complexity:
            Input: O(L), L is the length of sentences
            Aux: O(1)
        """
        self.root = Node()
        for sentence in sentences:
            self.insert_recur(sentence)

    def insert_recur(self, key):
        """
        Function description: To insert the key into the instance of Trie

        Input:
            self: the instance of CatsTrie
            key: the key of each node in Trie
        Return:
            None

        Time complexity:
            Best: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
            Worst: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
        Space complexity:
            Input: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
            Aux: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
        """
        current = self.root
        self.insert_recur_aux(current, key, 0)

    def insert_recur_aux(self, current, key, i=0):
        """
        Function description: The recursion function to insert the key into the instance of Trie

        Input:
            self: the instance of CatsTrie
            current: the current node
            key: the key of each node in Trie
            i: the index for current node
        Return:
            None

        Time complexity:
            Best: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
            Worst: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
        Space complexity:
            Input: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
            Aux: O(N * M), N is the number of sentence in sentences, M is the number of characters in the longest sentence
        """
        # Base case
        if i == len(key):
            # This is the end node, so the index is 0
            index = 0
            if current.link[index] is not None:
                current = current.link[index]
                current.frequency += 1
            else:
                current.link[index] = Node()
                current = current.link[index]
                current.frequency += 1
            current.data = key
            # Since it is the end node, set isEnd is True
            current.isEnd = True
            return True
        # Recursion
        else:
            # Get the index of char and $, then $ = 0, a = 1, b = 2
            index = ord(key[i]) - 97 + 1
            # If path exists, go to next node
            if current.link[index] is not None:
                current = current.link[index]
            # If path does not exist
            else:
                # Create a new node, then go to next node
                current.link[index] = Node()
                current = current.link[index]
            # Recursion Call
            self.insert_recur_aux(current, key, i + 1)

    def autoComplete(self, prompt):
        """
        Function description: To find one highest frequency completed sentence for prompt in sentences list

        Approach: This function can find one highest frequency completed sentence for prompt in sentences list,
                  It uses the recursion function to find

        Input:
            self: the instance of CatsTrie
            prompt: a string with characters in the set of [a...z]
        Return:
            max_sentence: one highest frequency completed sentence for prompt in sentences list

        Time complexity:
            Best: O(X + Y), X is the length of prompt,
                            Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
            Worst: O(X + Y), X is the length of prompt,
                             Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
        Space complexity:
            Input: O(X + Y), X is the length of prompt,
                             Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
            Aux: O(X + Y), X is the length of prompt,
                           Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
        """
        current = self.root

        for char in prompt:
            index = ord(char) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]
            # If sentences doesn't exist
            else:
                return None
        max_frequency, max_sentence = self.find_most_frequent(current)
        return max_sentence

    def find_most_frequent(self, current):
        """
        Function description: The recursion function to find one highest frequency completed sentence for prompt in sentences list

        Approach: This function can find one highest frequency completed sentence for prompt in sentences list,
                  it can auto find depends on the prompt:
                  if this prefix exists, then will find the highest frequency completed sentence include this prefix;
                  if this prefix does not exist, then will return None;
                  if there are more than one sentences have same frequency,
                  it returns the sentence order by lexicographical smaller string
                  In this case, I need to use frequency and data to save in each node and compare

        Input:
            self: the instance of CatsTrie
            current: the current node
        Return:
            max_frequency, max_sentence: a tuple which is the frequency and sentence of
                                         one highest frequency completed sentence for prompt in sentences list

        Time complexity:
            Best: O(X + Y), X is the length of prompt,
                            Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
            Worst: O(X + Y), X is the length of prompt,
                             Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
        Space complexity:
            Input: O(X + Y), X is the length of prompt,
                             Y is the length of the most frequent sentence in sentences that begins with the prompt in the link
            Aux: O(X + Y), X is the length of prompt,
                           Y is the length of the most frequent sentence in sentences that begins with the prompt in the link

        The complexity would be O(X), when the sentence do not exist
        """
        max_frequency = 0
        max_sentence = ""

        # Check if reach the end node
        if current.isEnd:
            # Compare current frequency and update the current maximum frequency and sentence
            if current.frequency > max_frequency:
                max_frequency = current.frequency
                max_sentence = current.data
            # When the sentence of frequency are same, choose the smaller one by lexicographical
            elif current.frequency == max_frequency and current.data < max_sentence:
                max_sentence = current.data

        # This is the recursion to check all the next nodes
        for link in current.link:
            if link is not None:
                # Get the necessary data (need to compare below) from the next node
                next_frequency, next_sentence = self.find_most_frequent(link)
                # Compare next frequency and update the current maximum frequency and sentence
                if next_frequency > max_frequency:
                    max_frequency = next_frequency
                    max_sentence = next_sentence
                # When the sentence of frequency are same, choose the smaller by lexicographical
                elif next_frequency == max_frequency and next_sentence < max_sentence:
                    max_sentence = next_sentence

        return max_frequency, max_sentence
