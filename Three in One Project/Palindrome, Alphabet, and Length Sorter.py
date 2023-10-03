def palindrome(str_lst1):
    palindromes = []
    for i in range(len(str_lst1)):
        list2 = []
        word = ''
        for e in range(len(str_lst1[i])):
            word += str_lst1[i][len(str_lst1[i]) - 1 - e]
        list2.append(word)
        if str_lst1[i] == list2[0]:
            palindromes.append(str_lst1[i])       
    return palindromes

def length(str_lst2):
    len_lst = []
    for i in range(len(str_lst2)):
        if i == 0:
            len_lst.append(str_lst2[0])           
        elif len(str_lst2[i]) > len(len_lst[len(len_lst) - 1]):
            for e in range(len(len_lst)):
                if len(str_lst2[i]) < len(len_lst[len(len_lst) - 1 - e]) and str_lst2[i] not in len_lst:
                    len_lst.insert(len(len_lst) - e, str_lst2[i])                   
            if len(str_lst2[i]) >= len(len_lst[0]): 
                    len_lst.insert(0, str_lst2[i])
        else:
            len_lst.append(str_lst2[i])
    return len_lst

def alphabet(str_lst3):
    alp_lst = []
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        for e in range(len(str_lst3)):          
            if str_lst3[e][0] == alp[i]:             
                alp_lst.append(str_lst3[e])
    return alp_lst

def final(initial_lst):
    print('These are all of the palindromes in the list: %s, this is the list organized by length: %s, and this is the list in alphabetical order: %s.' % (palindrome(initial_lst), length(initial_lst), alphabet(initial_lst)))


final(['peep','mindless','noon','load','nip','brush','sudden','dry','father','lol','astonish','understand','boorish','well-off','racecar','worried','insurance'])
