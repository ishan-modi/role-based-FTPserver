import sys,select,socket,os,time
from thread import *

def clientthread(conn):
	conn.send("Enter user name :")	
	usrname=conn.recv(1024)
	
	conn.send("Enter password :")
	pswd=conn.recv(1024)
		
	if usrname in boss and pswd==boss[usrname]:
		while True:			
			conn.send("(u) for upload (d) for download (bye) for exit")
			c=conn.recv(1024)
			if(c=='u'):
				upload(conn,False)
			elif(c=='d'):
				download(conn)
			else:
				break
					
	if usrname in employee and pswd==employee[usrname]:
		while True:	
			conn.send("(d) for download (bye) for exit")
			c=conn.recv(1024)
			if(c=='d'):			
				download(conn,False)
			else:
				break

	conn.send('bye')		
	remove(conn)
	conn.close()
		
	
def download(conn,fullaccess=True):

	conn.send("Enter file path :")
	filename=conn.recv(1024)
	
	if os.path.isfile(filename):
		if(filename[0]!='/'):
			conn.send('exists'+filename)
			time.sleep(0.00001)
			conn.send('filesize'+str(os.path.getsize(filename)))
			time.sleep(0.00001)
		else:
			conn.send('exists'+find(filename))			
			conn.send('filesize'+str(os.path.getsize(filename)))						
			if(fullaccess!=True):
				fullaccess=checkaccess(filename,conn)
				
		if(fullaccess==True or filename[0]!='/'):
			conn.send('do you want to download (y/n)')
						
			c=conn.recv(1024)
			if c=='y':
				cnt=0
				data=""
				with open(filename,'rb') as f:				
					while(cnt<=(os.path.getsize(filename))//1024):
						cnt+=1						
						data=f.read(1024)						
						conn.send(data)
						
	else:
		conn.send("not found")
	
def upload(conn,fullaccess=True):
	filepath=""
	
	conn.send("Enter file path :")
	filename=conn.recv(1024)	
	
	if(filename[0]=='/'):
		filepath=filename		
		filename=find(filepath)
		filepath=filepath[:(len(filepath)-len(filename)-1)]					
		if(fullaccess!=True):			
			fullaccess=checkaccess(filepath,conn)			
			
	if(fullaccess==True or filepath==""):
		conn.send('upload'+filename)
		filesize=conn.recv(1024)
		cnt=0
		data=""
		while(cnt<=(int(filesize))//1024):
			cnt+=1			
			data+=conn.recv(1024)
			
		if filepath!="":
			os.chdir(filepath)		
		f=open('new_'+filename,'wb')
		f.write(data)
		f.close()
	
def checkaccess(filepath,conn):
	global access
	for i in access:
		if(filepath.find(i)!=-1):
			conn.send("access granted")			
			return True;
	conn.send("access denied")
	return False;
		

def find(filename):
	f=''
	i=len(filename)-1	
	while(filename[i]!='/' and i>=0):
		f+=filename[i]
		i-=1
	return f[::-1]

def remove(conn):
	for sock in list_of_conn:
		if sock == conn:
			list_of_conn.remove(conn)


serversoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=12346
serversoc.bind(('100.100.239.54',port))

serversoc.listen(5)
list_of_conn = []

boss={'aaa':'12345','bbb':'23456'}
employee={'ccc':'54321','ddd':'65432'}
access=['/home/ishan/Desktop','/home/ishan/Downloads']

while True:
	conn,addr=serversoc.accept()
	
	list_of_conn.append(conn)

	print str(addr) +"connected"
	
	start_new_thread(clientthread,(conn,))

