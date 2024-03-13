import sys
import unittest


class TestLibraries(unittest.TestCase):

    def test_correct_version(self):
        found = (sys.version_info.major, sys.version_info.minor)

        self.assertEqual(found, (3, 11), 'Versão incorreta do Python encontrada! Deve ser a versão 3.11')

    def test_libraries_available(self):
        libraries = [
            ('numpy', 1),
            ('pandas', 2),
            ('dash', 2),
            ('flask', None),
            ('sklearn', 1),
            ('scipy', 1),
            ('tqdm', None),
            ('matplotlib', 3),
            ('jupyter', 1),
            ('nbconvert', None),
            ('db2', None),
            ('ibm_db', None),
            ('plotly', None),
            ('shap', None),
        ]

        for lib, version in libraries:
            try:
                exec(f'import {lib}')
                self.assertTrue(True, 'Todas as bibliotecas foram instaladas com sucesso!')
            except ImportError:
                self.fail('Não foi possível importar a biblioteca')


if __name__ == '__main__':
    unittest.main()
