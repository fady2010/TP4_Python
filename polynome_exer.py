from sympy import symbols, Eq

Px=[1,-4,2,-3,45,-5,0]
x=2
def afficher(Px):
    for i in range(len(Px)):
        if(i==len(Px)-1):
            if(Px[len(Px)-i-1]>=0):
                print(str("+ ")+str(Px[len(Px)-i-1]),end=" " )
            else:
                
                print(str(Px[len(Px)-i-1]),end=" " )
            
        elif(Px[len(Px)-i-1]>=0 and i>0):
            print(str("+")+str(Px[len(Px)-i-1])+"X^"+ str(len(Px)-i-1),end=" " )
        elif(Px[len(Px)-i-1]<0 and i>0):
            print(str(Px[len(Px)-i-1])+"X^"+ str(len(Px)-i-1),end=" " )
        else:
            print(str(Px[len(Px)-i-1])+"X^"+ str(len(Px)-i-1),end=" " )
def get_valeur(Px,x):
    
    s=x
    som=0
    for i in range(len(Px)):
        for j in range(len(Px)-i-1-1):
            s*=s
        if(i!=len(Px)-1):
            som=som+Px[len(Px)-i-1]*s
    
        else:
            som=som+Px[len(Px)-i-1]
        s=x
    print("\n"+"P("+str(x)+")="+str(som))
    return som
    
def devriver(Px):
    for i in range(len(Px)):
        if(i<len(Px)-1):
            Px[i]=Px[i+1]*(i+1)
            
    Px=Px[:-1]
    return Px  
    
afficher(Px)
get_valeur(Px,x) 
print("calcul de la derivé")
afficher(devriver(Px)) 








    
