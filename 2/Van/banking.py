def change(N,A):
    #A = list(map(int, input().split()))
    #N = int(input())
    try:
        INF = 10**10
        F = [INF] * (N+1)
        F[0] = 0
        Prev = [0] * (N+1)
        for k in range(1, N+1):
            for i in range(len(A)):
                if k-A[i] >= 0 and F[k-A[i]] < F[k]:
                    F[k] = F[k-A[i]]
                    Prev[k]=A[i]
            F[k] +=1
        if F[N] >= INF:
            return("impossible")
        else:
            amount = ''
            while N>0:
                amount += str(Prev[N]) + ' '
                N-= Prev[N]
            return (amount).strip()
    except ValueError:
        print('Это не число. Выходим.')
    except TypeError:
        print("Не соответсвие с типом")

        
   
#change()