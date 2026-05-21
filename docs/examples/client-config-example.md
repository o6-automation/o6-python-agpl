# Client Configuration Example

Source example: `examples/highlevel/client_config.py`

This example inspects the exposed `ClientConfig` object and changes a few of its fields directly.

## Explanation

### Accessing the config object

The client configuration is available directly on the client instance.

```python
client = o6.Client()
cfg = client.config
```

### Setting application metadata

The example constructs an `ApplicationDescription` and assigns it to the config.

```python
application_desc = o6.types.ApplicationDescription()
application_desc.application_uri = "urn:example:application"
application_desc.application_name = o6.types.LocalizedText("Example Application")
application_desc.application_type = o6.types.ApplicationType.Client
application_desc.product_uri = "urn:example:product"

cfg.application_description = application_desc
```

### Inspecting nested values

The helper function converts the config object into dictionaries so it can be printed with `json.dumps`.

```python
print(json.dumps(obj_to_dict(cfg), indent=2, default=str))
```

### Updating basic settings

```python
cfg.timeout = 1234
cfg.endpoint_url = "opc.tcp://localhost:4840"
cfg.no_session = True
```

## Full source

```python
# Test for ClientConfig implementation
import pprint
import json
import o6


def obj_to_dict(obj, depth=2):
    if depth == 0:
        return str(obj)
    if isinstance(obj, (bool, int, float, str, type(None))):
        return obj
    if isinstance(obj, (list, tuple)):
        return [obj_to_dict(v, depth - 1) for v in obj]
    attrs = [a for a in dir(obj) if not a.startswith("_")]
    if not attrs:
        return str(obj)
    result = {}
    for attr in attrs:
        try:
            result[attr] = obj_to_dict(getattr(obj, attr), depth - 1)
        except Exception as e:
            result[attr] = f"<Error: {e}>"
    return result


def test_config():
    client = o6.Client()
    cfg = client.config

    application_desc = o6.types.ApplicationDescription()
    print(f"Application-Description type-check {type(application_desc)}")
    application_desc.application_uri = "urn:example:application"
    application_desc.application_name = o6.types.LocalizedText("Example Application")
    application_desc.application_type = o6.types.ApplicationType.Client
    application_desc.product_uri = "urn:example:product"

    cfg.application_description = application_desc
    print(f"Client-Config type-check {type(cfg)}")

    print("All attributes and current value from cfg:")
    print(json.dumps(obj_to_dict(cfg), indent=2, default=str))

    print("Initial Value: " + str(client.config.timeout))
    client.config.timeout = 10000
    print("After Asign: " + str(client.config.timeout))

    print(type(cfg.application_description))

    print(f"timeout: {cfg.timeout} -> setting to 1234")
    cfg.timeout = 1234
    print(f"timeout now: {cfg.timeout}")

    print(f"endpoint_url: {cfg.endpoint_url} -> setting to opc.tcp://localhost:4840")
    cfg.endpoint_url = "opc.tcp://localhost:4840"
    print(f"endpoint_url now: {cfg.endpoint_url}")

    print(f"no_session: {cfg.no_session} -> setting to True")
    cfg.no_session = True
    print(f"no_session now: {cfg.no_session}")


if __name__ == "__main__":
    test_config()
```