#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 04.py

import sys

def q01():
	str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	str = str.split()

	dict = {}
	single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

	for element in str:
		if str.index(element) + 1 in single:
			dict[element[:1]] = str.index(element) + 1
		else:
			dict[element[:2]] = str.index(element) + 1

	for k, v in sorted(dict.items(), key=lambda x:x[1]):
		print (k, v)

	str2 = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
	 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	words_list = str2.split()

	dict2 = {}
	single2 = [0, 4, 5, 6, 7, 8, 14, 15, 18]

	for i in range(len(words_list2)):
		clen = 1 if i in single else 2
		dict[words_list[i][:clen]] = i + 1

	# for k, v in sorted(dict.items(), key=lambda x: x[1]):
	#     print(k, v)


def q05():
	#05. n-gram
	#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
	#この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
	original = "I am an NLPer"

	print(n_gram(original, 3))
	print(n_gram(original.split(), 3))

def q06():
	#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
	seq1= "paraparaparadise"
	seq2 ="paragraph"
	x = set(n_gram(seq1, 2))
	y = set(n_gram(seq2, 2))

	print x & y
	print y & x
	print x | y
	print x.intersection(y)
	print "se" in x

def n_gram(seq, n):
	ret = []
	for i in range(0, len(seq)-n+1): 
		ret.append(seq[i:i+n])

	return ret

def q07():
	#07. テンプレートによる文生成
	#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
	print(func(12, "気温", 22.4)	)

def func(x, y, z):
	return "x時のyはz"

def main():
	q07()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
