import sys,select,socket,os,time

def upload(filename):
	global clientsoc
	filesize=os.path.getsize(filename)
	clientsoc.send(str(filesize)) 
	with open(filename,'rb') as f:
		cnt=0
		data=""
		while(cnt<=filesize//1024):
			cnt+=1			
			data=f.read(1024)
			clientsoc.send(data)
			
def download(filename,filesize,c,clientsoc):
	if c=='y':
		cnt=0	
		data=""	
		while(cnt<=(int(filesize))//1024):
			cnt+=1			
			data+=clientsoc.recv(1024)			
		f=open('new_'+filename,'wb')
		f.write(data)
		f.close()
		print 'Download complete'


clientsoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_addr='100.100.239.54'
port=12346
clientsoc.connect((IP_addr,port))
filesize=''

message=clientsoc.recv(1024)
print message
c=raw_input()
clientsoc.send(c)	

message=clientsoc.recv(1024)
print message
c=raw_input()
clientsoc.send(c)	

while True:
	message=clientsoc.recv(1024)
	
	if(message=='(u) for upload (d) for download (bye) for exit' or message=='(d) for download (bye) for exit'):
		print message
		c=raw_input()
		clientsoc.send(c)	

	elif(message=='bye'):
		clientsoc.close()
		break							

	elif(message[:6]=='exists'):
		filename=message[6:]
		#print filename

	elif(message[:8]=='filesize'):								
		filesize=message[8:]
		#print filesize		
	
	elif(message=='do you want to download (y/n)'):
		print message+' filesize : '+filesize
		c=raw_input()
		clientsoc.send(c)
		download(filename,filesize,c,clientsoc)
		
	elif(message[:6]=='upload'):
		upload(message[6:])
		print 'Upload complete'
			
	elif(message=='access granted' or message=='access denied' or message=='not found'):
		print message					
	
	elif(message=='Enter file path :'):
		print message
		c=raw_input()
		clientsoc.send(c)	

