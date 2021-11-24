# Беручи за основу структуру даних LinkedList, реалізувати неорієнтований зважений граф, який матиме наступний функціонал:
# 1. Додавання нових вершин
# 2. Додавання ребер між вершинами
# 3. Видалення ребер
# 4. Видалення вершини (з видаленням усіх ребер, що ведуть до неї)
# 4. Встановлення і змінення ваги ребра (значення ваги за замовчуванням - 1)
# 5. Виведення у тестовому представленні всіх наявних вершин і ребер між ними
# 6. Пошук найкоротшого шляху між двома вершинами

class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    # def __eq__(self, other):
    #     return self.name == other.name

    def add_neighbors(self, *args):
        for item in args:
            if isinstance(item, Vertex):
                if self.name != item and item not in self.neighbors:
                    self.neighbors.append(item)
            else:
                return False

    def del_neighbors(self, neighbors):
        for val in self.neighbors:
            if val.name == neighbors:
                self.neighbors.remove(val)
        return self.neighbors


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_graf_vertex(self, *args):
        for vertex in args:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors

    def del_neighbors(self, name, neighbors):
        # print(self.vertices)
        for kay, val in self.vertices.items():
            if name.name == kay:
                for item in val:
                    if item.name == neighbors.name:
                        # print(self.vertices[kay][val.index(item)])
                        self.vertices[kay].remove(item)
            elif neighbors.name == kay:
                for item in val:
                    # print(item)
                    if item.name == name.name:
                        # print('a')
                        self.vertices[kay].remove(item)

    def del_vertex(self, vertex):
        item = None
        for ver in self.vertices:
            if ver == vertex.name:
                item = ver
        self.vertices.pop(item)




if __name__ == '__main__':
    ver0 = Vertex(0)
    ver1 = Vertex(1)
    ver2 = Vertex(2)
    ver3 = Vertex(3)
    # ver4 = Vertex(4)
    # ver5 = Vertex(5)
    # ver6 = Vertex(6)
    # ver7 = Vertex(7)
    # ver8 = Vertex(8)
    ver0.add_neighbors(ver1, ver2, ver3)
    ver1.add_neighbors(ver0, ver2)
    ver2.add_neighbors(ver1, ver0)
    ver3.add_neighbors(ver0)
    # ver0.del_neighbors(1)
    # print(ver0.neighbors)

    # print(ver1.neighbors)
    # print(ver2.neighbors)
    # print(ver3.neighbors)

    graph = Graph()
    graph.add_graf_vertex(ver0, ver1, ver2, ver3)
    graph.del_vertex(ver1)
    # graph.del_neighbors(ver0, ver1)
    print(graph.vertices)