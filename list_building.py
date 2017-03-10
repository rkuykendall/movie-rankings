def build_graph(options, lists):
    graph = {key: set(options) for key in options}

    for movies in lists:
        for movie in movies:
            graph[movie] -= set(movies)

    return graph


def health(graph):
    total = float(len(graph))
    avg = sum([len(graph[k]) for k in graph]) / total
    health = ((total - avg) / total) * 100

    return health


def build_list(graph, rankings, length=10, ):
    rankings_dict = {r['player']: r['score'] for r in rankings}
    graph_len = len(graph)

    seed = max(graph, key=lambda k: len(graph[k]))
    movies = set([seed])
    del graph[seed]

    def max_key(k):
        overlap = len(graph[k] & movies)
        k_mismatches = len(graph[k])
        return overlap * graph_len + k_mismatches

    for i in range(length-1):
        key = max(graph, key=max_key)
        movies.add(key)
        del graph[key]

    return sorted(list(movies), key=lambda m: rankings_dict[m], reverse=True)
