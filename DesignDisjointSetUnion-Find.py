#Design a Disjoint Set (aka Union-Find) class.
#
#Your UnionFind class should support the following operations:
#
#UnionFind(int n) will initialize a disjoint set of size n.
#int find(int x) will return the root of the component that x belongs to.
#bool isSameComponent(int x, int y) will return whether x and y belong to the same component.
#bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.
#int getNumComponents() will return the number of components in the disjoint set.
#Example 1:
#
#Input:
#["UnionFind", 10, "isSameComponent", 1, 3, "union", 1, 2, "union", 2, 3, "getNumComponents", "isSameComponent", 1, 3]
#
#Output:
#[null, 1, false, true, true, 8, true]
#Note: The find method will not be directly tested, but you will need to use it in the implementation of the other methods. Thus, it will be tested indirectly.
#
#
class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_compents = n

    def find(self, x: int) -> int:

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def isSameComponent(self, x: int, y: int) -> bool:
        parent1, parent2 = self.find(x), self.find(y)
        return parent1 == parent2


    def union(self, x: int, y: int) -> bool:
        parent1, parent2 = self.find(x), self.find(y)
        if parent1 != parent2:
            if self.size[parent1] < self.size[parent2]:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
            else:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            self.num_compents -= 1
            return True
        return False


    def getNumComponents(self) -> int:
        return self.num_compents


