import math as mt

def euler(a, b, U, F, n):
    h = (b-a)/n
    t = a
    W = U
    print(f"t0 = {t}, u1_0 = {U[0]:.6f}, u2_0 = {U[1]:.6f}, u3_0 = {U[2]:.6f}")

    for i in range(1, n+1):
        W0 = W
        for j, w in enumerate(W):
            W[j] = w + h*F[j](t, W0[0], W0[1], W0[2])
        t = a + i*h
        print(f"t{i} = {t:.2f}, u1_{i} = {W[0]:.6f}, u2_{i} = {W[1]:.6f}, u3_{i} = {W[2]:.6f}")
    return W

def RK2(a, b, U, F, n):
    h = (b-a)/n
    t = a
    W = U
    print(f"t0 = {t}, u1_0 = {U[0]:.6f}, u2_0 = {U[1]:.6f}, u3_0 = {U[2]:.6f}")

    for i in range(1, n+1):
        W0 = W
        K1 = []
        for j in range(len(W)):
            K1.append(h*F[j](t, W0[0], W0[1], W0[2]))

        K2 = []
        for j in range(len(W)):
            K2.append(h*F[j](t + h, W0[0] + K1[0], W0[1] + K1[1], W0[2] + K1[2]))
        
        for j,w in enumerate(W):
            W[j] = w + (1/2)*(K1[j]+K2[j])
        t = a + i*h
        print(f"t{i} = {t:.2f}, u1_{i} = {W[0]:.6f}, u2_{i} = {W[1]:.6f}, u3_{i} = {W[2]:.6f}")
    return W

def RK4(a, b, U, F, n):
    h = (b-a)/n
    t = a
    W = U
    print(f"t0 = {t}, u1_0 = {U[0]:.6f}, u2_0 = {U[1]:.6f}, u3_0 = {U[2]:.6f}")

    for i in range(1, n+1):
        W0 = W
        K1 = []
        for j in range(len(W)):
            K1.append(h*F[j](t, W0[0], W0[1], W0[2]))

        K2 = []
        for j in range(len(W)):
            K2.append(h*F[j](t + h/2, W0[0] + K1[0]/2, W0[1] + K1[1]/2, W0[2] + K1[2]/2))

        K3 = []
        for j in range(len(W)):
            K3.append(h*F[j](t + h/2, W0[0] + K2[0]/2, W0[1] + K2[1]/2, W0[2] + K2[2]/2))
        
        K4 = []
        for j in range(len(W)):
            K4.append(h*F[j](t + h, W0[0] + K3[0], W0[1] + K3[1], W0[2] + K3[2]))

        for j,w in enumerate(W):
            W[j] = w + (1/6)*(K1[j]+2*K2[j]+2*K3[j]+K4[j])
        t = a + i*h
        print(f"t{i} = {t:.2f}, u1_{i} = {W[0]:.6f}, u2_{i} = {W[1]:.6f}, u3_{i} = {W[2]:.6f}")
    return W

def f1(t, u1, u2, u3):
    return u2

def f2(t, u1, u2, u3):
    return -u1-2*mt.exp(t)+1

def f3(t, u1, u2, u3): # en caso de sistema con 2 ecuaciones return 0
    return -u1-mt.exp(t)+1

a,b,n = 0,2,5
U = [1, 0, 1]
F = [f1, f2, f3]

W = euler(a, b, U, F, n)