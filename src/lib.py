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
    if n <= 1:
        return True
    is_leaf = i > int((n - 2) / 2)
    if is_leaf:
        return True
    if heap[i] > heap[i * 2 + 1] or (i * 2 + 2 < n and heap[i] > heap[i * 2 + 2]):
        return False
    if is_heap(heap, n, i * 2 + 1) and (i * 2 + 2 >= n or is_heap(heap, n, i * 2 + 2)):
        return True
    else:
        return False


def print_heap(heap):
    elm_on_line = 1
    i_max = 0
    i_min = 0
    heap_string = []
    for index, item in enumerate(heap):
        if index > i_max:
            line = " ".join(["{:03d}".format(elm) for elm in heap[i_min:i_max + 1]])
            heap_string.append(line)
            elm_on_line = elm_on_line * 2
            i_min = i_max + 1
            i_max += elm_on_line
            last_line_len = len(line)
    line = " ".join(["{:03d}".format(elm) for elm in heap[i_min:i_max + 1]])
    last_line_len = len(line) if len(line) > last_line_len else last_line_len
    heap_string.append(line)
    for line in heap_string[:-1]:
        print("{text:^{pad}}".format(text=line, pad=last_line_len))
    print("{text}".format(text=heap_string[-1]))

