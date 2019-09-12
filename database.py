import re
import sqlite3

class Dictionary:
    def __init__(self):
        self.connection = sqlite3.connect("dictionary.db")
        self.crsr = (self.connection).cursor()
        (self.crsr).execute("CREATE TABLE IF NOT EXISTS words(word TEXT primary key)")
    def add(self, word):
        try:
            (self.crsr).execute("INSERT INTO words VALUES(?)", (word,))
        except sqlite3.IntegrityError as ex:
            None
        finally:
            (self.connection).commit()
    def contains(self, word):
        (self.crsr).execute("SELECT COUNT(word) FROM words WHERE word = ?", (word,))
        result = (self.crsr).fetchall()
        if result[0][0] > 0:
            return True
        else:
            return False
    def delete(self, word):
        (self.crsr).execute("DELETE FROM words WHERE word = ?", (word,))
        (self.connection).commit()
    def replace(self, old_word, new_word):
        try:
            (self.crsr).execute("UPDATE words SET word = ? WHERE word = ?", (new_word, old_word))
        except sqlite3.IntegrityError as ex:
            None
        finally:
            (self.connection).commit()

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
    (d.connection).close()
    f.close()

main()