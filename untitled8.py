class Date:
    def __init__(self, day, month = None, year = None):
        pass
    def __repr__(self):
        pass
    
    def _total_days(self):
        pass
    @staticmethod 
    def _convert_date(tdays):
        pass
    
    def __lt__(self):
        pass
    
    def __gt__(self):
        pass
    
    def __le__(self):
        pass
    
    def __ge__(self):
        pass
    
    def __ge__(self):
        pass
    
    def __le__(self):
        pass
    
    def __add__(self, days):
        pass
    
    def __sub__(self, days):
        pass
    
d = Date(37320)
k = Date('12/11/1992')
m = Date(10,12,2022)

print(d)
print(k)
print(m)

result = m+2
print(result)

result = k-2
print(result)

if k > m:
    print('k > m')
elif k < m:
    print('k < m')
elif k == m:
    print('k == m')

