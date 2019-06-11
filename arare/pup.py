import sys
from pegpy.tpeg import grammar, generate, STDLOG

# 文法を直したいときは
# pegpy/grammar/puppy.tpeg を編集する

peg = grammar('puppy.tpeg')
parser = generate(peg)

source = '''
print("こんにちは、のぶちゃん")
'''


# print(t.tag)
# for label, subtree in t:
#   print(label, subtree)


def Source(t):
    s = ''
    for lb, st in t:
        s += conv(st)
    return s


# def IfStmt(t):
#   s = 'if ('
#   s += conv(s.cond)
#   s += ') {'
#   pass
#   return s


func = globals()


def conv(t):
    if t.tag in func:
        return func[t.tag](t)
    else:
        return str(t)


def transpile(s):
    t = parser(s)
    STDLOG.dump(t)  # debug
    return conv(t)

# main スクリプト


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            source = f.read()
    code = transpile(source)
    print(code)