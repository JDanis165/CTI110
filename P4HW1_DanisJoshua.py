# CTI-110
# P4HW1 - Score List
# Joshua Danis
# 11/14/22

# Have user input scores
# Collect entered scores, determine validity
# Add scores to a list 
# Determine lowest score
# Drop lowest score 
# Calculate average
# Print Lowest score, Modified list, Scores Average and Grade


num_scores=int(input('How many scores do you want to enter? '))
print()
i = 1
tot_score=[]


while i<=num_scores:
    print('Enter score {}: '.format(i), end= '')
    score = float(input())
    
    if score<0 or score>100:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')

    else:
        tot_score.append(score)
        i+=1 

low_score = min(tot_score)
tot_score.remove(low_score)
score_avg=sum(tot_score)/len(tot_score)

if score_avg>=90:
    grade = 'A'

elif score_avg>=80:
    grade = 'B'

elif score_avg>=70:
    grade = 'C'

elif score_avg>=60:
    grade = 'D'

else:
    grade = 'F'

print()
print()

print('--------------Results-----------')
print('Lowest Score  :',low_score)
print('Modified List :',tot_score)
print("Scores Average: %.2f"%score_avg)
print('Grade         :',grade)
print('-----------------------------------')