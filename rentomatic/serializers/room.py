import json

class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try: 
            to_serialise = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
        }
            return to_serialise
        except AttributeError: # pragma: no cover
            return super().default(o)