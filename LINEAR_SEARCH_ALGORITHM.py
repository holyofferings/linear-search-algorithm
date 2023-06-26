from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
test = []
def locate_cards(cards,query):
    position = 0
    print("crards: ", cards)
    print("query: ", query)
    while position<len(cards):
        print("postion: ", position)
        if cards[position]==query:
            return position
        position+=1
    return -1

test.append(
    {
        'input':{'cards': [13,12,11,7,4,3,2,1,0],
                 'query': 1

                },
        'output':7
        }
)

test.append(
    {
        'input':{'cards': [13,12,11,7,4,3,2,1,0],
                 'query': 13

                },
        'output':0
        }
)
test.append(
    {
        'input':{'cards': [13,12,11,7,4,3,2,1,0],
                 'query': 0

                },
        'output':8
        }
)

test.append(
    {
        'input':{'cards': [13],
                 'query': 13

                },
        'output':0
        }
)
test.append(
    {
        'input':{'cards': [],
                 'query': 4

                },
        'output':-1
        }
)
test.append(
    {
        'input':{'cards': [13,12,11,7,4,3,2,1,0],
                 'query': 5

                },
        'output':-1
        }
)
test.append(
    {
        'input':{'cards': [13,13,12,12,11,11,7,4,3,2,1,0],
                 'query': 7

                },
        'output':6
        }
)
test.append(
    {
        'input':{'cards': [13,12,11,7,7,7,7,4,3,2,1,0],
                 'query': 7

                },
        'output':3
        }
)
evaluate_test_case(locate_cards,test[6])
evaluate_test_cases(locate_cards,test)
