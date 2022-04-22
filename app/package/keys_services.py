from app.exceptions.keys_exceptions import MissingKeys

def validate_keys(payload: dict, expected_keys: set):

    body_keys = set(payload.keys())
    invalid_keys = body_keys - expected_keys
    missing_keys = len(body_keys) - len(expected_keys)

    if invalid_keys:
        raise KeyError(
            {
                "error": "Invalid keys. Please, check your keys",
                "expected": list(expected_keys),
                "wrong_keys": list(invalid_keys)
            }
        )

    if missing_keys:
        raise MissingKeys({
            "error": "Keys are missing. Please, check your keys",
            "expected": list(expected_keys),
            "received": list(body_keys)
        })