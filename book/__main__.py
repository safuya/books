from book import convert, cli, logging


if __name__ == '__main__':
    parse = cli.parser()
    args = parse.parse_args()
    logging.log.notice(f'Running the program with args: {args}.')
    print(convert.run(args.completed, args.overall, args.pages))
