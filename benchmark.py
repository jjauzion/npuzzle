import numpy as np

from src import config


def bench_mark_dico(nb_iter, MOVE_DIC):
    for i in range(nb_iter):
        for key in MOVE_DIC:
            var = MOVE_DIC[key]


def bench_mark_list(nb_iter, MOVE):
    for i in range(nb_iter):
        for key in MOVE:
            var = key


def bench_mark_list_2(nb_iter):
    for i in range(nb_iter):
        MOVE = config.MOVE_LIST
        for key in MOVE:
            var = key


def bench_mark_list_3(nb_iter):
    for i in range(nb_iter):
        for key in config.MOVE_LIST:
            var = key


def bench_str_comparison(nb_iter, string, match):
    for i in range(nb_iter):
        for test in match:
            if string == test:
                var = True


def bench_lst_comparison(nb_iter, lst, match):
    for i in range(nb_iter):
        for test in match:
            if lst == test:
                var = True


def bench_nparray_comparison(nb_iter, array, match):
    for i in range(nb_iter):
        for test in match:
            if np.array_equal(test, array):
                var = True


def bench_nparray_creation(nb_iter):
    for i in range(nb_iter):
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def bench_list_creation(nb_iter):
    for i in range(nb_iter):
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(lambda: bench_list_creation(10000))
    print("list creation exe time : {}".format(t.timeit(number=100)))
    t = Timer(lambda: bench_nparray_creation(10000))
    print("nparray creation exe time : {}".format(t.timeit(number=100)))

    lst = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    match = [lst, [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
    t = Timer(lambda: bench_lst_comparison(10000, lst, match))
    print("list comparison time : {}".format(t.timeit(number=100)))
    string = "111111111"
    match = [string, "123456789", "987654321"]
    t = Timer(lambda: bench_str_comparison(10000, string, match))
    print("str comparison time : {}".format(t.timeit(number=100)))
    array = np.arange(9)
    match = [array, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])]
    t = Timer(lambda: bench_nparray_comparison(10000, array, match))
    print("numpy array comparison time : {}".format(t.timeit(number=100)))

    MOVE_LST = [1, 2, 3, 4]
    t = Timer(lambda: bench_mark_list(10000, MOVE_LST))
    print("list exe time : {}".format(t.timeit(number=100)))
    MOVE_DIC = {"top": 1, "bottom": 2, "left": 3, "right": 4}
    t = Timer(lambda: bench_mark_dico(10000, MOVE_DIC))
    print("dico exe time : {}".format(t.timeit(number=100)))
    t = Timer(lambda: bench_mark_list_2(10000))
    print("list affect new var exe time : {}".format(t.timeit(number=100)))
    t = Timer(lambda: bench_mark_list_3(10000))
    print("list iter on config exe time : {}".format(t.timeit(number=100)))
