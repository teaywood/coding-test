import re

def solution(new_id):
    #1단계
    new_id = new_id.lower()
    
    #2단계
    new_id = ''.join(re.findall('[\da-z._-]', new_id))

    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    #4단계
    new_id = list(new_id)
    
    if new_id and new_id[0] == '.':
        del new_id[0]
    if new_id and new_id[-1] == '.':
        del new_id[-1]
    if not new_id:
        #5단계
        new_id = ['a']

    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            del new_id[-1]
    
    #7단계
    while len(new_id) <= 2:
        new_id.append(new_id[-1])
        
    return ''.join(new_id)