
def printImg(img):
    for i in img:
        for j in i:
            if (j<10):
                print(" ",end="")
            print(j,end=" ")
        print()
        # print(*i)

image=[
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]
]


kernel =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

convolKernal = list(reversed([list(reversed(x)) for x in kernel]))

yPadding=len(kernel)//2

xPadding=len(kernel[0])//2

def paddingWith0():
    padding_with_0 = []
    for i in range(len(image)+2*yPadding):
        if i==0 or i == (len(image)+2*yPadding)-1:
            padding_with_0.append([0]*(len(image[0])+2*xPadding))
        else:
            padding_with_0.append([0]*xPadding + image[i-1] +[0]*xPadding)
    return padding_with_0


def paddingExtended():
    padding_extend=[]
    for i in range(len(image)+2*yPadding):
        if i==0:
            padding_extend.append([image[0][0]]*xPadding + image[0] + [image[0][-1]]*xPadding)
        elif i == (len(image)+2*yPadding)-1:
            padding_extend.append([image[-1][0]]*xPadding + image[-1]+ [image[-1][-1]]*xPadding)
        else:
            padding_extend.append([image[i-1][0]]*xPadding + image[i-1]+ [image[i-1][-1]]*xPadding)
    return padding_extend


def paddingMirror():
    paddingMirror=[]
    for i in range(yPadding):
        arr=[]
        for j in range(xPadding):
            arr.append(image[yPadding-i][xPadding-j])
        arr.extend(image[yPadding-i])
        for j in range(xPadding):
            arr.append(image[yPadding-i][len(image[0])-xPadding+j-1])
        paddingMirror.append(arr)
    for i in range(len(image)):
        arr=[]
        for j in range(xPadding):
            arr.append(image[i][xPadding-j])
        arr.extend(image[i])
        for j in range(xPadding):
            arr.append(image[i][len(image[0])-xPadding+j-1])
        paddingMirror.append(arr)
    for i in range(yPadding):
        arr=[]
        for j in range(xPadding):
            arr.append(image[len(image)-2-i][len(image[0])-2-j])
        arr.extend(image[yPadding-i])
        for j in range(xPadding):
            arr.append(image[len(image)-2-i][len(image[0])-j-2])
        paddingMirror.append(arr)
    return paddingMirror
    

def wrapping():
    wrapping=[]
    for i in range(yPadding):
        arr=[]
        for j in range(xPadding):
            arr.append(image[len(image)+i-yPadding][len(image[0])-xPadding+j])
        arr.extend(image[len(image)+i-yPadding])
        for j in range(xPadding):
            arr.append(image[len(image)+i-yPadding][j])
        wrapping.append(arr)
    for i in range(len(image)):
        arr=[]
        for j in range(xPadding):
            arr.append(image[i][len(image[0])-xPadding+j])
        arr.extend(image[i])
        for j in range(xPadding):
            arr.append(image[i][j])
        wrapping.append(arr)
    for i in range(yPadding):
        arr=[]
        for j in range(xPadding):
            arr.append(image[i][len(image[0])-xPadding+j])
        arr.extend(image[i])
        for j in range(xPadding):
            arr.append(image[i][j])
        wrapping.append(arr)
    return wrapping


def Correlation(img):
    new_img=[[]]
    for i in range(len(image)):
        for j in range(len(image[0])):
            val=0
            for ii in range(-yPadding,yPadding+1):
                for jj in range(-xPadding,xPadding+1):
                    print( img[i+yPadding+ii][j+xPadding+jj] ,"*",kernel[yPadding+ii][xPadding+jj], end=" + ")
                    val+=img[i+yPadding+ii][j+xPadding+jj]*kernel[yPadding+ii][xPadding+jj]
            print("=",val)
            print("-"*100)
            new_img[-1].append(val)
        new_img.append([])
        
    return new_img


def Convolution(img):
    new_img=[[]]
    printImg(img)
    for i in range(len(image)):
        for j in range(len(image[0])):
            val=0
            for ii in range(-yPadding,yPadding+1):
                for jj in range(-xPadding,xPadding+1):
                    print( img[i+yPadding+ii][j+xPadding+jj] ,"*",convolKernal[yPadding+ii][xPadding+jj], end=" + ")
                    val+=img[i+yPadding+ii][j+xPadding+jj]*convolKernal[yPadding+ii][xPadding+jj]
            print("=",val)
            print("-"*100)
            new_img[-1].append(val)
        new_img.append([])
        
    return new_img


t = ''
while(t!='q'):
    valid = True
    padding = input('''
  Padding techniques:
  0. Padding With 0
  1. Replicate Padding
  2. Reflect / Mirror Padding
  3. Wrapping
  Enter Choice : ''')


    padded_img = []

    if(padding == '0'):
        padded_img=paddingWith0()
    elif(padding == '1'):
        padded_img=paddingExtended()
    elif(padding == '2'):
        padded_img=paddingMirror()
    elif(padding == '3'):
        padded_img=wrapping()
    else:
        print("\nInvalid padding input!")
        valid = False

    print("Padded Image :\n")
    printImg(padded_img)

    if(valid):
        process = input('''
  Kernel types:
  1. Convolution
  2. Correlation
  Enter Choice : ''')
        
        if(process == '1'):
            printImg(Convolution(padded_img))
        elif(process == '2'):
            printImg(Correlation(padded_img))
        else:
            print("\nInvalid Process selected!")
    
    t = input("Enter q to quit or press ENTER to continue : ")
