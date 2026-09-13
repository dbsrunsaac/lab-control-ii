% función de transferencia
num = [100];
den = [1 8 19 12];
H = tf(num, den);
disp(H);
bode(H);