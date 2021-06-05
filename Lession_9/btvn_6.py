def nhap():
    my_dict = {}
    n = int(input("Hay nhap so luong phan tu dict: "))
    i = 0
    while i < n:
        m = input("Hay nhap key: ")
        if my_dict.get(m) is None: 
            my_dict[m] = input("Hay nhap value ")
            i += 1
        else:
            my_dict[m] = input("Hay nhap value ")
    print(my_dict)
    return my_dict

def lay_du_lieu(my_dict):
    new_dict = {}
    new_list = []
    n = int(input("Nhap so luong key muon lay: "))
    if  0 < n < len(my_dict):
        i = 0
        while i < n:
            new_list.insert(i, input("Hay nhap key: "))
            i += 1
        i = 0
        while i < n:
            if new_list[i] in my_dict.keys():
                new_dict[new_list[i]] = my_dict.get(new_list[i])
            else:
                print("Key khong co trong my_dict")
            i += 1 
        print(new_dict)
    else:
        print("Nhap n sai")

lay_du_lieu(nhap())