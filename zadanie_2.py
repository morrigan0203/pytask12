
import json

class Factorial:

    def __init__(self, k) -> None:
        self.history = []
        self.k = k
    
    def __call__(self, fact):
        res = 1
        for i in range(1,fact+1):
            res = res * i
        if len(self.history) == self.k:
            self.history.pop(0)
        self.history.append((fact, res))
        return res
    
    def __str__(self) -> str:
        return f'Factorial with history {self.k} elements : {self.history}'
    
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.history)
        with open("TesT_12/factorial_res.json", "w") as f:
            json.dump(self.history, f, indent=2)


if __name__=="__main__":
    f = Factorial(3)
    print(f(3))
    print(f(5))
    print(f(10))
    print(f(2))
    print(f(7))

    with f as fe:
        print(f)




