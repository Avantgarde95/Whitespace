# Loop 4 times
LSS L 
SS STSSL # x.

# Print '-' 3 times
LSS SL 
SS STTL # y.

LSS SSL 
SS STSTTSTL 
TLSS 
SS STL 
TSST # y -= 1.
SLS 
LTS SSSL # If y = 0.
LSL SSL 

# Print '*' 2 times
LSS SSSL 
SLL # Clear y.
SS STSL # z.

LSS SSSSL 
SS STSTSTSL 
TLSS 
SS STL 
TSST # z -= 1.
SLS 
LTS SSSSSL # If z = 0.
LSL SSSSL 

LSS SSSSSL 
SLL # Clear z.
SS STSTSL 
TLSS 
SS STL 
TSST # x -= 1.
SLS # If x = 0.
LTS SSSSSSL 
LSL SL 

LSS SSSSSSL 
LLL 