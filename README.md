```
argparse --- 命令行选项、参数和子命令解析器
https://docs.python.org/zh-cn/3/library/argparse.html

使用 python3 实现 Markdown to Html

    使用 os 模块进行路径相关的操作
    markdown模块的使用
    使用 BeautifulSoup 模块格式化 HTML
    命令行选项的实现

了解如何使用 markdown 模块来编译 markdown 输出 HTML，
熟悉了使用 os 模块进行路径相关的操作，
以及模仿系统命令实现了程序命令行选项。

通过下面的命令，执行mth程序  可以将test文档转化为html
python3 mth.py test.md test2.md -s ./GithubMarkdownCSS.css -o ./test
----------------------------------------------------------------------
if not destinationDirectory:
    # 未定义输出目录则将源文件目录(注意要转换为绝对路径)作为输出目录
    destinationDirectory = os.path.dirname(os.path.abspath(sourceFilePath))
if not outputFileName:
    # 未定义输出文件名则沿用输入文件名
    outputFileName = os.path.splitext(os.path.basename(sourceFilePath))[0] + '.html'

os.path.abspath() 将参数路径转为绝对路径并返回
os.path.dirname() 获得参数路径的目录部分并返回（如 "\home\a.txt" 为参数，返回 "\home"）
os.path.basename() 返回参数路径字符串中的完整文件名（文件名+后缀名）
os.path.splitext() 将参数转换为包含文件名和后缀名两个元素的元组并返回

文件的编码转换流程可以这样概括：
初始编码 → unicode → 目标编码

对于目录下面的文件的读取操作
包括指定目录path或者指定文件类型txt
https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

You can list all files in the current directory using:

import os
for filename in os.listdir(os.getcwd()):
   # do your stuff
Or you can list only some files, depending on the file pattern using the glob module:

import glob
for filename in glob.glob('*.txt'):
   # do your stuff
It doesn't have to be the current directory you can list them in any path you want:

path = '/some/path/to/file'

for filename in os.listdir(path):
    # do your stuff

for filename in glob.glob(os.path.join(path, '*.txt')):
    # do your stuff


hashlib --- 安全哈希与消息摘要    
https://docs.python.org/zh-cn/3/library/hashlib.html

```
