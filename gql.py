# -*- coding: utf-8 -*-
"""
    pygments.lexers.graphql
    ~~~~~~~~~~~~~~~~~~~~
    Lexers for GraphQL formats.
    :copyright: Copyright 2017 by Martin ZlÃ¡mal.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ['GraphqlLexer']


class GraphqlLexer(RegexLexer):
    """
    Lexer for GraphQL.
    """

    name = 'GraphQL'
    aliases = ['graphql', 'gql']
    filenames = ['*.graphql', '*.gql']
    mimetypes = ['application/graphql']

    tokens = {
        'root': [
            (r'#.*', Comment.Singline),
            (r'\.{3}\w+', Operator),
            (ur'"[\u0009\u000A\u000D\u0020-\uFFFF]*"', String.Double),
            (r'(-?0|-?[1-9][0-9]*)(\.[0-9]+[eE][+-]?[0-9]+|\.[0-9]+|[eE][+-]?[0-9]+)', Number.Float),
            (r'(-?0|-?[1-9][0-9]*)', Number.Integer),
            (r'\$+[_A-Za-z][_0-9A-Za-z]*', Name.Variable),
            (r'[_A-Za-z][_0-9A-Za-z]+\s?:', Text),
            (r'(type|query|interface|fragment|mutation|extend|input|implements|directive|@[a-z]+|on\s+\w+|true|false|null)\b', Keyword.Type),
            (r'(\:\s*\w+)\b', Keyword.Type),
            (r'[!$():=@\[\]{|}]+?', Punctuation),
            (r'[_A-Za-z][_0-9A-Za-z]*', Keyword),
            (r'(\s|,)', Text),
        ]
}
