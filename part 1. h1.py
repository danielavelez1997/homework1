def tripple(a):
    x = a*3
    return x
tripple(5)

def substract(b,c):
    y=c-b
    return y 
substract(5,8)    

def dictionary_maker(tup1,dic):
    dic=dict(tup1)
    return dic

tuple_values = [('foo', 1), ('bar', 3)]
empty_dictionary = {}  

dictionary_maker(tuple_values,empty_dictionary)
