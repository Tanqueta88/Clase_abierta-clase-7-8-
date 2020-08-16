import unittest  # clase padre (A los test los ejecuta una libreria de unittest)


class Pruebas_de_standards(unittest.TestCase):  # clase que contiene los test's

    def test_suma(self):  # metodo= prueba en si misma siempew dwbe comenzar con la palabra test
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)  # a & b deben ser iguales para que la prueba pase nos dice si dos elementos sean iguales

    def test_otra_suma(self):
        a = 5 + 1
        b = 7
        self.assertNotEqual(a, b)  # a & b no deben ser iguales (es valida la forma( 5+1, 7)como parametro# )

    def test_algo_es_verdadero(self):
        a = 2 + 3
        b = 3 + 1
        self.assertTrue(a > b)

    def test_algo_es_mayor_II(self):
        a = 50
        b = 30
        self.assertGreater(a, b)

    @unittest.skip(“not needed now”)
    def test_algo_es_mayor_o_igual(self):
        a = 4
        b = 4
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 4
        b = 5
        self.assertLess(a, b)

    def test_algo_es_menor_o_igual(self):
        a = 4
        b = 4
        self.assertLessEqual(a, b)

    def test_comparar_listas(self):
        a=[1, 2, "fruta"]
        b=[1, 2, "fruta"]
        self.assertListEqual(a, b)



if __name__ == '__main__':
    unittest.main()
