""" raise  ('test')

try:
    ...
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise """

class ParsingException (Exception):
    pass


raise ParsingException ('so ein macher dieser Exception')