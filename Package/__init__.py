def data_extract():
    member = dict()
    member['name'] = 'Michael'
    member['dob'] = '19 October 1998'
    member['address'] = 'Owl Street'
    member['gender'] = 'Male'
    return member


def data(result):
    print(f"Name : {result['name']}")
    print(f"Date of Birth : {result['dob']}")
    print(f"Address : {result['address']}")
    print(f"Gender : {result['gender']}")

