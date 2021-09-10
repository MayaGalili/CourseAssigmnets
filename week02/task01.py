"""
Given a dictionary containing N words and a new set of Q query words, your goal is to print the
smallest words from the original dictionary for which the query word is a prefix.
The Q words were typed really fast and  some typos may have occurred.
You should find matches considering at most 1 typo only.
A “typo” means an incorrect character was typed instead of the correct one.
For example, “the -> tje” or “test -> tast” have 1 typo, but “the -> teh” has 2 typos.
Additional and missing characters, such as "the" -> "thje" and "the" -> "te", are not considered typos.

If there are more than 10 matches, print only the smallest 10 matches. Otherwise print all of them.

See the samples for explanation.



Input
-------
You will be given an integer N (1 <= N <= 105) representing the number of words in the original
dictionary, followed by N words. An integer Q (1 <= Q <= 105) representing the number of query words will then be given, followed by Q query words. Each word contains only lowercase latin letters. Words in the dictionary or the queries may appear multiple times.

The length of a single word is at most 105. The sum of all words' lengths in the dictionary is at most 3 * 105 and the sum of all query words is at most 3 * 105.



Output
---------
For each word in the Q query words, find the smallest words in the original dictionary that have the
query word as a prefix. If there are more than 10 matches, print only the smallest 10.
Otherwise print all of them. The printed words should be ordered from smallest to largest lexicographically.
If the same word appears multiple times in the dictionary, it should be considered only once in the output.

The output per query should be in a single line and words separated by spaces.

If there are no matches at all, print "<no matches>" without the quotations.

See the samples for further elaboration.

Examples
--------------
Input
7
the
computer
technology
elevate
compute
elevator
company
4
the
new
techn
compa


Output

tech technology

<no matches>

technology

company compute computer



Notes

In the first query, the word was "tevh", which does not match any words.
However, considering that 'v' is a typo and that the intended character was possibly 'c',
then it matches "tech" and "technology".

The same occurs with the last query "compa". It of course matches "company" with 0 errors.
It also matches "compute" and "computer" since the prefixes "compu" and "compa" differ by only one character.

"""

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord


def solve(dictionary, queries):
    # Build prefix tree from the dictionary
    # search each word from the query in the prefix tree
    # during the search - if 1 typo - continue in the tree search
    # if the query ended during the search - add it to the query result list
    # Write your code here ...
    # Trie object
    output = ["Not present in trie",
              "Present in trie"]
    t = Trie()

    # Construct trie
    for key in dictionary:
        t.insert(key)

    for q in queries:
        print(output[t.search(q)])


def main():
    dict_size = int(input())
    dictionary = []
    for _ in range(dict_size):
        dict_word = input()
        dictionary.append(dict_word)
    query_size = int(input())
    queries = []
    for _ in range(query_size):
        query = input()
        queries.append(query)
    solve(dictionary, queries)


if __name__ == "__main__":
    main()