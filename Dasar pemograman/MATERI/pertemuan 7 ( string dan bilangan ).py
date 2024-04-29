import decimal
import fractions

# mengakses nilai string
var1 = 'hello python!'
var2 = "i love python"
print('var1[0]', var1[0])
#output= h
print('var2[2:6]', var2[2:6])
# output= love

# mengupdate string
var1 = 'hello python!'
var2 = var1[:6]
print('string update:-', var1[:6] + 'World' + var1[5:12])
print("var1*3 = ", var1[0:6]*3)
# output= hello word

# karakter escape
# menggunakan kutip tiga
print('''He said,"what's there?''')
# output= He said,"what's there?"

# menggunakan karakter escape untuk tanda kutip tunggal
print('He said,"What\'s there?"')
# output= He said,"what's there?"

# menggunakan karakter escpae untuk tanda kutip ganda
print("He said,\"What's there?\"")
# output= He said,"what's there?"


# meratakan nilai string
print("|{:<10}|{:^10}|{:>10}|".format('beras', 'gula', 'garam'))
# output= |beras     |   gula   |     garam|

nama = 'budi'
print("nama saya %s" % (nama))
# output= nama saya budi

x = 12.3456789
print('Nilai x = %3.2f' % (x))
# output= Nilai x = 12.35
print('Nilai x = %3.4f' % (x))
# output= Nilai x = 12.3457

# mengecilkan Capslock
print('Universits Nusa Mandiri'.lower())
# output= universits nusa mandiri

# membesar semua nilai
print('Universits Nusa Mandiri'.upper())
# output= UNIVERSITS NUSA MANDIRI

print("i love programming in python".split())
#output= ['i', 'love', 'programming', 'in', 'python']

print('-'.join(['i', 'love', 'you']))
#output= i-love-you

print("Belajar JAVA di unm".replace('JAVA', 'Python'))
# output= Belajar Python di unm

# python decimal
print(0.1)
# output = 0.1
print(decimal.Decimal(0.1))
# output = 0.1000000000000000055511151231257827021181583404541015625

# Bilangan pecahan
print(fractions.Fraction(1.5))
# output = 3/2
print(fractions.Fraction(1.3))
# output = 1/3
