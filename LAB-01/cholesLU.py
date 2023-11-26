from PALU import factorizar_PALU as fP

def fact_choleski_P(A):
    if not np.allclose(A, A.T):
        return 'La matriz A no es simétrica'

    auto_valores = np.linalg.eigvalsh(A)
    if np.any(auto_valores <= 0):
        return 'La matriz A no es definida positiva'

    P, L, U = fP(A)

    D = np.sqrt(np.diag(np.diagonal(U)))

    L_chlk = np.matmul(L,D)

    return L_chlk, L_chlk.T