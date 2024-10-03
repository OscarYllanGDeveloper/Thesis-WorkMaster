def main():
    height= int(input("Enter Tree height: "))
    
    lineas=0
    
    while lineas<height:
        espacios= height -lineas - 1
        
        arbolito= " "* espacios +"*"*(2*lineas+1)
        print(arbolito)
        lineas+=1

if __name__ == '__main__':
    main()