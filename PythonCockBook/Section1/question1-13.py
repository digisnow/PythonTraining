# access to a part of string
import struct
#
baseformat = "5s 3x 8s 8s"
numremine = len(theline) - struct.calcsize(baseformat)
format = "%s %ds " % (baseformat, numremine)
1, s1, s2, t = struct.unpack(format, theline)
