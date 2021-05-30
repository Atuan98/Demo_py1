
def tim_tu_dai_nhat(str_):
	chuoi1 = 0
	list_ = []
	i = 0
	if str_:
		for ky_tu in str_:
			if ky_tu != " ":
				chuoi1 += 1
				if str_.index(ky_tu) == len(str_) - 2:
					list_.insert(i, chuoi1 + 1)
					break
			else:
				list_.insert(i, chuoi1)
				i+=1
				chuoi1 = 0
		print(f"{max(list_)}")
	else:
		print("Chuoi rong")		
m = input("Hay nhap chuoi: ")
tim_tu_dai_nhat(m)