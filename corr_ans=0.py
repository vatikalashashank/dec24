corr_ans=0
wrong_ans=0
print('1.what is the capital of india ?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='delhi':
    corr_ans+=1
    print('correct ans')
else:
     wrong_ans+=1
     print('wrong ans')
corr_ans=0
wrong_ans=0
print('2.what the national game?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='hockey':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
corr_ans=0
wrong_ans=0
print('3.what the national fruit?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='mango':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
corr_ans=0
wrong_ans=0
print('4.what the national tree?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='banyan tree':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((corr_ans/(corr_ans+wrong_ans))*100))
