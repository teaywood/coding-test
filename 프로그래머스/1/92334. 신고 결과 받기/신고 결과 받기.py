def solution(id_list, report, k):
    reporter = {id_: 0 for id_ in id_list} # {신고자: 메일 받은 개수} 딕셔너리
    suspect = {id_: [] for id_ in id_list} # {피신고자 : [신고자 명단]} 딕셔너리
    
    for report_list in report:
        _reporter, _suspect = report_list.split()
        if _reporter not in suspect[_suspect]:
            suspect[_suspect].append(_reporter)
        
    for v in suspect.values():
        if len(v) >= k:
            for r in v:
                reporter[r] += 1
    return list(reporter.values())
