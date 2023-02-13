def read_answer():
    N = int(input()) #number of line of student's answers
    answers = []
    for k in range(N): #loop N times
        sid,ans = input().split() #input student id and ans
        answers.append([sid,ans])
    return answers #return list of lists of student id and answers

def marking(answer,solution):
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]: #if character of answer is the same as solution, count score
            score += 1
    return score

def grading(score):
    g = [[80,"A"],[70,"B"],[60,"C"],[50,"D"]]
    for a,b in g:
        if score >= a:
            return b
    return "F"

def scoring(answers,solution):
    scores=[]
    for sid,ans in answers:
        score = marking(ans,solution)/len(solution) * 100 #convert to percent
        grade = grading(score) #get grade letter
        scores.append([sid,score,grade]) #append list of student id, score, grade into list
    return scores

def report(scores):
    for sid,sc,grade in scores:
        print(sid,sc,grade)

def sort(scores):
    x = []
    for sid,score,grade in scores:
        x.append([score,sid,grade]) #append to new list, reorder so that we use score to sort
    x.sort(reverse=True) #reverse so that the score is in decending order (A->F)
    for i in range(len(x)):
        scores[i] = [x[i][1],x[i][0],x[i][2]] #rearrange the score list

solution = input()
answers = read_answer()
scores = scoring(answers,solution)
sort(scores)
report(scores)