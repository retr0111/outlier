from time import process_time
from typing import Optional

class Word:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector

    def similarity(self, other_word):
        # Implement your similarity measure here
        pass

class Model(list):
    features = 300

    def __init__(self, inp_file_name: str) -> None:
        super().__init__()
        print(f"Loading model from {inp_file_name} ...")
        t0 = process_time()
        with open(inp_file_name) as inp_file:
            for line in inp_file:
                sa = line.split()
                if len(sa) != Model.features + 1:
                    continue
                self.append(Word(sa[0], [float(x) for x in sa[1:]]))
        print(f"Loaded in {process_time() - t0} secs")

    def find_word(self, text: str) -> Optional[Word]:
        for w in self:
            if w.text == text:
                return w

    def find_similar_words(self, word: Word, n: int = 10) -> list[Word]:
        return sorted(self, key=lambda w: w.similarity(word), reverse=True)[:n]
