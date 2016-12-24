import pickle
import sys

file_name = sys.argv[1]
out_put_name = sys.argv[2]
f = open(file_name, "r")

lines = [line for line in f.readlines()]
print len(lines)

def decode_line(line):
    try:
        rt = line.decode("gbk")
        return rt
    except:
        print line
        return None

lines = map(decode_line, lines)
lines = filter(lambda x:x is not None, lines)
print len(lines)

pickle.dump(lines, open(out_put_name, "wb"))

f.close()
