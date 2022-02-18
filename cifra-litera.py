list1={'0':'zero','1':'unu','2':'doi','3':'trei', '4':'patru','5':'cinci','6':'sase','7':'sapte','8':'opt','9':'noua',
    '11':'unsprezece','12':'doisprezece','13':'treisprezece','14':'paisprezece',
    '15':'cincisprezece','16':'saisprezece','17':'saptesprezece','18':'optsprezece','19':'nouasprezece'}
def intstr(x):
    str1=''
    xv=x-int(x)
    xv=round(xv,2)
    x=int(x)
    x1=x//1000                 
    x2=(x%1000)//100
    if x!=10000 and x!=0:
        if x1!=0:
            if x1==1:
                str1+='o mie '
            elif x1==2:
                str1+="doua mii "
            else:
                str1+=(list1[str(x1)]+' '+'mii ')
        if x2!=0:
            if x2==1:
                str1+='o suta '
            elif x2==2:
                str1+="doua sute "
            else:
                str1+=(list1[str(x2)]+' '+'sute ')
        if (x%100 not in range(11,20)) and (x%100 not in range(0,10)) :
            x3=(x%100)//10
            x4=x%10
            if x4==0:
                if x3==1:
                    str1+='zece '
                elif x3==2:
                    str1+="douazeci "
                elif x3==6:
                    str1+="saizeci "
                else:
                    str1+=(list1[str(x3)]+'zeci ')
            else:
                if x3==2:
                    str1+='douazeci si'+' '+list1[str(x4)]
                elif x3==6:
                    str1+='saizeci si'+' '+list1[str(x4)]
                else:
                    str1+=list1[str(x3)]+'zeci'+' '+'si'+' '+list1[str(x4)]
        else:
            x34=x%100
            if x34!=0:
                str1+=list1[str(x34)]
    else:
        if x==10000:
            str1='zece mii'
        elif x==0:
            str1='zero'
    if xv!=0:
        xv=int(xv*100)
        str1+=' virgula '
        if xv>9:
            if (xv not in range(11,20)) and (xv not in range(0,10)) :
                xv3=xv//10
                xv4=xv%10
                if xv4==0:
                    if xv3==1:
                        str1+='zece '
                    elif xv3==2:
                        str1+="douazeci "
                    elif xv3==6:
                        str1+="saizeci "
                    else:
                        str1+=(list1[str(xv3)]+'zeci ')
                else:
                    if xv3==2:
                        str1+='douazeci si'+' '+list1[str(xv4)]
                    elif xv3==6:
                        str1+='saizeci si'+' '+list1[str(xv4)]
                    else:
                        str1+=list1[str(xv3)]+'zeci'+' '+'si'+' '+list1[str(xv4)]
            else:
                str1+=list1[str(xv)]
        elif xv<=9:
            str1+='zero '
            str1+=list1[str(xv)]

    return str1
print('Daca doresti sa transformi doar un numar scrie 0, doresti sa le vezi pe toate scrie 1')
y=int(input('::'))
if y==0:
    print(intstr(float(input('Numarul ce doresti sa-l transformezi: '))))
if y==1:
    print('Va trebui sa astepti un pic...')
    with open('desktop/output.txt','a') as f:
        f.write('zero'+'\n')
        for i in range(0,10000):
            for j in range(99):
                i+=0.01
                f.write(intstr(i)+'\n')
        f.write('zece mii'+'\n')
    print('''Verifica pe desktop fisierul textual "output", 52.9 MB))
    Te sfatui sa deschizi in VisualStudio
    ''')


