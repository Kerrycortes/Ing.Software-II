from backend import app
import json

def test_productos_endpoint_black_box_behavior():
    """
    Prueba de caja negra para el endpoint '/productos'.
    Verifica el comportamiento externo esperado:
    - La solicitud GET devuelve un código de estado 200.
    - El tipo de contenido de la respuesta es 'application/json'.
    - La respuesta JSON es una lista.
    - Si la lista no está vacía, sus elementos son objetos (diccionarios).
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
            for item in data:
                assert isinstance(item, dict), \
                    "Expected each item in the /productos list to be a JSON object (dictionary)."

    except json.JSONDecodeError:

        assert False, "Response from /productos is not a valid JSON."
    except Exception as e:

        assert False, f"An unexpected error occurred during black box test for /productos: {e}"
