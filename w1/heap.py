"""
File:    heap.py
Authors: Jakub Janicek (j.janicek@student.rug.nl), Matei Tanasa (m.tanasa@student.rug.nl)
Description:
    Implements heap inspired by the lecture code (this is a reference :]).
"""

from __future__ import annotations


class Node:
    """A generic node with data we want to keep"""

    def __init__(self, _id, state) -> None:
        self.id: int = _id
        self.state: object = state


class PriorityItem:
    """Object holding a City along with its priority. Used to simplify the heap"""

    def __init__(self, node: Node, priority: float) -> None:
        self.node = node
        self.priority = priority

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PriorityItem):
            return False
        return self.priority == other.priority

    def __lt__(self, other: PriorityItem) -> bool:
        return self.priority > other.priority

    def __gt__(self, other: PriorityItem) -> bool:
        return self.priority < other.priority

    def __le__(self, other: PriorityItem) -> bool:
        if self == other:
            return True
        return self.priority > other.priority

    def __ge__(self, other: PriorityItem) -> bool:
        if self == other:
            return True
        return self.priority < other.priority

    def __hash__(self) -> int:
        return self.node.id


class Heap:
    """A heap implementaiton loosely based on the one provided in the lecture"""

    def __init__(self) -> None:
        self._heap: list[PriorityItem] = [None]  # intentional type violation
        self._reverse_lookup: dict[int, int] = {}
        self._size = 0

    def _upheap(self, index: int) -> None:
        """Executes the upheap fuction - moves necessart nodes up the heap

        Args:
            index (int): An index at which to upheap
        """

        parrent_idx = index // 2
        if index > 1 and self._heap[index] > self._heap[parrent_idx]:
            self._heap[index], self._heap[parrent_idx] = (
                self._heap[parrent_idx],
                self._heap[index],
            )

            node_idx = self._heap[index].node.id
            par_node_idx = self._heap[parrent_idx].node.id

            self._reverse_lookup[node_idx], self._reverse_lookup[par_node_idx] = (
                self._reverse_lookup[par_node_idx],
                self._reverse_lookup[node_idx],
            )

            self._upheap(parrent_idx)

    def _downheap(self, index: int) -> None:
        """Executes the downheap fuction - moves necessary nodes down the heap

        Args:
            index (int): An index at which to downheap
        """

        if index <= self._size:
            lc = 2 * index
        rc = (2 * index) + 1 if index < self._size else lc

        if lc > self._size or rc > self._size:
            return

        if self._heap[lc] > self._heap[index] and self._heap[lc] >= self._heap[rc]:
            self._heap[lc], self._heap[index] = self._heap[index], self._heap[lc]

            node_idx = self._heap[index].node.id
            lc_node_idx = self._heap[lc].node.id

            self._reverse_lookup[node_idx], self._reverse_lookup[lc_node_idx] = (
                self._reverse_lookup[lc_node_idx],
                self._reverse_lookup[node_idx],
            )

            self._downheap(lc)

        elif self._heap[rc] > self._heap[index]:
            self._heap[rc], self._heap[index] = self._heap[index], self._heap[rc]

            node_idx = self._heap[index].node.id
            rc_node_idx = self._heap[rc].node.id

            self._reverse_lookup[node_idx], self._reverse_lookup[rc_node_idx] = (
                self._reverse_lookup[rc_node_idx],
                self._reverse_lookup[node_idx],
            )

            self._downheap(rc)

    def _update_size(self) -> None:
        """Updates size of the heap"""

        self._size = len(self._heap) - 1

    def enqueue(self, item: Node, priority: float) -> None:
        """Adds an item to the heap. Only callable before remove_min is called

        Args:
            item (City): An item to add
            priority (float): priority

        Raises:
            Exception: Negative priority - thrown when negative priority is assigned to item
        """

        if priority < 0:
            raise Exception("Negative priority")

        self._heap.append(PriorityItem(item, priority))
        self._update_size()
        self._reverse_lookup[item.id] = self._size
        self._upheap(self._size)

    def remove_min(self) -> tuple[Node, float]:
        """Removes the item with lowest priority from the heap

        Raises:
            Exception: Heap empty error - thrown when removed is called on empty heap

        Returns:
            tuple[City, float]: City with the lowest priority, priority
        """

        item = self._heap[1]
        new_item = self._heap.pop()
        self._update_size()
        del self._reverse_lookup[item.node.id]

        if self._size > 0:
            self._heap[1] = new_item
            self._downheap(1)
            self._reverse_lookup[self._heap[1].node.id] = 1

        return item.node, item.priority

    def update_priority(self, item: Node | int, priority: float) -> None:
        """Updates the priority of specific item

        Args:
            item (City | int): An item (city) to update the priority for
            priority (float): priority

        Raises:
            Exception: Negative priority - thrown when negative priority is assigned to item
            Exception: Access to nonexistent value - thrown when nonexistent item is to be updated
        """

        if priority < 0:
            raise Exception("Negative priority")

        if isinstance(item, Node):
            item = item.id

        if item not in self._reverse_lookup.keys():
            raise Exception("Access to nonexistent value")

        lookup_index: int = self._reverse_lookup[item]
        self._heap[lookup_index].priority = priority
        self._upheap(lookup_index)
        self._downheap(lookup_index)

    def get_lookup_keys(self):
        """Returns the keys used in the reverse lookup table

        Returns:
            dict_keys[int, int]: Reverse lookup table
        """
        return self._reverse_lookup.keys()

    def get_size(self):
        """Returns the size of the heap

        Returns:
            int: Returns the size of the heap
        """
        return self._size
