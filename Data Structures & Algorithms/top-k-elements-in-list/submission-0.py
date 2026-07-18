class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # PASO 1: Contar frecuencias con HashMap
        contador = {}
        for num in nums:
            contador[num] = contador.get(num, 0) + 1
    
        # PASO 2: Crear buckets agrupados por frecuencia
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in contador.items():
            buckets[freq].append(num)
    
        # PASO 3: Extraer los k más frecuentes (de atrás hacia adelante)
        resultado = []
        for i in range(len(buckets) - 1, 0, -1):
            resultado.extend(buckets[i])
            if len(resultado) >= k:
                return resultado[:k]