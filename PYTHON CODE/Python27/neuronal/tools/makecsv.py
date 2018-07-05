
def main():
	f = open("large.csv","w")

	for i in range(0,60000):
		f.write("ORA-100%s, Description 1%s \n"%(i,i)) 
		
	f.close()