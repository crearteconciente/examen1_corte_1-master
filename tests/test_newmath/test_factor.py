import unittest
from newmath.factor import multiplicador_factor, factor_fibonacci



class Testmultiplicador_factor(unittest.TestCase):

    def test_multiplicador_factor_positivos(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(8, 12, 150)
        esperado: int = 652
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(1, 1, 1)
        esperado: int = 6
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(1, 1, 1) #error
        esperado: int = 7
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_negativos(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(-1, -1, -1)
        esperado: int = 3
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-2, -1, -1)
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-1, -1, -1) #error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_negativos_y_positivos(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(-1, -1, 1)
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-1, 1, 1)
        esperado: int = 5
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-1, -1, 1)
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_rango_0_a_9(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(0, 0, 0)
        esperado: int = 0
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(0, 1, 0)
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(0, 1, 0) #error
        esperado: int = 3
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_rango_10_a_99(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(10, 10, 10)
        esperado: int = 90
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(11, 10, 10)
        esperado: int = 93
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(11, 10, 10)#error
        esperado: int = 0
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_rango_100_en_adelante(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(100, 100, 100)
        esperado: int = 1200
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(101, 100, 100)
        esperado: int = 1204
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(101, 100, 100)#error
        esperado: int = 1205
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_negativos_float(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(-0.1, -0.1, -0.1)
        esperado: int = 0.30000000000000004
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-0.2, -0.1, -0.1)
        esperado: int = 0.4
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(-0.2, -0.1, -0.1)#error
        esperado: int = 0.41
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_de_cero_a_9_float(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(0.1, 0.1, 0.1)
        esperado: int = 0.6000000000000001
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(0.2, 0.1, 0.1)
        esperado: int = 0.8
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(0.2, 0.1, 0.1)#error
        esperado: int = 0.9
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_de_10_en_99_float(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(10.1, 10.1, 10.1)
        esperado: int = 90.89999999999999
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(10.2, 10.1, 10.1)
        esperado: int = 91.19999999999999
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(10.2, 10.1, 10.1)
        esperado: int = 91.2
        self.assertEqual(restultado, esperado)

    def test_multiplicador_factor_de_100_en_adelante_float(self):
        """
        Se va verificar los factores
        """
    
        restultado: int =  multiplicador_factor(100.1, 100.1, 100.1)
        esperado: int = 1201.1999999999998
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(100.2, 100.1, 100.1)
        esperado: int = 1201.6
        self.assertEqual(restultado, esperado)

        restultado: int =  multiplicador_factor(100.2, 100.1, 100.1)#error
        esperado: int = 1201.7
        self.assertEqual(restultado, esperado)


#*************************************************************************************************
class Testfactor_fibonacci(unittest.TestCase):
     def test_factor_fibonacci_numeros_iguales(self):
        """
        Verifica valores básicos en la serie de Fibonacci.
        """
        resultado = factor_fibonacci(1, 1, 1)  
        esperado = 1.0
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(5, 5, 5) 
        esperado = 8.0
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(5, 5, 5) #error
        esperado = 1.0
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_numeros_diferentes(self):
        """
        Verifica valores básicos en la serie de Fibonacci.
        """
        resultado = factor_fibonacci(1, 2, 1)  
        esperado = 1.0
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(1, 2, 3)  
        esperado = 3.0
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(1, 2, 3)  
        esperado = 4.0
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_numeros_positivos(self):
        """
        Verifica valores básicos en la serie de Fibonacci.
        """
        resultado = factor_fibonacci(2, 3, 4)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(5, 3, 4)  
        esperado = 5.8
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(5, 3, 4)  #error
        esperado = 5.9
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_numeros_negativos(self):
        """
       no puede ser negativo.
        
        """
 
        resultado = factor_fibonacci(-1, -2, 3)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(-1, 2, -3)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)
        
        
        resultado = factor_fibonacci(-1, -2, -3)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        
     def test_factor_fibonacci_con_ceros(self):
        """
        no puede existir cero
        
        """
 
        resultado = factor_fibonacci(0, 0, 0)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(0, 1, 0)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(1, 0, 0)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_con_un_solo_numero(self):
        """

        
        """
        resultado = factor_fibonacci(6)  
        esperado = 1.33
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(5)  
        esperado = 1.0
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(7)  
        esperado = 1.86
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_con_dos_numeros(self):
        """
        
    
        """
        resultado = factor_fibonacci(6,1)  
        esperado = 3.33
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(6,2)  
        esperado = 3.5
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(6,3)  
        esperado = 2.67
        self.assertEqual(resultado, esperado)

     def test_factor_fibonacci_mayor_a_100(self):
        """
           resultado = factor_fibonacci(100,100,100) 
        no deja se bloquea
        """
     def test_factor_fibonacci_mayor_a_50(self):
        """
        no deja se bloquea
                resultado = factor_fibonacci(50,50,50)  
                 esperado = 20412414523.19
                 self.assertEqual(resultado, esperado)
    
        """

     def test_factor_fibonacci_mayor_a_10(self):
        """
        
    
        """
        resultado = factor_fibonacci(10,10,10)  
        esperado = 34.1
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(11,10,10)  
        esperado = 50.18
        self.assertEqual(resultado, esperado)

        resultado = factor_fibonacci(11,11,11)  
        esperado = 55.0
        self.assertEqual(resultado, esperado)

