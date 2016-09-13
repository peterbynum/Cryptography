"""
cryptography.py
Author: Peter Bynum
Credit: How to count characters in a list: http://stackoverflow.com/questions/25934586/finding-the-amount-of-characters-of-all-words-in-a-list-in-python
Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
on = True
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
# make list of numbers for message and key
# add them while compiling a new list
# print new string



while on:
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command == 'e':
        m = input("Message: ")
        k = input("Key: ")
        mlist = []
        klist = []
        encryptionlist = []
        encryption = []
        
        
        for i in range(0,len(m)):
            mlist.append(associations.find(m[i]))# creates mlist
        for i in range(0,len(k)):
            klist.append(associations.find(k[i]))# creates klist
        for i in range(0,len(mlist)):#creates encryptionlist
            encryptionlist.append(mlist[i]+klist[i%len(klist)])
        for i in range(0,len(encryptionlist)):
            encryption.append(associations[encryptionlist[i]%len(associations)])
        print(''.join(encryption))
        
    elif command == 'd':
        m = input("Message: ")
        k = input("Key: ")
        mlist = []
        klist = []
        decryptionlist = []
        decryption = []
        
        
        for i in range(0,len(m)):
            mlist.append(associations.find(m[i]))# creates mlist
        for i in range(0,len(k)):
            klist.append(associations.find(k[i]))# creates klist
        for i in range(0,len(mlist)):#creates decryptionlist
            decryptionlist.append(mlist[i]-klist[i%len(klist)])
        for i in range(0,len(decryptionlist)):
            decryption.append(associations[decryptionlist[i]%len(associations)])
        print(''.join(decryption))
        
        
    elif command == 'q':
        print('Goodbye!')
        on = False    
    else:
        print("Did not understand command, try again.")
