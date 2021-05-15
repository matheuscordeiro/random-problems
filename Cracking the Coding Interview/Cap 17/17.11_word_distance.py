cache = {}

class PaiWords:

    def __init__(self, word1, word2,) -> None:
        self.word2 = word2
        self.pos_word1 = -1
        self.pos_word2 = -1

    @property
    def distance(self,):
        return abs(self.pos_word1 - self.pos_word2)

    def update_pos_word1(self, post_word1):
        if (self.pos_word1 == -1 and self.pos_word2 == -1) or self.pos_word2 == -1:
            self.pos_word1 = post_word1
        elif self.distance > abs(self.pos_word2 - post_word1):
            self.pos_word1 = post_word1

    def update_pos_word2(self, post_word2):
        if (self.pos_word1 == -1 and self.pos_word2 == -1) or self.pos_word1 == -1:
            self.pos_word2 = post_word2
        elif self.distance > abs(self.pos_word1 - post_word2):
            self.pos_word2 = post_word2

    

def find_min_distance(words, word1, word2):
    pair = PaiWords(word1, word2)
    cache[word1] = []
    cache[word2] = []
    for key, value in enumerate(words):
        if value == word1:
            pair.update_pos_word1(key)
            cache[word1].append(key)
        elif value == word2:
            pair.update_pos_word2(key)
            cache[word2].append(key)


def find_min_distance_array(A, B):
    i = j = 0
    min_distance = abs(A[i] - B[j])
    while i < len(A) and j < len(B):
        if abs(A[i] - B[j]) < min_distance:
            min_distance = abs(A[i] - B[j])
        
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    
    return min_distance


if __name__ == "__main__":
    A = [1,5,8,10]
    B = [3,14,15]
    print(find_min_distance_array(A, B))
