from book import convert, cli


if __name__ == '__main__':
    parse = cli.parser()
    args = parse.parse_args()
    print(convert.run(args.completed, args.overall, args.pages))
