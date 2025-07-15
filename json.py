import json
import base64

data = {
    'id': 5192,
    'media': {
        'spoiler': False,
        'photo': {
            '_': 'Photo',
            'id': 52716568027271,
            'sizes': [
                {
                    '_': 'PhotoStrippedSize',
                    'type': 'i',
                    'bytes': b'\x01\x02\x03'
                },
                {
                    '_': 'PhotoSize',
                    'size': 45678
                }
            ]
        }
    }
}

def serialize(obj):
    if isinstance(obj, bytes):
        return {'__bytes__': True, 'data': base64.b64encode(obj).decode('utf-8')}
    return obj

serialized_json = json.dumps(data, default=serialize, indent=2)
print("Сериализованные данные (JSON):\n", serialized_json)

def deserialize(obj):
    if '__bytes__' in obj:
        return base64.b64decode(obj['data'])
    return obj

deserialized_data = json.loads(serialized_json, object_hook=deserialize)
print("\nДесериализованные данные:")
print(deserialized_data)
