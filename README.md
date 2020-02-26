ROLE BASED FTP

This project is implemented in python2 virtual environment.

Introduction

As the name suggest the project chosen as a term assignment for the course of
Computer Network is Role Based FTP. Now, the question arises that what is a Role
Based FTP and how is it different from a simple FTP ? Answer to the question is
that a simple FTP consist of a server and a client where the client can upload or
download files from the server , whereas a Role Based FTP consists of some
additional functionalities like,
• Username and Password login
• Accessing files from different part of the Server
• Checking the availability of the file at the given location
• Priviledges required for accessing the files


Technical Details

You may wonder that this is just the definition but how it can be implemented ? So
before going into the implementation and functionality let us discuss the Technical
details of the Project. This project consists of a centralized FTP server that works
on TCP/IP protocol which contains all the access information and the files that are
to be shared with the clients. The connection between the server and the client is a
multi-threaded connection, that is multiple clients can be connected with the server
at the same time. File transfer here is possible for the systems in same network. In
this project the binary 0’s and 1’s are read from the file and they are transferred
from the server to the client in chunks of 1024 bytes. Since read binary is used at
the server and and write binary is used at the client end to create a new file thus
files like .txt, .JPEG, .mp3 etc, can be transferred using this model.


Implementation

Let us now jump onto the Implementation :
The server end starts by assigning it a socket and binding it to a port and ip there
after it waits for the clients whenever a client arrives client thread is initiated.the
client thread is the main part of the program from here the client is asked to enter
username and password which are than compared with the dictionaries maintained
at the server there are two dictionaries which contain username and password and
the piviledge is granted as per the username and password.The download function sends the data to the client and the upload function recieves
data from client. There are other function for checking access and finding the
filename from the user given path.
The client end consist of a set of recieve statement and instruction on what is to be
done when a particular message is received. It also has a download function for
receiving the data and upload function foe sending the data.


Functionalities

The Functionalities include :
• Username and Password : Here predefined Username and corresponding
password are stored in a dictionary and whenever correct username and
password is typed user is given access to upload or download based on the
privilege.
• Along with file transfer from the default directory (folder where the program is
placed) at the server user can also give the path along with the name of the
file that he wants to access and the response will be send to him as per his
privilege.
• Privilege : There are two dictionaries called ‘boss’ and ‘employee’. When
username and password of boss match user has download and upload
writes both and an access to download the files from any directory in the
server. But in case of employee it has only download write and it can
download files from only a few directories within the server.



Common Difficulties

Difficulties one may face while making a Role Based FTP :
After the file transfer is completed the socket has to be emptied so that the
subsequent message is not appended into the file. This error can be solved by
waiting for the socket to get empty OR sending some marker after the file to detect
the transfer is over at client OR to carry out file transfer from different socket.
Another one is that how should one send data. The answer to this is that is that one
can either keep on sending the data till the file is empty and keep on receving data
till null is recieved OR we can count the number of statements to be send and place
same number of recieve statement at the reciever end. The second one works
better out of the two.


Conclusion

Nowadays FTP is used in large companies and even in universities, for quick file
transfer between end-systems in same network or different local networks. It
consists of a centralized server and multiple clients that can connect to the server
and can download and upload files. The main advantage is that the file transfer
occurs over wired media locally and thus whenever a file is need the access link
need not be burdened.The project helped learn the technicalities of the services
that we use in our day-to-day life.