from voluptuous import Schema, ALLOW_EXTRA

fact = Schema({
    'fact': str,
    'length': int
})

facts = Schema({
    'data': [fact]
},
    extra=ALLOW_EXTRA
)
