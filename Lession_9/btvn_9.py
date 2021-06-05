def nhap():
	str_ = input("Hay viet 1 doan van: ")
	return str_

def str_to_tuple(str_):
	str1 = ""
	tuple_ = ()
	for i in range(len(str_)):
		if str_[i] != " ":
			str1 += str_[i]
		else:
			tuple_+= str1,
			str1 = ""
		if i == len(str_) - 1:
			tuple_ += str1,
	return(tuple_) 


def tuple_to_dict(tuple_):
	dict_ = {}
	for i in tuple_:
		dict_[i] = tuple_.count(i)
	print(dict_)

tuple_to_dict(str_to_tuple(nhap()))

