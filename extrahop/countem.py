# foo.c
# $ countem.py foo.c
# 173
#   /* this is a
#      multiline
#      comment
#   */
#
#   // this is a comment too
#       // as is this indented one
#   /* this is a single line */
#
#   /* and this one
#    * for some reason
#    * is different
#    */


#!/usr/bin/env python

import sys

def count(file):
    numlines = 0
    multiline = False

    with open("foo.c", 'r') as file:
        for line in file:
            toks = line.split()
            if toks != []:
                if multiline == False:
                    #grab first token
                    cur = toks[0]
                    if len(cur) > 2:
                        if cur[0] != '/' and cur[1] != '/':
                            numlines += 1 
                        elif cur[0] =='/' and cur[1] == '*': # how to deal with the end of this
                            #check to see if the last char is terminted with a /
                            multiline = True
                            if cur[-1] == '/':
                                if cur[-2] == '*':
                                    multiline = False
                    ##
                else:
                    #multilined grab last token
                    cur = toks[-1]
                    if cur[-1] == '/' and cur[-2] == '*':
                        multiline = False
        print ("number of lines: " + str(numlines))

if __name__ == '__main__':
    file = sys.argv[1]
    count(file)
             
        
        
        
