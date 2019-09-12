import re

class Dictionary:
    def __init__(self):
        self.data = {}
    def add(self, word):
        branch = self.data
        for letter in (word + '\0'):
            if letter not in branch:
                branch[letter] = {}
            branch = branch[letter]
    def contains(self, word):
        branch = self.data
        for letter in word:
            if letter not in branch:
                return False
            branch = branch[letter]
        if '\0' in branch:
            return True
        else:
            return False
    def delete(self, word):
        l = []
        match = True
        branch = self.data
        l.append(branch)
        for letter in word:
            if letter in branch:
                branch = branch[letter]
                l.append(branch)
            else:
                match = False
                break
        if match:
            Word = word + '\0'
            for node in range(len(l) - 1, -1, -1):
                Branch = l[node]
                if len(Branch[Word[node]]) == 0:
                    del Branch[Word[node]]
    def replace(self, old_word, new_word):
        if old_word != new_word:
            i = 0
            branch = self.data
            length = min(len(old_word), len(new_word))
            while i < length and old_word[i] == new_word[i]:
                branch = branch[old_word[i]]
                i += 1
            branch1 = branch
            for letter in (new_word[i:] + '\0'):
                if letter not in branch1:
                    branch1[letter] = {}
                branch1 = branch1[letter]
            l = []
            match = True
            branch2 = branch
            l.append(branch2)
            for letter in old_word[i:]:
                if letter in branch2:
                    branch2 = branch2[letter]
                    l.append(branch2)
                else:
                    match = False
                    break
            if match:
                Word = old_word[i:] + '\0'
                for node in range(len(l) - 1, -1, -1):
                    Branch = l[node]
                    if len(Branch[Word[node]]) == 0:
                        del Branch[Word[node]]

def main():
    d = Dictionary()
    f = open("Happiest-Minds-Sample.txt", "r")
    lines = (f.read()).split('\n')
    for line in lines:
        line = (re.sub('[^a-zA-Z]+', ' ', line)).lower()
        words = line.split(' ')
        for word in words:
            if len(word) > 0:
                d.add(word)
    print d.contains('the')
    print d.contains('them')
    f.close()

main()