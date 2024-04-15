from django.test import TestCase
from appmanager.models import Usuario, Sucursal
# Create your tests here.


class SucursalTestCase(TestCase):
    def test_create_branch(self):
        """
        Prueba que se pueda crear una sucursal.
        """
        usuario = Usuario.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )

        branch = Sucursal.objects.create(
            sucursal_nombre="Sucursal de Prueba",
            sucursal_ubicacion="Calle Falsa 123",
            sucursal_cod_gerente=usuario,
            sucursal_vigente=True
        )

        self.assertEqual(branch.sucursal_nombre, "Sucursal de Prueba")
        self.assertEqual(branch.sucursal_ubicacion, "Calle Falsa 123")
        self.assertEqual(branch.sucursal_cod_gerente, usuario)
        self.assertTrue(branch.sucursal_vigente)