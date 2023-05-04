class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        banned = [False] * n
        radiant, dire = 0, 0
        for i in senate:
            if i == "R":
                radiant += 1
            else:
                dire += 1
        dire_banned, radiant_banned = 0, 0
        while dire != 0 and radiant != 0:
            i = 0
            while i < n and dire != 0 and radiant != 0:
                if senate[i] == "R":
                    if radiant_banned > 0:
                        senate[i] = ""
                        radiant_banned -= 1
                    else:
                        dire_banned += 1
                        dire -= 1
                elif senate[i] == "D":
                    if dire_banned > 0:
                        senate[i] = ""
                        dire_banned -= 1
                    else:
                        radiant_banned += 1
                        radiant -= 1
                i += 1
                #print(senate, radiant, dire)
        return "Dire" if radiant == 0 else "Radiant"
                
                    
                    