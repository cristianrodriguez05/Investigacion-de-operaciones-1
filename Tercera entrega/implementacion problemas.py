def mochila(W, wt, val, n):
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   #Tabla de abajo hacia arriba
   for i in range(n + 1):
      for w in range(W + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif wt[i-1] <= w:
            K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
    # Devuelve el valor máximo de beneficio que puede almacenar la bolsa
   return K[n][W]


#val = [100,60,70,15,9]
#wt = [42,23,21,15,7]
#W = 60
#n = len(val)
#print(mochila(W, wt, val, n))

val = [11000000,9000000,1000000]
wt = [10000000,6000000,4000000]
W = 10000000
n = len(val)
print(mochila(W, wt, val, n))

val = [15,8,15,17,7]
wt = [5000000,2520000,3600000,4700000,1200000]
W = 5000000
n = len(val)
print(mochila(W, wt, val, n))
