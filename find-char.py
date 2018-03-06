word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for text in range(len(word_list)):
    if char in word_list[text]:
        new_list.append(word_list[text])
print(new_list)

       