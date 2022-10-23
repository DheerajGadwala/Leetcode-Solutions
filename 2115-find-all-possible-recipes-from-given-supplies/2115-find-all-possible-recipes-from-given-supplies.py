class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        adj= {recipes[i]:ingredients[i] for i in range(n)}
        black = set(supplies)
        reject = set()
        grey = set()
        
        def dfs(item):
            # print(item, black, grey, reject)
            if item in black:
                return True
            elif item in grey or item in reject or item not in adj:
                return False
            else:
                ret = True
                grey.add(item)
                for ing in adj[item]:
                    ret &= dfs(ing)
                grey.remove(item)
                if ret:
                    black.add(item)
                else:
                    reject.add(item)
                return ret

        ret = []
        for item in recipes:
            if dfs(item):
                ret.append(item)
        return ret