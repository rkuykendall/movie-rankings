import sys

from ranking import ranking, lists_to_matches
from file_operations import load_options, load_lists
from list_building import build_graph, build_list, health


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    lists = load_lists()

    if (arg == 'new'):
        options = load_options()
        graph = build_graph(options, lists)
        movies = build_list(graph)

        for movie in movies:
            print('{}'.format(movie))
    elif (arg == 'best'):
        matches = lists_to_matches(lists)
        rankings = ranking(matches)
        options = [m['player'] for m in rankings[:100]]

        lists = [list(set(l) & set(options)) for l in lists]
        lists = [l for l in lists if len(l) > 1]

        graph = build_graph(options, lists)
        movies = build_list(graph)

        for movie in movies:
            print('{}'.format(movie))
    elif (arg == 'health'):
        options = load_options()
        graph = build_graph(options, lists)
        print(health(graph))
    else:
        matches = lists_to_matches(lists)
        rankings = ranking(matches)

        for i, r in enumerate(rankings):
            print('#{} - {} (~{})'.format(i + 1, r['player'], r['score']))


if __name__ == "__main__":
    main()
