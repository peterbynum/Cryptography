"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

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


while on:
    input = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if input == 'e':
        m = input("Message: ")
        k = input("Key: ")
        
    elif input == 'd':
        m = input("Message: ")
        k = input("Key: ")
        
    elif input == 'q':
        on = False    
    else:
        print("Did not understand command, try again.")
