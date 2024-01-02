import argparse

def create_argparser():
    """Creates a parser for CLI commands."""
    parser = argparse.ArgumentParser(
        description='Simple calculator')
    subparsers = parser.add_subparsers(title='Available commands', help='description')

    build_parser = subparsers.add_parser('build')
    query_parser = subparsers.add_parser('query')

    build_parser.add_argument('--dataset', dest='dataset_path',
                              default='./tests/wikipedia_sample.txt',
                              help='path to dataset to build Inverted Index')
    build_parser.add_argument('--index', dest='index_path',
                              default='./index.json',
                              help='path for Inverted Index dump')
    build_parser.set_defaults(func=build_command)

    query_parser.add_argument('--query_file', dest='query_path',
                              default='./tests/01.in',
                              help='query file with collection of queries to '
                                   'run against Inverted Index')
    query_parser.add_argument('--index', dest='index_path',
                              default='./index.json',
                              help='path to load Inverted Index from')
    query_parser.set_defaults(func=query_command)
    return parser


def main():
    parser = create_argparser()
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)