# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class WordDictionary:

    def __init__(self):
        self.root = Word()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Word(c)
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self._searchHelper(self.root, word)

    def _searchHelper(self, cur, word):
        if not word:
            return True if cur.is_end else False
        if word[0] == '.':
            for child in cur.children.values():
                found = self._searchHelper(child, word[1:])
                if found:
                    return True
            return False
        elif word[0] not in cur.children:
            return False
        return self._searchHelper(cur.children[word[0]], word[1:])
class Word:
    def __init__(self, val=''):
        self.val = val
        self.is_end = False
        self.children = {}


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)