# A program that can show list, highest score, lowest score, and calculate mean score.(list practice)

scores = []
while True:
    print('請輸入第'+ str(len(scores)+1) + '個分數(按Enter結束): ')
    inputScore = input()
    if inputScore == '':
        break
    try:
        intscore = int(inputScore)
        if 0 <= intscore <= 100:
            scores.append(intscore)
        else:
            print('請輸入0到100的整數!')
    except ValueError:
        print('請輸入整數!')

print('分數清單: ',  scores)
print('最高分: '+ str(max(scores)))
print('最低分: ' + str(min(scores)))
print('平均分數: '+ str(round(sum(scores)/len(scores), 1)))