def bubble_up(heap, elm_index):
    """
    Bubble up an element from a heap until it is at his right place
    """
    newitem = heap[elm_index]
    while elm_index > 0:
        parentpos = (elm_index - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[elm_index] = parent
            elm_index = parentpos
            continue
        break
    heap[elm_index] = newitem


def is_heap(heap, n, i=0):
    is_leaf = i > int((n - 2) / 2)
    if is_leaf:
        return True
    if heap[i] > heap[i * 2 + 1] or heap[i] > heap[i * 2 + 2]:
        return False
    if is_heap(heap, n, i * 2 + 1) and is_heap(heap, n, i * 2 + 2):
        return True
    else:
        return False
