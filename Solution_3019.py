class Solution_3019:
    def countKeyChanges(s: str) -> int:
        temp = s.lower()
        temp2 = list(temp)
        cnt = 0

        for i, wd in enumerate(temp2):
            if i < len(temp2)-1:
                if wd == temp2[i+1]:
                    continue
                else:
                    cnt += 1
        return cnt     

    countKeyChanges( "aAbBcC")