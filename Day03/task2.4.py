p = " abcdefghij "
print (p [:: -2][:5][::-1][3:])

# The result will be i because [::-2] turn upside down and
# delete one caracter of two.
# [:5] take all caracters between index 0 and 5
# [::-1] turn upside down again
# [3:] take all caracters between index 3 and the end