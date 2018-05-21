text="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
order=[1, 5, 6, 7, 8, 9, 15, 16, 19]

for num,elem in zip(range(len(text.split(' '))),text.split(' ')):
    if num+1 in order:print(elem[0])
    else:           print(elem[0:2])
