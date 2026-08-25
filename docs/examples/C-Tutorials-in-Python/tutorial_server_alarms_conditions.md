# Using Alarms and Conditions

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_alarms_conditions.py`

The open62541 tutorial covers server-side alarm and condition handling. The
high-level Python API does not currently expose dedicated alarm/condition
helpers, so this page keeps the same tutorial slot and documents the gap.

```python
def main() -> None:
	print("Alarm and condition parity is not yet available in high-level o6 Python API.")


if __name__ == "__main__":
	main()
```

For now, the closest supported building blocks are server variables, methods,
and client-side event monitoring.
