# Degrees of polynomials in post-quantum cryptography. Breaking baby Kyber 

As a cybersecurity and cryptography professional wishes to demonstrate the dangers of incorrectly implementing post quantum cryptographic algorithms. 

In this challenge, you will act as a spy who wants to obtain a specific random symmetric cryptographic key ($m$ in our example) exchanged between two users. The cryptographic key is protected with a “kind of” Kyber algorithm (post quantum algorithm) that does not follow the correct implementation specification.

You have been able to intercept the key exchange transcript than contains the encryption of the random symmetric session key.

That is the information that you have:

- __The parameters of the bad implementaion of Kyber are small ($K=2$, $N=16$, $q=251$)__. All the vectors and matrices are defined over polynomials modulo $x^{N}+1$ mod $q$. Please, review the basic concepts of this algorithm to better understand this challenge.

- __The Public key $(A,t)$ is known__. Note that during the key generation, $A$ was a matrix of random polynomials and $t=As+e$ where $e$ is a column vector of "small" polynomials, with coefficients in $\{-1,0,1\}$.

$$ A = \begin{bmatrix} 
A1 & A2 \\ 
A3 & A4 \end{bmatrix} $$

$A1 = 195x^{15}+229x^{14}+25x^{13}+88x^{12}+5x^{11}+209x^{10}+91x^{9}+209x^{8}+189x^{7}+122x^{6}+34x^{5}+39x^{4}+194x^{3}+3x^{2}+198x+180$
$A2 = 187x^{15}+83x^{14}+58x^{13}+30x^{12}+77x^{11}+138x^{10}+71x^{9}+212x^{8}+11x^{7}+73x^{6}+24x^{5}+222x^{4}+8x^{3}+105x^{2}+246x+229$
$A3 = 84x^{15}+95x^{14}+224x^{13}+177x^{12}+43x^{11}+155x^{10}+63x^{9}+246x^{8}+232x^{7}+177x^{6}+53x^{5}+243x^{4}+41x^{3}+111x^{2}+73x+234$
$A4 = 3x^{15}+85x^{14}+143x^{13}+51x^{12}+177x^{11}+116x^{10}+247x^{9}+222x^{8}+181x^{7}+33x^{6}+78x^{5}+196x^{4}+188x^{3}+216x^{2}+170x+64$

$$ t = \begin{bmatrix} 
t1 \\ 
t2 \end{bmatrix} $$

$t1=109x^{15}+188x^{14}+107x^{13}+177x^{12}+240x^{11}+205x^{10}+22x^{9}+134x^{8}+174x^{7}+243x^{6}+36x^{5}+215x^{4}+114x^{3}+210x^{2}+145x+9$
$t2=198x^{15}+159x^{14}+120x^{13}+184x^{12}+217x^{11}+224x^{10}+96x^{9}+124x^{8}+30x^{7}+155x^{6}+247x^{5}+34x^{4}+224x^{3}+154x^{2}+240x+235$


-  __You also know the encryption $(u,v)$ of the symmetric session key $m$__ (this key has binary coefficients in $\{0,1\}$ in our challenge). We recall that the ciphertext has been generated as follow: 

$u=(A^{T}r+e1)$ mod $x^{N}+1$ mod $q$

$v= (t^{T}r+e2+\frac{q-1}{2}m)$ mod $x^{N}+1$ mod $q$

  where $e1, e2, r$ are polynomials (or vectors of polynomials) with “small” random coefficients in $\{-1,0,1\}$.

$$ u = \begin{bmatrix} 
u1 \\ 
u2 \end{bmatrix}$$

$u1=49x^{15}+118x^{14}+243x^{13}+19x^{12}+124x^{11}+37x^{10}+121x^{9}+30x^{8}+86x^{7}+34x^{6}+218x^{5}+5x^{4}+198x^{3}+248x^{2}+227x+49$
$u2=41x^{15}+70x^{14}+147x^{13}+28x^{12}+218x^{11}+224x^{10}+82x^{9}+128x^{8}+141x^{7}+85x^{6}+141x^{5}+70x^{4}+199x^{3}+242x^{2}+190x+112$

$v=78x^{15} +206 x^{14} +72 x^{13} +81 x^{12} +165 x^{11} +80 x^{10} +86 x^{9} +16 x^{8} +34 x^{7} +96 x^{6} +189 x^{5} +232 x^{4} +121 x^{3} +77 x^{2} +156 x +29$


- __The secret key $s$ is a column vector of polynomials with “small” random coefficients with dimensions 2x1__. The coefficients of  $s1$ and $s2$  are not communicated, but as an attacker, you know that their coefficients were drawn from ${0,1}$
  
$$ s = \begin{bmatrix} 
s1 \\ 
s2 \end{bmatrix}$$

$s1=cx^{15}+cx^{14}+cx^{13}+cx^{12}+cx^{11}+cx^{10}+cx^{9}+cx^{8}+cx^{7}+cx^{6}+cx^{5}+cx^{4}+cx^{3}+cx^{2}+cx+c$
$s2=cx^{15}+cx^{14}+cx^{13}+cx^{12}+cx^{11}+cx^{10}+cx^{9}+cx^{8}+cx^{7}+cx^{6}+cx^{5}+cx^{4}+cx^{3}+cx^{2}+cx+c$

## Challenge objective

The challenge is to obtain the random session key $m$ from the ciphertext $(u,v)$ and the public key $(A,t)$ above. 

To evaluate your solution you need to send us to __ctf-rwpqc2024@sandboxaq.com__ the answer with the subject "Challenge1" in the following format: flag="m", where m is the concatenation of the 16 coefficients of m. For example, the flag="0000000000010011" would correspond to the binary polynomial $m=x^3+x+1$. 

__Hint__: In general, to obtain $m$ your need to calculate m_n= v - $s^{T}u$ mod $x^{N}+1$ mod q. 

m_n will be ($m$) with a very high probability. Check how to “convert” m_n into $m$. For each coefficients, replace any values in [-q/4,q/4] mod q by 0, and all the other by 1.

## References
https://pq-crystals.org/kyber/index.shtml






