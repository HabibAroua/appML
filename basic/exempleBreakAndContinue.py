tab = [1,2,3,4,5,-1,6,7,8,9,10]
for i in range(0,len(tab)):
    if tab[i]%2 == 0 and tab[i]>=0:
        print(tab[i])
    elif tab[i]%2 != 0 and tab[i]>=0:
        continue
    elif(tab[i]<0):
        print('negatif value')
        break