from voluptuous import Schema

single_user = Schema(
    {
        'data': {
            'id': int,
            'email': str,
            'first_name': str,
            'last_name': str,
            'avatar': str
        },
        'support': {
            'url': str,
            'text': str
        }

    })
