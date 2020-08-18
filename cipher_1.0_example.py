def find_in_list(query, mainlist):
    mainlist_len = len(chars)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
            break
    return (i)
chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# print(find_in_list(query, mainlist))
# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
            # print(encrypted_msg)
        else:
            encrypted_msg = encrypted_msg + character
    print(encrypted_msg)
# print(encrypt_message(encrypt_message))
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
            # print(decrypted_msg)
        else:
            decrypted_msg = decrypted_msg + character
    print(decrypted_msg)
# print(decrypt_message(decrypted_msg))
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice =='e':
        plain_message = input("Enter message to encrypt??")
        encrypt_message(plain_message)
        # print(encrypted_msg)
    else: 
        choice == 'd'
        encrypted_msg = input("Enter message to decrypt?")
        decrypt_message(encrypted_msg)
        # print(decrypted_msg)
    # else:
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        print("shnati")
    elif play_again == 'N':
        break
