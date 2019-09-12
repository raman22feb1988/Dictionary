import re

class Dictionary:
    def __init__(self):
        self.data = set([])
    def add(self, word):
        (self.data).add(word)
    def contains(self, word):
        return word in self.data
    def delete(self, word):
        if word in self.data:
            (self.data).remove(word)
    def replace(self, old_word, new_word):
        if old_word in self.data:
            (self.data).remove(old_word)
        (self.data).add(new_word)

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