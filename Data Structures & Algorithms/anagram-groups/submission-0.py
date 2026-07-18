class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Mapping: conteo → lista de anagramas
        
        for s in strs:  # Para cada palabra
            count = [0] * 26  # Array de 26 posiciones (a-z)
            
            for c in s:  # Para cada carácter
                count[ord(c) - ord("a")] += 1  # Contar ocurrencias
            
            res[tuple(count)].append(s)  # Agrupar por conteo
        
        return list(res.values())# Retornar los grupos