#
def unexpand(astring, tablen=8):
    import re
    #
    pieces = re.split(r'( +)', astring.expandtabs(tablen))
    #
    lensofar = 0
    for i, piece in enumerate(pieces):
        thislen = len(piece)
        lensofar += thislen
        if piece.isspace():
            numblanks = lensofar % tablen
            numtabs = (thislen-numblanks+tablen-1)/tablen
            pieces[i] = '\t'*numtabs + ' '*numblanks
        return ''.join(pieces)
