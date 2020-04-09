# !/usr/bin/env python3
# Zwtfy.py
# 转换文件为Base 64编码再转换为二进制格式再转换为类字符串格式再保存
# (或逆操作)
# 一种新式混淆方案?
# lwd-temp@Github.com 使用GNU Affero通用公共许可证开源发布
import sys
import base64

def helptext():
    print("Zwtfy使用帮助")
    print("zwtfy.py [操作] [输入文件] [输出文件]")
    print("操作：encode或decode")
    print("输入文件和输出文件：文件名或完整路径")

def bencode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
def bdecode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
# Not mine.But it just works.Isn't it wired?
# Source:https://blog.csdn.net/ztf312/article/details/88703456

def encode(infi,outfi):
    print("Encoding...")
    with open(infi,"rb") as infile:
        fi=infile.read()
    fib64=str(base64.b64encode(fi),encoding='utf-8')
    bytestr=bencode(fib64)
    charno="init"
    zwtstr=""
    done=0
    for chars in bytestr:
        if charno=="init":
            charno="z"          
        if charno=="z" and done==0:
            if chars=="1":
                zwtstr=zwtstr+"Z"
                charno="w"
            if chars=="0":
                zwtstr=zwtstr+"z"
                charno="w"
            if chars==" ":
                zwtstr=zwtstr+" "
            done=1
        if charno=="w" and done==0:
            if chars=="1":
                zwtstr=zwtstr+"W"
                charno="t"
            if chars=="0":
                zwtstr=zwtstr+"w"
                charno="t"
            if chars==" ":
                zwtstr=zwtstr+" "
            done=1
        if charno=="t" and done==0:
            if chars=="1":
                zwtstr=zwtstr+"T"
                charno="z"
            if chars=="0":
                zwtstr=zwtstr+"t"
                charno="z"
            if chars==" ":
                zwtstr=zwtstr+" "
            done=1
        done=0
    with open(outfi,"w",encoding='utf-8') as outfile:
            outfile.write(zwtstr)


def decode(infi,outfi):
    print("Decoding...")
    with open(infi,"r") as infile:
        zwtstr=infile.read()
    bytestr=""
    for chars in zwtstr:
        if chars=="Z" or chars=="W" or chars=="T":
            bytestr=bytestr+"1"
        if chars=="z" or chars=="w" or chars=="t":
            bytestr=bytestr+"0"
        if chars==" ":
            bytestr=bytestr+" "
    fib64=bdecode(bytestr)
    fi=base64.b64decode(fib64)
    with open(outfi,"wb") as outfile:
        outfile.write(fi)


argvlen=len(sys.argv)

if int(argvlen)!=4:
    print("错误：参数错误")
    print()
    helptext()
    sys.exit()
method=sys.argv[1]
if method!="encode" and method!="decode":
    print("错误：操作类型选择错误")
    print()
    helptext()
    sys.exit()
if sys.argv[2]==sys.argv[3]:
    print("警告：输入输出文件相同，输出将覆写输入文件，继续操作？[y/N]")
    choice=input()
    if choice.lower()!="y":
        print("程序退出")
        sys.exit()
if method=="encode":
    encode(infi=sys.argv[2],outfi=sys.argv[3])
if method=="decode":
    decode(infi=sys.argv[2],outfi=sys.argv[3])