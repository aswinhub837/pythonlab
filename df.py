
File1=input("Enter the source file to be copied")
File2=input("Enter the destination file name")
Fr=open (File1,"w")

Fw=open(File2,"w")
for line in fr.readlines():
    Fw.write(line)

Fr.close()
