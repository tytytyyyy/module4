a = 'abcdfaa'

# общее колтчество символов
#def strcounter(s):
#    counter = 0
#    for sym in s:
#        counter += 1
#    print(counter)
#strcounter(a)

# квадратичная сложность
#def strcounter(s):
#    for sym in s:
 #       counter = 0
  #      for sub_sym in s:
   #         if sym == sub_sym:
    #            counter +=1
     #   print(sym, counter)

#strcounter(a)

# сложность M*N
#def strcounter(s):
#    print(set(s))
#    for sym in set(s):
#        counter = 0
#        for sub_sym in s:
#            if sym == sub_sym:
#                counter +=1
#        print(sym, counter)

#strcounter(a)


#линейная сложность
def strcounter(s):
    sym_counter = {}
    for sym in s:
        if sym not in sym_counter:
            sym_counter[sym] = 1
        else:
            sym_counter[sym] += 1
    
    for sym, count in sym_counter.items():
        print(sym, count)

strcounter(a)