a = ' '

b = '*'

a = a + b

a *= 5 ** 0 * 5      # ' * * * * *'

 

a = ' '

b = '$ '

a = a + b

a += '* ' * 3        # ' $ * * * '

 

a = '''Hello

(^_^)

'''

b = a * 2

a += b               # 'Hello\n\n(^_^)\n\nHello\n\n(^_^)\n\nHello\n\n(^_^)\n\n'