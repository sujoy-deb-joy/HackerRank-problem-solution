# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    text = ''
    for ele in s:
        if ele == ele.upper():
            text += ele.lower()
        else:
            text += ele.upper() 
    return text         
            