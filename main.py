input_data = open('input.txt', 'r') 
data = input_data.read()
s = str(data)
k = 0
N = 0
for i in range(0, len(s)):

    if s[i] == '0':
        k= k + 1
        if k > N:
            N +=1
    else:
        k = 0
output_data = open('output.txt','w')
output_data.write(str(N))
input_data.close()
output_data.close()