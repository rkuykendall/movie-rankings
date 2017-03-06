import os


def load_options(fname='options.txt'):
    with open(fname) as f:
        lines = f.readlines()

    return [d.strip() for d in lines]


def load_lists(folder='rankings'):
    lists = []

    for fname in os.listdir(folder):
        if fname[-4:] == '.txt':
            with open(os.path.join(folder, fname)) as f:
                lists.append([l.strip() for l in f.readlines()])

    return lists
