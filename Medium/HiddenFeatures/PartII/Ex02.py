import io

num: int = 50
string_ex = ""
for i in range(num):
    string_ex += str(i)

print(string_ex)


string_fx = io.StringIO()
for i in range(num):
    string_fx.write(str(i))

print(string_fx.getvalue())

#OUTPUT
#012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849
#012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849