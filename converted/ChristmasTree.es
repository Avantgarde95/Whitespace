# var n = 5, x = n.
LSS L 
SS STSTL 
SLS 

# do { y = x - 1; ...; print('\n'); x -= 1 } while (x != 0).
LSS SL 
SLS 
SS STL 
TSST # y = x - 1 => Stack = [n, x, y].

# while (y != 0) { print(' '); y -= 1 }.
LSS SSL 
SLS 
LTS SSSL # Break if (y = 0).
SS STSSSSSL 
TLSS 
SS STL 
TSST # y -= 1
LSL SSL 

# var z = (n - x) * 2 + 1.
LSS SSSL 
SLL # Clear y => Stack = [n, x].
STS STL 
STS STL 
TSST # z = n - x => Stack = [n, x, z].
SS STSL 
TSSL # z *= 2.
SS STL 
TSSS # z += 1.

# while (z != 0) { print('*'); z -= 1 }.
LSS SSSSL 
SLS 
LTS SSSSSL # Break if z = 0.
SS STSTSTSL 
TLSS 
SS STL 
TSST # z -= 1.
LSL SSSSL 

LSS SSSSSL 
SLL # Clear z => Stack = [n, x].
SS STSTSL 
TLSS 
SS STL 
TSST # x -= 1.
SLS 
LTS SSSSSSL # Break if x = 0.
LSL SL 

# var s = n - 1.
LSS SSSSSSL 
SLL # Clear x => Stack = [n].
SLS 
SS STL 
TSST # s = n - 1 => Stack = [n, s].

# while (s != 0) { print(' '); s -= 1 }.
LSS SSSSSSSL 
SLS 
LTS SSSSSSSSL # Break if (s = 0).
SS STSSSSSL 
TLSS 
SS STL 
TSST # s -= 1.
LSL SSSSSSSL 

# print('|\n'); var t = n - 2.
LSS SSSSSSSSL 
SLL # Clear s => Stack = [n].
SS STTTTTSSL 
TLSS 
SS STSTSL 
TLSS 
SLS 
SS STSL 
TSST # t = n - 2 => Stack = [n, t].

# while (t != 0) { print(' '); t -= 1 }.
LSS SSSSSSSSSL 
SLS 
LTS SSSSSSSSSSL # Break if (t = 0).
SS STSSSSSL 
TLSS 
SS STL 
TSST # t -= 1.
LSL SSSSSSSSSL 

# print('===\n').
LSS SSSSSSSSSSL 
SS STTTTSTL 
SLS 
SLS 
TLSS 
TLSS 
TLSS 
SS STSTSL 
TLSS 
LLL 