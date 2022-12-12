'''
The idea of this algorithm is to create a new way of visualize folder in a os as a graph.
'''

import os


class Dir:
    def __init__(self, name, path, is_file, level):
        self.name = name
        self.path = path + '/' + name
        self.is_file = is_file
        self.level = level
        self.sons = []


def get_os():

    root = 'C:/Users/alexa'
    directories = [Dir('Documents', root, False, 0)]
    directories_names = ['Documents']

    stack = [d for d in directories]

    while len(stack) > 0:
        dir = stack[0]
        stack.pop(0)

        if os.access(dir.path, os.R_OK) and (dir.is_file == False):
            sons = []
            try:
                sons = [Dir(x, dir.path, os.path.isfile(dir.path + '/' + x), dir.level+1) for x in os.listdir(dir.path)]
                dir.sons = sons
            except PermissionError as e:
                continue
                print('PERMISSION ERROR', end=':')
                print(e)
            except OSError as e:
                continue
                print('OS ERROR', end=':')
                print(e)
            finally:
                # Few folders to ignore
                forbiden = ['venv', 'Lib', 'pyfhn', '.git', '.idea', 'django', 'node_modules', '[COVID-19]']
                for s in sons:
                    if s.name not in forbiden:
                        stack.append(s)
                        directories_names.append(s.name)
                        directories.append(s)

    target = directories[directories_names.index('Seconde')]
    for i in range(len(target.sons)):
        d = target.sons[i]
        print(d.name, d.level)


get_os()
