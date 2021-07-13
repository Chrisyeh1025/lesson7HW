num = int(input('有多少同學?'))
num = int(num)
score_list = []
x = []
def chris(num,score):
    max_num = max(score)
    min_num = min(score)
    sum_num = sum(score)
    avg_num = sum_num/num
    return max_num,min_num,sum_num,avg_num
for i in range(num):
    score = int(input('分數?'))
    score_list.append(int(score))
   
print(score_list)
x = chris(num,score_list)
print('最高分是:', x[0],'最低分是:',x[1],'總分是:',x[2],'平均分數是:',x[3])
