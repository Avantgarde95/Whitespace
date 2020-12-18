"""Convert human-readable code to Whitespace code.

Author: Hunmin Park (Avantgarde95)

Language: Supports the subset of Whitespace 0.3.
- https://ko.wikipedia.org/wiki/화이트스페이스_(프로그래밍_언어)
- https://en.wikipedia.org/wiki/Whitespace_(programming_language)

Usage: python Convert.py inputFileName inputPath outputPath
- For example, if the input's path is "original/Test.txt",
  run "python Convert.py Test.txt original converted",
  then the 'encoded' code will be generated at "converted/Test.es",
  and the runnable code will be generated at "converted/Test.ws".
- You can run the generated file (*.ws) at the following links:
  https://naokikp.github.io/wsi/whitespace.html
  https://vii5ard.github.io/whitespace/

Grammar
- # Blahblah...: Comment.
- push arg: Push arg onto the stack. (arg: int or char)
- dup: Duplicate the top item on the stack.
- dupn arg: Duplicate the [arg]th item on the stack. (arg: int)
- swap: Swap the top two items on the stack.
- pop: Discard the top item on the stack.
- op+: Pop the top two items a, b and push a + b.
- op-: Pop the top two items a, b and push a - b.
- op*: Pop the top two items a, b and push a * b.
- op/: Pop the top two items a, b and push a / b.
- label arg: Create the [arg]th label. (arg: int)
- jump arg: Jump to the [arg]th label. (arg: int)
- jumpz arg: Jump to the [arg]th label if the top of the stack is zero. (arg: int)
- jumpn arg: Jump to the [arg]th label if the top of the stack is negative. (arg: int)
- exit: End the program.
- print: Pop the top character and print it.
- printn: Pop the top number and print it.
"""

import os
import sys


def convertLabel(labelIndex: int):
    return 'S' * labelIndex + 'L'


def convertNumber(number: int):
    sign = 'S' if number > 0 else 'T'
    binary = bin(abs(number))[2:]

    return sign + ''.join('T' if c == '1' else 'S' for c in binary) + 'L'


def convertChar(char: str):
    return convertNumber(ord(char))


escapeMap = {
    's': ' ',
    't': '\t',
    'n': '\n'
}


def convertLine(line: str):
    if '#' in line:
        commentIndex = line.index('#')
        code, comment = line[:commentIndex], line[commentIndex:]
    else:
        code, comment = line, ''

    tokens = code.split()

    if not tokens:
        return comment

    command = tokens[0]

    if command == 'push':
        arg = tokens[1]

        if arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()):
            return f'SS {convertNumber(int(arg))} {comment}'
        elif len(arg) == 1:
            return f'SS {convertChar(arg)} {comment}'
        elif len(arg) == 2 and arg[0] == '\\':
            return f'SS {convertChar(escapeMap[arg[1]])} {comment}'
    elif command == 'dup':
        return f'SLS {comment}'
    elif command == 'dupn':
        arg = tokens[1]

        if arg.isdigit():
            return f'STS {convertNumber(int(arg))} {comment}'
    elif command == 'swap':
        return f'SLT {comment}'
    elif command == 'pop':
        return f'SLL {comment}'
    elif command == 'op+':
        return f'TSSS {comment}'
    elif command == 'op-':
        return f'TSST {comment}'
    elif command == 'op*':
        return f'TSSL {comment}'
    elif command == 'op/':
        return f'TSTS {comment}'
    elif command == 'label':
        arg = tokens[1]

        if arg.isdigit():
            return f'LSS {convertLabel(int(arg))} {comment}'
    elif command == 'jump':
        arg = tokens[1]

        if arg.isdigit():
            return f'LSL {convertLabel(int(arg))} {comment}'
    elif command == 'jumpz':
        arg = tokens[1]

        if arg.isdigit():
            return f'LTS {convertLabel(int(arg))} {comment}'
    elif command == 'jumpn':
        arg = tokens[1]

        if arg.isdigit():
            return f'LTT {convertLabel(int(arg))} {comment}'
    elif command == 'exit':
        return f'LLL {comment}'
    elif command == 'print':
        return f'TLSS {comment}'
    elif command == 'printn':
        return f'TLST {comment}'

    raise SyntaxError('Wrong syntax! (Line: %s)' % line)


def encodeLine(line: str):
    commands = []

    for c in line:
        if c == '#':
            break
        elif c == 'S':
            commands.append(' ')
        elif c == 'T':
            commands.append('\t')
        elif c == 'L':
            commands.append('\n')

    return ''.join(commands)


def main():
    if len(sys.argv) < 4:
        print('Usage: %s inputFileName inputPath outputPath' % sys.argv[0])
        return

    inputFileName = sys.argv[1]
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]

    inputFilePureName, inputFileExtension = os.path.splitext(inputFileName)

    with open(inputPath + '/' + inputFileName, 'r') as p:
        lines = p.readlines()

    convertedLines = [convertLine(line.strip()) for line in lines]
    encodedLines = [encodeLine(line) for line in convertedLines if line != '']

    with open(outputPath + '/' + inputFilePureName + '.es', 'w') as p:
        p.write('\n'.join(convertedLines))

    with open(outputPath + '/' + inputFilePureName + '.ws', 'w') as p:
        p.write(''.join(encodedLines))

    print('Done!')


main()
