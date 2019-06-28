from book import cli


def test_parser_description():
    parser = cli.parser()
    assert parser.description == 'Tools for books.'
