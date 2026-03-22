def biseccion(funcion,a,b,tolerancia,max_iteraciones):
    if (funcion(a)*funcion(b)>0):
        print("No hay raices en el intervalo")
        return None
    else:
        i=0
        while((b-a)/2 > tolerancia and (i< max_iteraciones)):
            m=(b+a)/2
            if abs(funcion(m))<1e-12:
                return m
            elif (funcion(a)*funcion(m)<0):
                b=m
            else:
                a=m
            i+=1
    return (a+b)/2

def simpson13(funcion,a,b,n):
    h=(b-a)/(2*n)
    integral=funcion(a)+funcion(b)
    suma_impar=0.0
    suma_par=0.0
    for i in range(1,n+1):
        suma_impar +=funcion(a+(2*i-1)*h)
    for i in range(1,n):
        suma_par +=funcion(a+2*i*h)
    integral=(h/3)*(integral+4*suma_impar+2*suma_par)
    return integral

def busqueda_binaria(x,A):
    r=len(A)-1
    p=0
    while(p<=r):
        m=(p+r)//2
        if(A[m]==x):
            return m
        elif(A[m]<x):
            p=m+1
        else:
            r=m-1
    return r

def error_porcentual(A,B,funcion):
    s=len(B)
    error=[]
    for i in range(0,s):
        e=100*abs(funcion(A[i])-B[i])/abs(funcion(A[i])+1e-12)
        error.append(e)
    return error




