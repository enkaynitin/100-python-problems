word_freq = {}
s = raw_input().split(' ')
for word in s:
    word_freq[word] = word_freq.get(word,0)+1

words = word_freq.keys()
words.sort()

for w in words:
    print "%s:%d" %(w,word_freq[w])
