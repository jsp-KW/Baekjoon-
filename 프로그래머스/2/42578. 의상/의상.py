from collections import defaultdict

def solution(clothes):
#     answer = 1
#     cody = defaultdict(list)
#     for i in range (0, len(clothes)) :
#                 cody[clothes[i][1]].append(clothes[i][0])
    
#     lengths = []
    
#     if len(cody) == 1 :
        
#         answer = len(clothes)
#     else: 
#         temp = []
#         for key in cody.keys() :
#             temp.append((len(cody[key]) +1))
                        
#         for t in temp:
#             answer = answer *t
#         answer= answer -1
        
    
    
    answer = 1
    
    # 얼굴, 상의, 하의, 겉옷
    # 종류별 최대 1가지 의상만 착용 가능
    
    clothes_dic = dict()
    
    for c in clothes :
        clothe = c[0]
        clothe_type = c[1]
        if clothe_type not in clothes_dic :
            clothes_dic[clothe_type]  =1 
        else:
            clothes_dic[clothe_type] +=1
   
    for _, c_count in clothes_dic.items() :
        answer*= (c_count+1)
       
    
    
    
    return answer-1