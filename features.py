import csv

topics = ['Atheism', 'CC', 'FM', 'HC', 'Legalization']

for topic in topics:
    print 'Topic : {}'.format(topic)
    f1 = open(topic + '.txt', 'r')
    f2 = open(topic + '_train.csv', 'r')
    f3 = open(topic + '_train_feat.csv', 'w')
    f3w = csv.writer(f3)
    words = set()
    for line in f1:
        words.add(line.strip())
    f1.close()
    print 'Words : {}'.format(len(words))
    f3w.writerow(list(words))
    for tweet in f2:
        row = []
        for word in words:
            if word in tweet:
                row.append(1)
            else:
                row.append(0)
        f3w.writerow(row)
    f2.close()
    f3.close()