
def printImg(img):
    for i in img:
        print(*i)
image=[
    [0,0,0],
    [0,1,0],
    [0,0,0]
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
printImg(Convolution(paddingMirror()))