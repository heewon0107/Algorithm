def solution(genres, plays):
    result = []
    album = {}
    for i in range(len(genres)):
        # 앨범에 장르가 없으면 장르 추가
        if not album.get(genres[i]):
            album[genres[i]] = {
                "play_num" : 0,
                "play_list" : []               
                               }
        
        # 장르에 노래 횟수 넣기
        album[genres[i]]["play_list"].append((plays[i], i))
        album[genres[i]]["play_num"] += plays[i]
        
    
    # 노래 횟수가 큰 거 부터.
    sorted_data = dict(sorted(album.items(), key=lambda item: item[1]['play_num'], reverse=True))
    for data in sorted_data.values():
        
        # 플레이 리스트를 재생 횟수 내림차순, 고유번호 오름차순으로 정렬
        data["play_list"].sort(key=lambda x: (-x[0], x[1]))
        
        for idx, num_and_unique in enumerate(data["play_list"]):
            if idx == 2:
                break
            result.append(num_and_unique[1])
    return result