from rentomatic.requests.room_list import build_room_list_request

def test_build_room_list_request_without_parameters():
    request = build_room_list_request()

    assert bool(request) is True

def test_build_room_list_request_from_empty_dict():
    request = build_room_list_request.from_dict({})

    assert bool(request) is True