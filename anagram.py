#coding:utf-8

import sys
dictionary = open ("dictionary","r") #ファイルを開く
arvs = sys.argv #引数を代入

def SortDictionary (dictionaryname):
    lines = dictionary.readlines () #行ごとにすべて読み込んでリストデータにする
    for line in lines:
        sortedline = sorted (line)
    sorteddictionary = sorted (sortedline)
    return (sorteddictionary)

def SortArgument (argument):
    sortedargument = sorted (args)#argsをそーとしたリストを返す
    return (sortedargument)
    
def Compare (dictionaryname, argument):
    return (goodstring)

    
while True:
    #辞書をそーとして、ソートされた辞書を返す
    newdictionary =  SortDictionary (dictionary)
    #引数をソートしてソートされた引数を返す
    newargument = Sortargument (args)
    #辞書と比較してあればそれを返す
    answer = Compare (newdictionary, newargument)
    #あったものを出力する
    print ("%s\n" %answer)

dictionary.close()#ファイルを閉じる
