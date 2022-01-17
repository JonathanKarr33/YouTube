from typing import Union
def calculation(x : Union[int,float], y : Union[int,float]) -> Union[int,float]:
    return (x + y) ** x
print(calculation(3,4))