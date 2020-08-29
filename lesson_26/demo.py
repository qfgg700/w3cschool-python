#统计一个字符在文本当中的次数；
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
#用input()输入函数，输入一个正确的文本路径；
filename = input("输入一个文件名: ")
with open(filename) as f:
  text = f.read()
#对每个字符进行占比计算；
for char in "abcdefghijklmnopqrstuvwxyz":  #a =2
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))