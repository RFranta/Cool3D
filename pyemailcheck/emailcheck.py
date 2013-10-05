# RFC822 Email Address Regex
# --------------------------
# 
# Originally written by Cal Henderson
# c.f. http://iamcal.com/publish/articles/php/parsing_email/
#
# Translated to Python by Tim Fletcher, with changes suggested by Dan Kubb.
#
# Licensed under a Creative Commons Attribution-ShareAlike 2.5 License
# http://creativecommons.org/licenses/by-sa/2.5/

import re

qtext = '[^\\x0d\\x22\\x5c\\x80-\\xff]'
dtext = '[^\\x0d\\x5b-\\x5d\\x80-\\xff]'
atom = '[^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+'
quoted_pair = '\\x5c[\\x00-\\x7f]'
domain_literal = "\\x5b(?:%s|%s)*\\x5d" % (dtext, quoted_pair)
quoted_string = "\\x22(?:%s|%s)*\\x22" % (qtext, quoted_pair)
domain_ref = atom
sub_domain = "(?:%s|%s)" % (domain_ref, domain_literal)
word = "(?:%s|%s)" % (atom, quoted_string)
domain = "%s(?:\\x2e%s)*" % (sub_domain, sub_domain)
local_part = "%s(?:\\x2e%s)*" % (word, word)
addr_spec = "%s\\x40%s" % (local_part, domain)

email_address = re.compile('\A%s\Z' % addr_spec)

# if __name__ == '__main__':
#   addresses = (
#     'cal@iamcalx.com',
#     'cal+henderson@iamcalx.com',
#     'cal henderson@iamcalx.com',
#     '"cal henderson"@iamcalx.com',
#     'cal@iamcalx',
#     'cal@iamcalx com',
#     'cal@hello world.com',
#     'cal@[hello world].com',
#     'abcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz'
#   )
#   for address in addresses:
#     print "%s : %s" % (repr(address), email_address.match(address))

# How this is used: 
def isValidEmailAddress(email):
    if email_address.match(email):
        return True
    else:
        return False
