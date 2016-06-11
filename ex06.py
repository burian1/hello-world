# Exercise the sixth: Strings and Text

x = "There are %d types of girls." % 2
redhead = "redhead"
non_redhead = "not redhead"
y = "%ss and those who are %s." % (redhead, non_redhead)

print x
print y

print "I said: %r." % x
print "I also have been quoted as having said %r" % y

#why do the single quotes appear in the result when run?