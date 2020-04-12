# !/usr/bin/env python3
# Zwtfy.py
# 转换文件为Base 64编码再转换为二进制格式再转换为类字符串格式再保存
# (或逆操作)
# 一种新式混淆方案?
# Lib版本
# lwd-temp@Github.com 使用GNU Affero通用公共许可证开源发布
import base64

def bencode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
def bdecode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
# Not mine.But it just works.Isn't it wired?
# Source:https://blog.csdn.net/ztf312/article/details/88703456

def encode(instr):
    fi=instr
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
    return zwtstr


def decode(instr):
    zwtstr=instr
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
    return fi
