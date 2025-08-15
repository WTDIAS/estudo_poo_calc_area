# Estudo de POO com Python - Conceitos aprendidos:
#=================================================
# .Abstração
# .Herança
# .Polimorfismo
# .**kwargs
# .Encapsulamento
#=================================================

from abc import ABC, abstractmethod

#==============================
# classe Forma
#==============================
class Forma(ABC):
    @abstractmethod
    def calc_area(self,**kwargs) -> None:
        raise NotImplementedError


#==============================
# classe Circulo
#==============================
class Circulo(Forma):
    def __init__(self,**kwargs):
        if not "raio" in kwargs:
            raise ValueError("Não encontrado chave raio em kwargs.")
        self.raio = kwargs["raio"]

    @property
    def raio(self) -> float:
        return self._raio
    
    @raio.setter
    def raio(self, valor) -> None:
        if not isinstance(valor,(float,int)):
            raise ValueError("Raio deve ser float ou int.")
        if valor < 1:
            raise ValueError("Raio deve ser maior que zero.")
        self._raio = valor

    def calc_area(self) -> str:
        resultado = round(3.14 * (self.raio **2),2)
        return f"A área do circulo é: {resultado:.2f}"
    
#==============================
# classe Triangulo
#==============================
class Triangulo(Forma):
    def __init__(self, **kwargs):
        if not "base" in kwargs:
            raise ValueError("Não encontrado chave base em kwargs.")
        self.base = kwargs["base"]
        if not "altura" in kwargs:
            raise ValueError("Não encontrado chave altura em kwargs.")
        self.altura = kwargs["altura"]        
    
    @property
    def base(self) -> float:
        return self._base
    
    @base.setter
    def base(self, valor) -> None:
        if not isinstance(valor,(float,int)):
            raise ValueError("Base deve ser float ou int.")
        if valor < 1:
            raise ValueError("Base deve ser maior que zero.")
        self._base = valor


    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, valor) -> None:
        if not isinstance(valor,(float,int)):
            raise ValueError("Altura deve ser float ou int.")
        if valor < 1:
            raise ValueError("Altura deve ser maior que zero.")
        self._altura = valor

    def calc_area(self) -> str:
        resultado = round((self.base * self.altura) / 2,2)
        return f"A área do triangulo é: {resultado:.2f}"
    
#==============================
# classe Retangulo
#==============================
class Retangulo(Forma):
    def __init__(self,**kwargs):
        if not "base" in kwargs:
            raise ValueError("Não encontrado chave base em kwargs.")
        self.base = kwargs["base"]
        if not "altura" in kwargs:
            raise ValueError("Não encontrado chave altura em kwargs.")
        self.altura = kwargs["altura"]

    @property
    def base(self) -> float:
        return self._base
    
    @base.setter
    def base(self, valor) -> None:
        if not isinstance(valor,(float,int)):
            raise ValueError("Base deve ser float ou int.")
        if valor < 1:
            raise ValueError("Base deve ser maior que zero.")
        self._base = valor
    
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, valor) -> None:
        if not isinstance(valor,(float,int)):
            raise ValueError("Altura deve ser float ou int.")
        if valor < 1:
            raise ValueError("Altura deve ser maior que zero.")
        self._altura = valor

    def calc_area(self) -> str:
        resultado = round(self.base * self.altura,2)
        return f"A área do retangulo é: {resultado:.2f}"


#==============================
# Execução
#==============================
if __name__ == "__main__":
    class CalcularArea:
        def executar(self):
            formas = [
                Circulo(raio=5),
                Triangulo(base=10, altura=4),
                Retangulo(base=8, altura=3)
            ]

            for forma in formas:
                print(forma.calc_area())

    calc = CalcularArea()
    calc.executar()