#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Small python script to brute force an Oracle 10 hash
'''

__author__ = "C4rt"
__date__ = "11/05/2013"
__version__ = "1.0"
__maintainer__ = "C4rt"
__email__ = "eric.c4rtman@gmail.com"
__status__ = "Production"

try:
    from passlib.hash import oracle10
    import optparse
    from threading import Thread
except ImportError, err:
    raise
    print >>sys.stderr, "[X] Unable to import : %s\n" % err
    sys.exit(1)


def testPass(hashPass, user, word):
    try:
            if oracle10.verify(word, hashPass, user):
                print '[+] Found Password: ' + word + '\n'
                exit(0)
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog "+\
        "-f <hashPass> -u <user> -d <dictionary>")
    parser.add_option('-f', dest='cname', type='string',\
        help='specify hashed password')
    parser.add_option('-u', dest='uname', type='string',\
        help='specify user name')
    parser.add_option('-d', dest='dname', type='string',\
        help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.cname == None) | (options.uname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else :
        cname = options.cname
        uname = options.uname
        dname = options.dname
    hashPass = cname
    user = uname
    dico = open(dname)
    for line in dico.readlines():
        word = line.strip('\n')
        t = Thread(target=testPass, args=(hashPass, user, word))
        t.start()

if __name__ == '__main__':
    try:
        main()
    except:
        print "\n\n\n\n", traceback.format_exc()
