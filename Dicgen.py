# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:35:21 2024

@author: Alex
"""

import itertools as its
import sys
import os


def main(keyWordsPath=None, fileName="password_list", start=1, end=10):
    if keyWordsPath is None:
        words = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345679-=\[]';,./*+~!@#$%^&*()_+{}|:\"<>?"
        print(f'[+]Default words: {words}')
    else:
        try:
            with open(keyWordsPath, 'r') as f:
                words = f.read()
            print(f'[+]加載{keyWordsPath}成功！')
        except Exception as e:
            print(f'[!]加載{keyWordsPath}失败！，原因：{e}')
            exit(0)
    dic = open(f'{fileName}.txt', 'w+')
    print(f'[+]Output File Name: {fileName}')
    for i in range(start, end):
        r = its.product(words, repeat=i)
        for w in r:
            dic.write("".join(w) + "\n")
        print("\r[-]寫入中{:.2f}%".format(i / end * 100), end="", flush=True)
    print("\r[-]寫入中{:.2f}%".format(100))
    dic.close()
    print("\r[+]寫入完成！")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("[*]用法:python dicgen.py YourKeyWordsFile.txt OutputDistFileName WordStartLength WordEndLength\n[*]範例:python dicgen.py sample.txt password_list 1 10")
        sw = input('[!]是否使用預設值產生字典？（y/n）')
        if sw == 'y' or sw == "Y":
            main()
        else:
            os._exit(0)
    else:
        start = int(sys.argv[3])
        end = int(sys.argv[4]) + 1
        main(sys.argv[1], sys.argv[2], start, end)
