import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calc_area import Circulo,Triangulo,Retangulo

#==============================
# classe circulo
#==============================
class TestCalcAreaCirculo(unittest.TestCase):
    def setUp(self):
        self.raio_valido = 12.5
        self.circulo = Circulo(raio=self.raio_valido)

    def test_init_circulo_sucesso(self):
        #verifica se o circulo foi criado corretamente
        self.assertEqual(self.circulo.raio,self.raio_valido)

    def test_init_sem_chave_falha(self):
        with self.assertRaises(ValueError):
            #verifica a criação sem a chave raio levanta erro com outro nome para chave
            self.circulo = Circulo(chave=10)

    def test_retorno_raio_sucesso(self):
        #verifica se a propriedade raio retorna o valor esperado
        self.assertEqual(self.circulo.raio,12.5)
    
    def test_raio_invalido_falha(self):
        #verifica várias possibilidades de valores para raio em que poderá levantar falha
        valores_invalidos = ["","a",-1,0]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Circulo(raio=valor)

    def test_calc_area(self):
        #verifica se o metodo esta funcionando como esperado
        resultado = 3.14 * (self.circulo.raio **2)
        esperado = f"A área do circulo é: {resultado:.2f}"
        self.assertEqual(self.circulo.calc_area(),esperado)

#==============================
# classe Triangulo
#==============================
class TestCalcAreaTriangulo(unittest.TestCase):
    def setUp(self):
        self.base_valida = 15.8
        self.altura_valida = 7.5
        self.triangulo = Triangulo(base=self.base_valida,altura=self.altura_valida)

    def test_init_triangulo_sucesso(self):
        #verifica se triangulo foi criado corretamente
        self.assertEqual(self.triangulo.base,self.base_valida)
        self.assertEqual(self.triangulo.altura,self.altura_valida)

    def test_init_sem_chave_base_e_altura_falha(self):
        #verifica se levantara erro ao tentar criar Triangulo sem as chaves: base e altura
        with self.assertRaises(ValueError):
            Triangulo(x=10,altura=20)
        with self.assertRaises(ValueError):
            Triangulo(base=10,y=20)

    def test_retorno_base_e_altura_sucesso(self):
        #verifica se os valores de base e altura retornam corretos
        self.assertEqual(self.triangulo.base,15.8)
        self.assertEqual(self.triangulo.altura,7.5)

    def test_base_e_altura_invalidos_falha(self):
        #verifica varias possibilidade de erro para dados inválido para base e altura
        valores_invalidos = [
            {"base":"", "altura":""},
            {"base":-1, "altura":-1},
            {"base":"abc", "altura":"abc"},
            {"base":0, "altura":0}
            ]
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Triangulo(**valor)

    def test_calc_area_sucesso(self):
        #verifica se o metodo esta funcionando como esperado
        self.triangulo = Triangulo(base=self.base_valida,altura=self.altura_valida)
        resultado = (self.triangulo.base * self.triangulo.altura)/2
        esperado = f"A área do triangulo é: {resultado:.2f}"
        self.assertEqual(self.triangulo.calc_area(),esperado)

#==============================
# classe Retangulo
#==============================
class TestCalcAreaRetangulo(unittest.TestCase):
    def setUp(self):
        self.altura_valida = 9.9
        self.base_valida = 5
        self.retangulo = Retangulo(base=self.base_valida,altura=self.altura_valida)

    def test_init_retangulo_sucesso(self):
        #verifica se o retangulo foi criado corretamente
        self.assertEqual(self.retangulo.base,self.base_valida)
        self.assertEqual(self.retangulo.altura,self.altura_valida)

    def test_init_sem_chave_base_e_altura_falha(self):
        #verifica se levantar falha ao não informar as chaves base e altura
        with self.assertRaises(ValueError):
            Retangulo(x=9.5,altura=10.9)
        with self.assertRaises(ValueError):
            Retangulo(base=9.5,y=10.9)

    def test_retorno_base_altura_sucesso(self):
        #verifica se base e altura estão retornando corretamente
        self.assertEqual(self.retangulo.base,5)
        self.assertEqual(self.retangulo.altura,9.9)

    def test_base_altura_falha(self):
        #verifica varios valores invalidos para base e altura irão levantar falha
        valores_invalidos = [
            {"base":"", "altura":""},
            {"base":-1, "altura":-1},
            {"base":"abc", "altura":"abc"},
            {"base":0, "altura":0}
            ]
        
        for valor in valores_invalidos:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Retangulo(**valor)

    def test_calc_area_sucesso(self):
        #verifica se o metodo esta funcionando como esperado
        self.retangulo = Retangulo(base=self.base_valida,altura=self.altura_valida)
        resultado = self.retangulo.base * self.retangulo.altura
        esperado = f"A área do retangulo é: {resultado:.2f}"
        self.assertEqual(self.retangulo.calc_area(),esperado)


if __name__ == "__main__":
    unittest.main()