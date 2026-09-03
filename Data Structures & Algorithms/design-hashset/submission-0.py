class MyHashSet:

    def __init__(self):
        self.h=[]

    def add(self, key: int) -> None:
        flag=True
        for ch in self.h:
            if ch == key:
                flag=False
        if flag:
            self.h.append(key)

    def remove(self, key: int) -> None:
        for ch in self.h:
            if ch == key:
                self.h.remove(key)

    def contains(self, key: int) -> bool:
        for ch in self.h:
            if ch == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)