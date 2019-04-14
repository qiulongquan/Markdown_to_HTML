import sys
import os
import argparse
from chardet.universaldetector import UniversalDetector

#  python test1.py  d:\1.txt -e utf8 -o d:\
#  filePaths= d:\1.txt
#  -e : utf8
#  -o : d:\

parser = argparse.ArgumentParser(description = '这个是测试args参数调用的例子')

parser.add_argument('filePaths', nargs = '+',
                   help = '检测或转换的文件路径')

parser.add_argument('-e', '--encoding', nargs = '?', const = 'UTF-8',
                   help = '''
目标编码。支持的编码有：
ASCII, (Default) UTF-8 (with or without a BOM), UTF-16 (with a BOM),
UTF-32 (with a BOM), Big5, GB2312/GB18030, EUC-TW, HZ-GB-2312, ISO-2022-CN, EUC-JP, SHIFT_JIS, ISO-2022-JP,
ISO-2022-KR, KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251, ISO-8859-2, windows-1250, EUC-KR,
ISO-8859-5, windows-1251, ISO-8859-1, windows-1252, ISO-8859-7, windows-1253, ISO-8859-8, windows-1255, TIS-620
''')

parser.add_argument('-o', '--output',
                   help = '输出目录')

args = parser.parse_args()
print(args)
print("args.filePaths = ", args.filePaths)
print("args.encoding = ", args.encoding)
print("args.output = ", args.output)