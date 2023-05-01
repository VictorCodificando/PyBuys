from django.test import TestCase
from django.template import Template, Context
from django.template.defaultfilters import stringfilter
from product.models import Categorias
from product.templatetags.custom_tags import formatear_descripcion, obtener_todas_categorias

# Create your tests here.
class CategoriasTestCase(TestCase):
    
    def setUp(self):
        self.categoria1 = Categorias.objects.create(nombre="Categoria 1")
        self.categoria2 = Categorias.objects.create(nombre="Categoria 2", grupo=self.categoria1)
        self.categoria3 = Categorias.objects.create(nombre="Categoria 3", grupo=self.categoria2)
    
    def test_todas_categorias_padres_con_categoria_hija(self):
        categorias_padres = obtener_todas_categorias(self.categoria3.id)
        self.assertEqual(len(categorias_padres), 2)
        self.assertEqual(categorias_padres[0], self.categoria2)
        self.assertEqual(categorias_padres[1], self.categoria1)
        
    def test_todas_categorias_padres_con_categoria_padre(self):
        categorias_padres = obtener_todas_categorias(self.categoria1.id)
        self.assertEqual(len(categorias_padres), 1)
        self.assertEqual(categorias_padres[0], self.categoria1)
        
    def test_todas_categorias_padres_con_id_nulo(self):
        categorias_padres = obtener_todas_categorias(None)
        self.assertEqual(len(categorias_padres), 1)
        self.assertEqual(categorias_padres[0], None)

class TestFormatearDescripcion(TestCase):

    def test_sustituir_punto_bala(self):
        texto = 'Esto es un *ejemplo* de texto con *elementos* de lista.'
        esperado = 'Esto es un •ejemplo• de texto con •elementos• de lista.'
        resultado = formatear_descripcion(texto)
        self.assertEqual(resultado, esperado)

    def test_destacar_comillas_simples(self):
        texto = "Este es un ejemplo de 'texto destacado'."
        esperado = "Este es un ejemplo de 'TEXTO DESTACADO'."
        resultado = formatear_descripcion(texto)
        self.assertEqual(resultado, esperado)

    def test_completo(self):
        texto = """
        Este es un *ejemplo* de texto con *elementos* de lista.
        Aquí hay un bloque destacado:
        '''
        Este texto se destaca.
        Incluso si tiene varias líneas.
        '''
        Fin del bloque destacado.
        """
        esperado = """
        Este es un •ejemplo• de texto con •elementos• de lista.
        Aquí hay un bloque destacado:
        '''
        ESTE TEXTO SE DESTACA.
        INCLUSO SI TIENE VARIAS LÍNEAS.
        '''
        Fin del bloque destacado.
        """
        resultado = formatear_descripcion(texto)
        self.assertEqual(resultado, esperado)

    def test_con_filtro_de_template(self):
        # Configurar el entorno de prueba
        c = Context({'producto': {'descripcion': 'Este es un *ejemplo* de texto con *elementos* de lista.'}})
        t = Template("<p>Descripcion: {{ producto.descripcion|formatear_descripcion }}</p>")
        t.filters['formatear_descripcion'] = stringfilter
        
        # Ejecutar el test
        resultado = t.render(c)
        esperado = "<p>Descripcion: Este es un •ejemplo• de texto con •elementos• de lista.</p>"
        self.assertEqual(resultado, esperado)