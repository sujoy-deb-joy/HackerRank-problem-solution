results = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    results.append([name, score])
    scores.append(score)

runner_up = sorted(list(set(scores)))[1]

final_names = [student[0] for student in results if student[1] == runner_up]

for name in sorted(final_names):
    print(name)