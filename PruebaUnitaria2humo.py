from backend import app
import json

def test_productos_endpoint_smoke_test():
    """
    Realiza una prueba de humo en el endpoint '/productos'.
    Verifica que la solicitud GET devuelve un código 200,
    que el tipo de contenido es JSON, y que la respuesta JSON no está vacía.
    """
 
    tester = app.test_client()


    response = tester.get('/productos')


    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    assert response.content_type == 'application/json', \
        f"Expected content type 'application/json', but got '{response.content_type}'"


    try:
        data = json.loads(response.data)
 
        assert isinstance(data, list) and len(data) > 0, \
            "Expected a non-empty list of products in the JSON response."
    except json.JSONDecodeError:

        assert False, "Response is not a valid JSON."
    except Exception as e:
   
        assert False, f"An error occurred while processing JSON response: {e}"

