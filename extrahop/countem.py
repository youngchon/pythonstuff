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

    with open(file, 'r') as file:
        for line in file:
            toks = line.split()
            if toks != []:
                if multiline == False:
                    #grab first token
                    cur = toks[0]
                    print(len(cur))
                    if len(cur) >= 2:
                        if cur[0] != '/' and cur[1] != '/':
                            numlines += 1 
                        elif cur[0] =='/' and cur[1] == '*': # how to deal with the end of this
                            #check to see if the last char is terminted with a /
                            multiline = True
                            if cur[-1] == '/':
                                if cur[-2] == '*':
                                    multiline = False
                    ## now lets check to see if anywhere inbetween some one decided
                    ## to start a code block
                    for token in toks[1:]: #dont recount hte first one
                    	if len(token) >= 2:
                    		if token[0] == '/' and token[1] == '*':
                    			multiline = True
                else:
                    #multilined grab last token
                    cur = toks[-1]
                    if cur[-1] == '/' and cur[-2] == '*':
                        multiline = False
        print ("number of lines: " + str(numlines))

if __name__ == '__main__':
    file = sys.argv[1]
    count(file)
             
        
        
        
