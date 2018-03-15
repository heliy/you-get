try:
    # py 3.4
    from html import unescape as unescape_html
except ImportError:
    import re
    from html.entities import entitydefs

    def unescape_html(string):
        '''HTML entity decode'''
        string = re.sub(r'&#[^;]+;', _sharp2uni, string)
        string = re.sub(r'&[^;]+;', lambda m: entitydefs[m.group(0)[1:-1]], string)
        return string

    def _sharp2uni(m):
        '''&#...; ==> unicode'''
        s = m.group(0)[2:].rstrip(';；')
        if s.startswith('x'):
            return chr(int('0'+s, 16))
        else:
            return chr(int(s))

from .fs import legitimize

def filter_filename(string):
    return "".join(s for s in string if s.isalpha() or s.isdigit() or s in [' ', "."])

def get_filename(htmlstring):
    return filter_filename(unescape_html(htmlstring))

def parameterize(string):
    return "'%s'" % string.replace("'", r"'\''")
