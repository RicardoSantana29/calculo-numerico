// Programa par triangularizar superiormente una matriz real cuadrada
function [B] = triangsup(A)
    [n,m] = size(A);
    if(m~=n)
    error('La matriz no es cuadrada');
    return;
    end
    B = zeros(n,n);   
    B = A;
    
    for j = 1:n-1
    [ma,k]= max(abs(B(j:n,j)))
    k = k+j-1
    faux = B(j,:);
    B(j,:) = B(k,:);
    B(k,:) = faux;
        for i = j+1:n
        mu = B(i,j)/B(j,j)
        B(i,:) = B(i,:) - mu*B(j,:)
        end
    end
csvWrite(B,'Resultado.csv')
endfunction 
