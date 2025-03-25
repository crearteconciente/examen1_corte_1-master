import unittest
from newmath.string import contar_vocales, multiplicacion_vocales, porcentaje_vocales

class TestContarVocales(unittest.TestCase):

    def test_contar_vocales_minusculas(self):
        """
        Se va verificar que las vocales en minúsculas 
        """
    
        restultado: int = contar_vocales("hola")
        esperado: int = 2
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("murcielago")
        esperado: int = 5
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("pirata")
        esperado: int = 3
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("aeiou")#Se hace con un error
        esperado: int = 3
        self.assertEqual(restultado, esperado)



    
    def test_contar_vocales_Mayusculas(self):
        """
        Se va verificar que las vocales en mayúsculas
        """
    
        restultado: int = contar_vocales("PERRO")
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("AEIOU")
        esperado: int = 5
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("hOLA")#se hace con un error 
        esperado: int = 1
        self.assertEqual(restultado, esperado)

    def test_contar_vocales_Mayusculas_y_Minusculas(self):
        """
        Se va verificar que las vocales en mayúsculas y minusculas 
        """
        
        restultado: int = contar_vocales("AEIOUaeiou")       
        esperado: int = 10
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("HOLA como")
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("HOLA como")#con error
        esperado: int = 7
        self.assertEqual(restultado, esperado)

    def test_contar_vocales_Mayusculas_Acentuadas(self):
        """
        Se va verificar que las vocales en mayúsculas acentuadas 
        """
        
        restultado: int = contar_vocales("ÁÉÍÓÚ")       
        esperado: int = 5
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("HÓLÁ")
        esperado: int = 2
        self.assertEqual(restultado, esperado)


        restultado: int = contar_vocales("HÓLÁ")#con error
        esperado: int = 3
        self.assertEqual(restultado, esperado)


    
    def test_contar_vocales_Minusculas_Acentuadas(self):
        """
        Se va verificar que conteo de las vocales  minusculas acentuadas 
        """
        
        restultado: int = contar_vocales("áéíóú")       
        esperado: int = 5
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("cómó")
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("cómó")#con error
        esperado: int = 7
        self.assertEqual(restultado, esperado)




    def test_contar_vocales_Mayusculas_y_Minusculas_Acentuadas(self):
        """
        Se va verificar que las vocales en mayúsculas y minusculas acentuadas 
        """
        
        restultado: int = contar_vocales("ÁÉÍÓÚáéíóú")       
        esperado: int = 10
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("HÓLÁ cómó")
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("HÓLÁ cómó")#con error
        esperado: int = 7
        self.assertEqual(restultado, esperado)

    
    def test_contar_vocales_Minusculas_Acentuado_grave(self):
        """
        todas deben dar error ya que no esta la función con acentuado grave solo reconoce un error el primero
        """
        
        restultado: int = contar_vocales("àèìòù")  #con error    
        esperado: int = 5
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("còmò")#con error
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("hòlà còmò")#con error
        esperado: int = 4
        self.assertEqual(restultado, esperado)

    def test_contar_vocales_Mayuscula_Acentuado_grave(self):
        """
        todas deben dar error ya que no esta la función con acentuado grave solo reconoce un error el primero
        """
        
        restultado: int = contar_vocales("ÀÈÌÒÙ")  #con error    
        esperado: int = 5
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("HÒLÀ")#con error
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("HÒLÀ CÒMÒ")#con error
        esperado: int = 4
        self.assertEqual(restultado, esperado)

    def test_contar_vocales_Mayuscula_minusculas_Acentuado_grave(self):
        """
        todas deben dar error ya que no esta la función con acentuado grave solo reconoce un error el primero
        """
        
        restultado: int = contar_vocales("ÀÈÌÒÙàèìòù")  #con error    
        esperado: int = 5
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("HÒLÀcòmò")#con error
        esperado: int = 2
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("HÒLÀ CÒMÒ ")#con error
        esperado: int = 4
        self.assertEqual(restultado, esperado)

    def test_contar_vocales_minusculas_con_simbolos(self):
        """
       se verifica con simbolos 
        """
        
        restultado: int = contar_vocales("ae$")  
        esperado: int = 2
        self.assertEqual(restultado, esperado)
        
        restultado: int = contar_vocales("a $ %")
        esperado: int = 1
        self.assertEqual(restultado, esperado)

        restultado: int = contar_vocales("aei $$$ ")#con error
        esperado: int = 4
        self.assertEqual(restultado, esperado)


#***********************************************************************************************************

class Testmultiplicacion_vocales(unittest.TestCase):

    def test_multiplicar_vocales_minusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("aeiou")  
        esperado: int = 9
        self.assertEqual(restultado, esperado)
        
        restultado: int = multiplicacion_vocales("un murcielago")
        esperado: int = 7
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("aeiou")#con error
        esperado: int = 4
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_mayusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("AEIOU")  
        esperado: int = -5
        self.assertEqual(restultado, esperado)
       
        
        restultado: int = multiplicacion_vocales("CASA")
        esperado: int = -8
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("AEIOU")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_mayusculas_y_minusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("AEIOUaeiou")  
        esperado: int = 4
        self.assertEqual(restultado, esperado)
       
        
        restultado: int = multiplicacion_vocales("CASAcasa")
        esperado: int = -2
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("AEIOUaeiou")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_minusculas_acentuadas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("á")  
        esperado: int = 4
        self.assertEqual(restultado, esperado)
        
        restultado: int = multiplicacion_vocales("é")
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("á")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)


    def test_multiplicar_vocales_mayusculas_acentuadas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("Á")  
        esperado: int = 4
        self.assertEqual(restultado, esperado)
        
        restultado: int = multiplicacion_vocales("É")
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("Á")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_minusculas_y_mayusculas_acentuadas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("áÁ")  
        esperado: int = 8
        self.assertEqual(restultado, esperado)
        
        restultado: int = multiplicacion_vocales("éÉ")
        esperado: int = 8
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("áÁ")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_minusculas_con_simbolos(self):
            """
        se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
            """
            
            restultado: int = multiplicacion_vocales("aeiou$$$$")  
            esperado: int = 9
            self.assertEqual(restultado, esperado)
            
            restultado: int = multiplicacion_vocales("un murcielago$$$$")
            esperado: int = 7
            self.assertEqual(restultado, esperado)

            restultado: int = multiplicacion_vocales("aeiou$$$$")#con error
            esperado: int = 4
            self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_mayusculas_con_simbolos(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("AEIOU$$$")  
        esperado: int = -5
        self.assertEqual(restultado, esperado)
       
        
        restultado: int = multiplicacion_vocales("CASA$$$$")
        esperado: int = -8
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("AEIOU$$$$")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_mayusculas_y_minusculas_con_simbolos(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("AEIOUaeiou····")  
        esperado: int = 4
        self.assertEqual(restultado, esperado)
       
        
        restultado: int = multiplicacion_vocales("CASAcasa!!!!!")
        esperado: int = -2
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("AEIOUaeiou!!!!!")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)

    def test_multiplicar_vocales_minusculas_acentuadas_con_simbolos(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = multiplicacion_vocales("á$$$")  
        esperado: int = 4
        self.assertEqual(restultado, esperado)
        
        restultado: int = multiplicacion_vocales("é$$$")
        esperado: int = 4
        self.assertEqual(restultado, esperado)

        restultado: int = multiplicacion_vocales("á$$$$$")#con error
        esperado: int = 5
        self.assertEqual(restultado, esperado)


#****************************************************************************************************************************

class Testporcentaje_vocales(unittest.TestCase):
    def test_porcentaje_vocales_minusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("hola, como estas?")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("hola")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("hola")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

    
    def test_porcentaje_vocales_mayusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, COMO ESTAS")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLA")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLA")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

  

    def test_porcentaje_minusculas_y_mayusculas(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, cómo ESTÁS")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

    def test_porcentaje_vocales_mayusculas_con_acento(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, CÓMO ESTÁS")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLÁ")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLÁ")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)


    def test_porcentaje_vocales_minusculas_con_acento(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("hola, cómo estás")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("holá")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("holá")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)
    


    def test_porcentaje_vocales_mayusculas_y_minusculas_con_acento(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, cómo ESTÁS")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

    


    def test_porcentaje_vocales_minusculas_con_numeros(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("hola, como estas12345?")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("hola12345")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("hola12345")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

    
    def test_porcentaje_vocales_mayusculas_con_numeros(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, COMO ESTAS12345")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLA12345")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLA12345")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

  

    def test_porcentaje_minusculas_y_mayusculas_con_numeros(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, cómo ESTÁS12345")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla12345")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOla12345")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)

    def test_porcentaje_vocales_mayusculas_con_acento_con_numeros(self):
        """
       se verifica que los resultados concuerden cambiando cada letra segun lo asignado en la formula
        """
        
        restultado: int = porcentaje_vocales("HOLA, CÓMO ESTÁS12345")  
        esperado: int = 46.15
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLÁ12345")  
        esperado: int = 50
        self.assertEqual(restultado, esperado)

        restultado: int = porcentaje_vocales("HOLÁ12345")  #con error 
        esperado: int = 60
        self.assertEqual(restultado, esperado)