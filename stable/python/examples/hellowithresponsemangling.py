def foo(event, context):
    response = event["extensions"]["response"]
    response.set_header("test", "foo")
    response.status = 204
