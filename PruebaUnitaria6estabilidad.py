from backend import app
import json
import time 

def test_productos_endpoint_grey_box_behavior():
    """
    Prueba de caja gris para el endpoint '/productos'.
    Combina el comportamiento externo con un conocimiento parcial de la estructura interna.
    Verifica:
    - La solicitud GET devuelve un código de estado 200.
    - El tipo de contenido de la respuesta es 'application/json'.
    - La respuesta JSON es una lista.
    - Si la lista no está vacía, sus elementos son objetos (diccionarios)
      y contienen claves específicas esperadas (ej. 'id', 'nombre', 'precio').
      Esto es "caja gris" porque sabemos qué claves esperar sin ver la implementación exacta.
    """

    tester = app.test_client()


    response = tester.get('/productos')


    assert response.status_code == 200, \
        f"Expected status code 200, but got {response.status_code} for /productos"


    assert response.content_type == 'application/json', \
        f"Expected content type 'application/json', but got '{response.content_type}' for /productos"

    try:

        data = json.loads(response.data)

 
        assert isinstance(data, list), "Expected the JSON response for /productos to be a list."

        if data:
            expected_product_keys = ['id', 'nombre', 'precio']
            for item in data:
                assert isinstance(item, dict), \
                    "Expected each item in the /productos list to be a JSON object (dictionary)."
                for key in expected_product_keys:
                    assert key in item, f"Product item is missing expected key: '{key}'"
              

    except json.JSONDecodeError:
        assert False, "Response from /productos is not a valid JSON."
    except Exception as e:
        assert False, f"An unexpected error occurred during grey box test for /productos: {e}"

def test_get_specific_product_grey_box():
    """
    Prueba de caja gris para obtener un producto específico por ID (ej. /productos/1).
    Verifica el comportamiento externo y la estructura parcial del objeto devuelto.
    """
    tester = app.test_client()
  
    response = tester.get('/productos/1')

    assert response.status_code == 200, \
        f"Expected status code 200, but got {response.status_code} for /productos/1"
    assert response.content_type == 'application/json', \
        f"Expected content type 'application/json', but got '{response.content_type}' for /productos/1"

    try:
        data = json.loads(response.data)

      
        assert isinstance(data, dict), "Expected the JSON response for a single product to be a dictionary."
        expected_product_keys = ['id', 'nombre', 'precio'] 
        for key in expected_product_keys:
            assert key in data, f"Single product object is missing expected key: '{key}'"
    

    except json.JSONDecodeError:
        assert False, "Response from /productos/1 is not a valid JSON."
    except Exception as e:
        assert False, f"An unexpected error occurred during grey box test for /productos/1: {e}"

def test_stability_productos_endpoint():
    """
    Prueba de estabilidad para el endpoint '/productos'.
    Envía múltiples solicitudes repetidas para verificar que el endpoint
    mantiene un rendimiento consistente y no sufre de degradación o fallos
    bajo una carga prolongada simulada.
    """
    tester = app.test_client()
    num_requests = 100 
    delay_seconds = 0.01 
    print(f"\nRunning stability test for /productos with {num_requests} requests...")

    for i in range(num_requests):
        response = tester.get('/productos')

        assert response.status_code == 200, \
            f"Stability test failed at request {i+1}: Expected status 200, got {response.status_code}"

        assert response.content_type == 'application/json', \
            f"Stability test failed at request {i+1}: Expected JSON content, got {response.content_type}"

        try:
           
            data = json.loads(response.data)
            assert isinstance(data, list), \
                f"Stability test failed at request {i+1}: Expected JSON response to be a list."
        except json.JSONDecodeError:
            assert False, f"Stability test failed at request {i+1}: Response is not a valid JSON."
        except Exception as e:
            assert False, f"Stability test failed at request {i+1}: An error occurred: {e}"

        time.sleep(delay_seconds)

    print(f"Stability test for /productos completed successfully after {num_requests} requests.")
