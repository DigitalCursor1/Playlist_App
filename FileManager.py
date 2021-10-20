



 


def Fmove(File_Name):
	newName = File_Name
	files = os.listdir("MatchHistory")
	j = 0
	for i in range (len(files)):
			if files[i] == File_Name and j == 0:
					j = j + 1
					newName = File_Name + ("(%d)" % j)
					os.rename(File_Name,newName)
					File_Name = newName
					
			elif files[i] == newName and j != 0:
				j = j + 1
				newName = File_Name[:-3] + ("(%d)" % j)
				os.rename(File_Name, newName)	
				File_Name = newName				
	shutil.move(str(newName), "MatchHistory")