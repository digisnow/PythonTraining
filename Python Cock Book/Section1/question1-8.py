# existence check
aset = ['aaa', 'bbb', 'ccc']
seq = 'aaa'
def containsAny(seq, aset):
    for c in aset:
        if c in seq:
            return True
        return False

if containsAny(seq, aset) is True:
    print 'true'
elif containsAny(seq, aset) is False:
    print 'false'


