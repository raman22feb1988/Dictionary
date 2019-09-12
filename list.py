import re

class Dictionary:
    def __init__(self):
        self.data = []
    def add(self, word):
        start = 0
        end = len(self.data)
        position = (start + end) / 2
        while start < end:
            position = (start + end) / 2
            if self.data[position] < word:
                start = position + 1
            else:
                end = position
        position = (start + end) / 2
        if len(self.data) == 0 or len(self.data) == position or self.data[position] != word:
            (self.data).insert(position, word)
    def contains(self, word):
        start = 0
        end = len(self.data)
        position = (start + end) / 2
        while start < end:
            position = (start + end) / 2
            if self.data[position] < word:
                start = position + 1
            else:
                end = position
        position = (start + end) / 2
        return len(self.data) > 0 and len(self.data) > position and self.data[position] == word
    def delete(self, word):
        start = 0
        end = len(self.data)
        position = (start + end) / 2
        while start < end:
            position = (start + end) / 2
            if self.data[position] < word:
                start = position + 1
            else:
                end = position
        position = (start + end) / 2
        if len(self.data) > 0 and len(self.data) > position and self.data[position] == word:
            del self.data[position]
    def replace(self, old_word, new_word):
        delete(old_word)
        add(new_word)

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