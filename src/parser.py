from src import config
import fileinput


def parser(input_file):
    print("input : ", input_file)
    int_lst = []
    for line in fileinput.input(input_file):
        line = line.split('#')
        line[0] = line[0].strip()
        if line[0].isdigit() and config.TAQUIN_SIZE == 0 and len(line[0]):
            config.TAQUIN_SIZE = int(line[0])
        else:
            tab = line[0].split(' ')
            x = 0
            while x in range(len(tab)): #problemme avec for in range et .pop
                if not tab[x]:
                    tab.pop(x)
                elif not tab[x].isdigit():
                    print("Puzzle Error: '{}' is not a number".format(tab[x]))
                    exit(1)
                elif int(tab[x]) > int(config.TAQUIN_SIZE)**2 - 1:
                    print("Puzzle Error: '{}' > number max".format(tab[x]))
                    exit(1)
                else:
                    x += 1
            int_lst += [int(x) for x in tab]
            tab = set(tab)
            if len(tab) != int(config.TAQUIN_SIZE):
                print("Puzzle Error: Ne correspond pas a la taille du jeu ou doublon: ", end='')
                print(len(tab), end='=')
                print(config.TAQUIN_SIZE)
                print(tab)
                exit(1)
        pass
    return int_lst
