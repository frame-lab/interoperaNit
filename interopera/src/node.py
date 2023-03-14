class Node:
    def __init__(
            self,
            name: str,
            childs: list[str]) -> None:
        self.name = name
        self.childs = childs

    def __repr__(self):
        return 'Base()'

    def __str__(self):
        return f'  {{\n' + \
            f'  name: {self.name} \n' + \
            f'  childs: {self.childs},\n' + \
            f'  }}\n'
