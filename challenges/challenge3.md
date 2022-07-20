# Breaking a real PQC implementation. How to be a crypto analyst

PQFTP is a post quantum file transfer program. It consists of a client and a server binary. A real Kyber KEM implementation is established and used to transmit an AES key.
You are being provided with both binaries as well as a pcap capture of PQFTP in operation. 

PQFTP binaries provided are x86-64 compiled Ubuntu binaries that should run on a recent Ubuntu install.

## Challenge objective

The goal is to decrypt the traffic and return decrypted secret contents of the encrypted files transferred.
To evaluate your solution the decrypted secret contents need to send us to __ctf-rwpqc2024@sandboxaq.com__ with the subject "Challenge1".

Hint: To do this, reverse engineer the binary to find a cryptographic bug, and then using this knowledge write a program using libOQS library and any other necessary libraries to decrypt the network traffic in the pcap file.


## PQFTP Usage - PostQuantum File Transfer protocol

./ctf_server <PORT optional, defaults to 1337>

./ctf_client <NS1|NS3|NS5> <VERB> <IP optional> <PORT optional>

For example: ./ctf_client NS1 PUT abc.txt

./ctf_client 

Usage: ./ctf_client NS_LEVEL VERB <PATH/FILE> <IP> <PORT> : ip and port optional, default 1337

Supported verbs: 

         PUT <file> : upload file
         
         GET <file> : download file
         
         DIR <path> : do a directory listing (set to . to do cwd)
         
         DIS : disconnect ---> not currently implemented
        
        NS1 : keypair at Kyber512 (Nist Security Level 1)
        
        NS3 : keypair at Kyber768 (NIST Security Level 3)
        
        NS5 : keypair at Kyber1024 (NIST Security Level 5)


Extra information:

         PQFTP Protocol Description (Provide as additional help if necessary)

         Server hosts, client connects. Default port is 1337.

         Client sends ASCII string NS1, NS3, or NS5 corresponding to NIST Security level for Kyber.

         Server responds with public key of appropriate size.

         Client sends cipher text of appropriate size.

         Server decapsulates shared secret from cipher text.

         At this point, an AES ECB tunnel is established. 

         All messages from this point will be AES_ECB encrypted in exactly 16 byte blocks, with unused bytes in a 16 byte block set to 0. 
         While the protocol will be described in ASCII / plaintext below, all following operations need to be AES ECB encrypted / decrypted.

         The client can send one of 3 messages, "PUT", "GET", or "DIR". All of these will be followed by a filename, then a new AES block containing "END".

         After a PUT command, the client will begin sending file data. After the end of data, a new block containing "END" is sent.

         After a GET command, the server will begin sending file data. After the end of data, a new block containing "END" is sent.

         After a DIR command, the server will begin sending a new line separated directory listing. After the end of data, a new block containing "END" is sent.
         On errors, the server may send "ERR" as a response.

## References

https://github.com/open-quantum-safe/liboqs
