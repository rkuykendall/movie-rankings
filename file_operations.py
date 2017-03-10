import os


def load_options(fname='options.txt'):
    with open(fname) as f:
        lines = f.readlines()

    return [d.strip() for d in lines]


def write_readme(top, ftext='readme_text.md'):
    with open(ftext) as f:
        text = f.read()

    with open('readme.md', 'w') as f:
        f.write(text)
        f.write('\n')

        for i, r in enumerate(top):
            f.write('{}. {}\n'.format(i + 1, r['player']))


def load_lists(folder='rankings'):
    lists = []

    for fname in os.listdir(folder):
        if fname[-4:] == '.txt':
            with open(os.path.join(folder, fname)) as f:
                lists.append([l.strip() for l in f.readlines()])

    return lists
