def dem_so_luong(list_):
	for i in range(len(list_)):
		if type(list_[i]) == tuple:
			break
	print(f"So luong phan tu trong list cho den khi gap tuple: {i}")


list_ = [1,3,4,5,6,7,8,(123,123,45)]
dem_so_luong(list_)