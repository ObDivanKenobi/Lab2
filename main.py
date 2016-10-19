#Пробелы и знаки препинания стоят в неправильном порядке.
f = open('input.txt', 'r', encoding='cp1251')
s = f.read()
text = list(s)
f.close()
i = 1;
marks = (".", ",", "!", "?")
while i < len(text):
    if text[i] in marks and text[i-1] == ' ':
        text[i], text[i-1] = text[i-1], text[i]
    i+=1

i = len(text) - 1;
while i >= 0 and text[i] == ' ': text.pop(i); i -= 1
i = 0
while i < len(text) and text[i] == ' ': text.pop(i)
while i < len(text):
    if text[i] == ' ' and text[i-1] == ' ': text.pop(i)
    else: i+=1

f = open('output.txt', 'w')
out = ''.join(text)
f.write(out)
f.close()