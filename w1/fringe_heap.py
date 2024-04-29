from heap import Heap, Node
from state import State


class FringeHeap:
    def __init__(self, maxsize: int) -> None:
        self._heap = Heap()
        self._maxsize = maxsize

    def full(self) -> bool:
        return self._maxsize < self._heap.get_size()

    def qsize(self) -> int:
        return self._heap.get_size()

    def empty(self) -> bool:
        return self._heap.get_size() == 0

    def update_priority(self, item: Node | int, priority: float) -> None:
        self._heap.update_priority(item, priority)

    def put(
        self, item: State, block
    ) -> None:  # ignore block is forced on us by "fringe" design
        self._heap.enqueue(Node(hash(item.get_room()), item), item.cost)

    def get(self) -> State:
        res = self._heap.remove_min()[0].state
        if isinstance(res, State):
            return res
        raise Exception("Wrong type of node data")
