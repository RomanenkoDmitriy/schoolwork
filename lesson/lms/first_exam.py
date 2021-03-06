import json

EXAM = []

QUESTION = {
    'question': 'What is Python?',
    'answers': ['Programming language', 'Snake', "I don't know"],
    'correct_answer': '1'
}



def load_json(file_path='data/exam.json'):
    with open(file_path, 'r') as file:
        EXAM.extend(json.load(file))

def test():
    load_json()
    point = 0
    for qest in EXAM:
        answ = None
        print(qest['question'])

        for answer in qest['answers']:
            print(answer)
        answ = sorted(list(input('Your reply:  ')))
        if len(qest['correct_answer']) > 1:
            if answ == (qest['correct_answer']):
                point += qest['point']
        else:
            if answ == (qest['correct_answer']):
                point += qest['point']
                print(point)

    return point


point = test()

print(f'---------------------- {point}')