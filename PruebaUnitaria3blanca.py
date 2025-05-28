
from backend import app
import json

def test_productos_endpoint_returns_expected_structure():
    """
    Prueba de caja blanca para el endpoint '/productos'.
    Verifica que la solicitud GET devuelve un código 200,
    que el tipo de contenido es JSON, y que la respuesta JSON
    contiene una lista de diccionarios con las claves esperadas.
    """
    tester = app.test_client()
    response = tester.get('/productos')


    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    assert response.content_type == 'application/json', \
        f"Expected content type 'application/json', but got '{response.content_type}'"

    try:
        data = json.loads(response.data)

  
        assert isinstance(data, list), "Expected response to be a list."

      
        if data: 
            for product in data:
                assert isinstance(product, dict), "Each item in the product list should be a dictionary."
               
                expected_keys = ['id', 'nombre', 'precio']
                for key in expected_keys:
                    assert key in product, f"Product dictionary is missing key: '{key}'"
              
                assert isinstance(product['id'], int)
                assert isinstance(product['nombre'], str)
                assert isinstance(product['precio'], (int, float))

    except json.JSONDecodeError:
        assert False, "Response is not a valid JSON."
    except Exception as e:
        assert False, f"An error occurred during JSON processing or assertion: {e}"

def test_productos_endpoint_handles_empty_list():
    """
    Prueba de caja blanca para el endpoint '/productos' cuando no hay productos.
    Esto podría requerir mocking si tu aplicación interactúa con una base de datos.
    Para esta prueba, asumimos que el endpoint devolverá una lista vacía si no hay productos.
    """
    

    tester = app.test_client()
    response = tester.get('/productos') 

    assert response.status_code == 200, "Expected status code 200 even for empty product list."
    assert response.content_type == 'application/json', "Expected content type 'application/json'."

    try:
        data = json.loads(response.data)
        assert isinstance(data, list), "Expected response to be a list."
        assert len(data) == 0, "Expected an empty list when no products are available."
    except json.JSONDecodeError:
        assert False, "Response is not a valid JSON."
    except Exception as e:
        assert False, f"An error occurred during JSON processing or assertion: {e}"
