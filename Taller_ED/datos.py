class HashTable:
    def __init__(self, size = 7):
        self.size = size
        self.table = [[] for _ in range(self.size)]       
        

    def _hash(self, key):
        hash_value = 5381
        for char in key:
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value
    
    
    def set_item(self, key, value):
        index = self._hash(key)%self.size
        bucket = self.table[index]
        for i in bucket:
            if i[0] == key:
                i[1] = value
                return
        bucket.append([key, value])
    
    def get_item(self, key):
        index = hash(key)%self.size
        if self.table[index]!=[]:
            bucket = self.table[index]
            for i in bucket:
                if i[0] == key:
                    return i[1]
        return None

    def remove_item(self, key):
        index = hash(key)%self.size
        if self.table[index][0]!=[]:
            bucket = self.table[index]
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket.pop(i)
        return None  

    def keys(self):
        all_keys = []
        for i in range(self.size):
            if self.table[i]:
                for j in self.table[i]:
                    all_keys.append(j[0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.table): 
            print(i, ": ", val)

hash_table = HashTable(size=7)

with open('Taller_ED/estudiantes.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    values = line.strip().split('-')
    student_name = values[0]
    student_id = values[1]
    subjects = values[2::2]
    grades = values[3::2]

    # Calcula el promedio de las notas
    grades_float = [float(grade) for grade in grades]
    average = sum(grades_float) / len(grades_float)

    # Crea un diccionario con la información del estudiante
    student_info = {
        'name': student_name,
        'subjects': subjects,
        'grades': grades_float,
        'average': average
    }

    # Guarda la información del estudiante en la tabla hash
    hash_table.set_item(student_id, student_info)
hash_table.print_table()