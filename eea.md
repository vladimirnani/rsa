The recursive definition of the greatest common divisor (GCD) is:

$$
\gcd(a, b) = 
\begin{cases}
b & \text{if } a = 0 \\
\gcd(b \bmod a, a) & \text{otherwise}
\end{cases}
$$
