# Vulnerabilites

## FTP - PORT 21
The File Transfer Protocol (FTP) is used for transferring files between hosts over a TCP-based network. 
The FTP service version was identified as VSFTPD 2.3.4, which has a known vulnerability: Backdoor Command Execution. 
This vulnerability was exploited, granting root privileges.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/a36916e6-bfc6-4bc7-b64d-ae02603e6147)


## TELNET - PORT 23
Telnet is a terminal emulation program used for logging into a remote host and facilitating terminal-to-terminal communication. 
A username and password were exposed on the website (via an open HTTP port), allowing remote access to the system by simply entering the credentials.
Command used: telnet 192.168.111.148
![image](https://github.com/user-attachments/assets/6ca1bddf-e13e-4fd5-a0f5-3f4c7ae4ff9c)


## SAMBA (SMB) - PORT 139, 445
Samba provides file sharing and printing services using the SMB protocol. 
The SMB service version was identified as smbd 3.0.20, which has a known vulnerability. 
The exploit exploit/multi/samba/usermap_script was used to gain root privileges.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/e2b1f1c1-3361-4a44-936e-3241088dfb2d)


## JAVA RMI SERVER - PORT 1099 (RMI Registry)
The Java RMI (Remote Method Invocation) registry was found to be vulnerable. 
The service version was exploited using the following Metasploit modules: auxiliary/scanner/misc/jmx_server and exploit/multi/misc/java_rmi. This led to gaining root privileges.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/37b8a362-facd-45c1-ac5e-2c341f723e0e)


## BIND SHELL - PORT 1524
This port is typically used for system administration, monitoring, performance management, and software updates. 
Simply listening to the IP address on port 1524 provided root access to the machine.
Command used: nc 192.168.111.148 1524
![image](https://github.com/user-attachments/assets/42c75d4d-a86b-44c7-8652-82a6fbe05804)


## HTTP - PORT 80
The HTTP (Hypertext Transfer Protocol) is used for sending and receiving unencrypted web messages. 
The open HTTP port revealed information about a PHP configuration file. 
This led to exploiting the PHP CGI Argument Injection vulnerability using exploit/multi/http/php_cgi_arg_injection, which granted Metasploit meterpreter PHP shell access.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/cc26f942-1afa-46b8-ab80-5bb10f9a0bc6)


## POSTGRESQL - PORT 5432
PostgreSQL is a database system used for client-server communication. 
A vulnerability was found in PostgreSQL versions 8.3.0 - 8.3.7. 
Using the Metasploit module exploit/postgres/postgres_payload, a PostgreSQL meterpreter shell was obtained.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/9626e5ba-8f6b-4731-b668-db392423fabb)


## IRC (UNREAL) - PORT 6667
IRC (Internet Relay Chat) provides chatroom-style communication over a network. 
The IRC Unreal service was vulnerable to Backdoor Command Execution. 
The Metasploit module exploit/unix/irc/unreal_ircd_3281_backdoor was used to gain root privileges.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/e5cfd3ad-71f7-47e9-9413-ef1fcdd98d3d)


## VNC - PORT 5900
Virtual Network Computing (VNC) allows for remote control of another machine. 
A vulnerability was discovered in VNC version 3.3, which was exploited using exploit/scanner/vnc/vnc_login. This provided root shell access to the machine.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/0aa4319b-b7be-4d3c-aa3b-ea8ac55c3c73)


## TOMCAT APACHE - PORT 8180
Tomcat Apache is used for deploying and running Java web applications. 
A vulnerability in this service was exploited using the multi/http/tomcat_mgr_upload module, resulting in a Tomcat meterpreter shell.
Tools used: Metasploit
![image](https://github.com/user-attachments/assets/0b770e2c-0679-40c8-9fdf-8e7498d7d587)


