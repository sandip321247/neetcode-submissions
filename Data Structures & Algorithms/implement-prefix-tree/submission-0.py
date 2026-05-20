class PrefixTree:

    def __init__(self):
        self.array = []

        

    def insert(self, word: str) -> None:
        self.array.append(word)


    def search(self, word: str) -> bool:
        if word in self.array :
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for i in range(len(self.array)):
            if self.array[i][:n] == prefix:
                return True
        return False