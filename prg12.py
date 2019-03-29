event_dict={'1':'cs','2':'google it','3':'treasure hunt'}
part_details={}
def add_part():
	name=input('enter participant name:')
	event=input('enter the serial num of event from the list:\n\
		1.cs\n\
		2.google it\n\
		3.treasure hunt\n')
	part_details[name]=event_dict[event]
	return part_details

def see_part():
	for key,value in part_details.items():
		print(key,value,sep=' - ')


if __name__=='__main__':
	add_part()
	print(part_details)
	see_part()