f= open('test.txt', 'r')
def lifePath(file):
    x=0
    list3=[]
    for i in file:
        if len(i) <= 2:
            numberOfDates = i
            #print(numberOfDates)
        else:
            addedArray = []
            list2 = []
            date1 = i.replace('\n', '')
            date = date1.split('/')
            #print(date)
            for i in date:
                num1 = int(i[0])
                num2 = int(i[1])

                answer = num1+num2
                addedArray.append(str(answer))
            #print(addedArray)
            for i in addedArray:
                if len(i) > 1:
                    num1= int(i[0])
                    num2= int(i[1])
                    answer= num1 + num2
                    list2.append(answer)
                else:
                    list2.append(int(i))
            #print(list2)
            for x in range(len(list2)):
                if x == 0:
                    num1 = list2[x]
                    num2 = list2[x+1]
                    num3 = list2[x+2]

                    path = num1+num2+num3
                    if len(str(path)) > 1:
            
                        Path = str(path)

                        num1 = int(Path[0])
                        num2 = int(Path[1])

                        path = num1 + num2
                        #print(path)
                        
                else: 
                    break
            list3.append(str(path) + ' ' + date1 )


            
    return list3
                
test = lifePath(f)
for i in test:
    print(i)

