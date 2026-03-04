class

white = "\033[48;2;254;254;254m  \033[0m"
black = "\033[48;2;0;0;0m  \033[0m"

print(white * 21)
for i in range(10):
    line_str = white
    bottom_str = white
    for j in range(10):
        
        line_str += black
        line_str += white
        
        bottom_str += white
        bottom_str += black
    print(line_str)
    print(bottom_str)
# print(white * 22)




