import argparse
import convert


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tools for books.')
    parser.add_argument('--completed', '-c', action='store', type=str)
    parser.add_argument('--overall', '-o', action='store', type=str)
    parser.add_argument('--pages', '-p', action='store', type=int)
    args = parser.parse_args()
    print(convert.run(args.completed, args.overall, args.pages))
