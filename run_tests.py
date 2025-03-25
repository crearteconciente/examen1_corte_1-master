from tests.newmath import example, test_factor, test_string

example.test_deberia_saludar_a_mundo()
example.test_deberia_saludar_a_una_persona()

print("\nFACTOR")
test_factor.test_deberia_resultado_factor_58()
test_factor.test_deberia_resultado_factor_652()
test_factor.test_deberia_resultado_factor_227()
test_factor.test_deberia_resultado_factor_7()#deberia dar error

print("\nFIBONACCI")
test_factor.test_deberia_resultado_fibonacci_1()
test_factor.test_deberia_resultado_fibonacci_7_86()
test_factor.test_deberia_resultado_fibonacci_error()

print("\nSTRING")
print("\nVOCALES")
test_string.test_deberia_contar_vocales()

print("\nMULTIPLICADOR DE VOCALES")
test_string.test_deberia_multiplicar_vocales()
test_string.test_deberia_multiplicar_vocales_error()

print("\nPORCENTAJE DE VOCALES")
test_string.test_deberia_porcentaje_vocales()
