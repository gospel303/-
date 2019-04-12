
# -*- coding: utf-8 -*-
import os
import sys
import fnmatch
import win32com.client

PATH = "D:\\xingzheng"
PATH_DATA = "D:\\xingzheng"


# 主要执行函数
def main():
    wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
    try:
        for root, dirs, files in os.walk(PATH_DATA):
            for _dir in dirs:
                pass
            for _file in files:
                if not fnmatch.fnmatch(_file, '*.doc'):
                    continue
                word_file = os.path.join(root, _file)
                wordapp.Documents.Open(word_file)
                docastxt = word_file[:-3] + 'txt'
                wordapp.ActiveDocument.SaveAs(docastxt, FileFormat=win32com.client.constants.wdFormatText)
                wordapp.ActiveDocument.Close()
    finally:
        wordapp.Quit()
    print(
    "well done!")


if __name__ == '__main__':
    main()
