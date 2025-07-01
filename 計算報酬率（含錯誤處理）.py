#calc_return(yesterday,today)

def calc_return(yesterday,today):
    try:
        if yesterday is None or today is None:
            return '資料缺漏'
        return (today-yesterday)/yesterday
    except ZeroDivisionError:
        return '無法計算'

print(calc_return(100, 105))    
print(calc_return(0, 105))      
print(calc_return(None, 105))
print(calc_return(105, 105)) 