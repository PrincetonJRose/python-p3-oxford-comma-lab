import ipdb

def oxford_comma(items):
    # ipdb.set_trace()
    if len( items ) <= 1:
        return ''.join( items )
    elif len( items ) == 2:
        return ' and '.join( items )
    else:
        joined = ', '.join( items[ 0:-1 ] )
        add_and = ', and ' + items[-1]
        return joined + add_and

