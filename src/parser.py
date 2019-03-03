import fileinput

from src import error
from src import config


def parse_file(file):
    int_lst = []
    for line in file:
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
                    raise error.ParsingError("'{}' is not a number".format(tab[x]))
                elif int(tab[x]) > int(config.TAQUIN_SIZE)**2 - 1:
                    raise error.ParsingError("'{}' > number max".format(tab[x]))
                else:
                    x += 1
            int_lst += [int(x) for x in tab]
            tab = set(tab)
            if len(tab) != int(config.TAQUIN_SIZE):
                raise error.ParsingError("Ne correspond pas a la taille du jeu ou doublon: {}={}"
                                         .format(len(tab), config.TAQUIN_SIZE))
        pass
    if len(int_lst) == 0:
        raise error.ParsingError("File is empty")
    return int_lst


def parser(input_file):
    with fileinput.input(input_file, openhook=fileinput.hook_encoded("utf-8")) as file:
        try:
            int_lst = parse_file(file)
        except UnicodeDecodeError:
            raise error.ParsingError("File contains non utf-8 characters..")
        #except Exception as err:
        #    raise error.ParsingError("Unknown parsing error ({})".format(err))
        #except BaseException as err:
        #    raise error.ParsingError("Program interrupted by system ({})".format(err))
    return int_lst
