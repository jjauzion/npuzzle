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
