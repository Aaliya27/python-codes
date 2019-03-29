from prg12 import add_part, see_part

while True:
	choice=input("enter your choice:\n\
		1.add participant\n\
		2.see participant\n")
	if choice=='1':
		add_part()
	elif choice=='2':
		see_part()
	else:
		break
