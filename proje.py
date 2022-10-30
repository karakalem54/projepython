arr = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,6,7]

def duzlestir(arr):
    liste = []
    for item in arr:
        if(type(item) is list):
            for item2 in item:
                if(type(item2) is list):
                    for item3 in item2:
                       if(type(item3) is list):
                            pass
                       else:
                            liste.append(item3)
                else:
                    liste.append(item2)
        else:
            liste.append(item)
    return liste

print(duzlestir(arr))
