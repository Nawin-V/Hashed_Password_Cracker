import hashlib

tool_name = "************HASHED PASSWORD CRACKER************"
creator_name = "******CREATOR NAME : NAWIN******"

print(tool_name)
print(creator_name)

pass_found = 0

input_hash = input("Enter the hashed password: ")

pass_doc = input("\nEnter passwords filename including path(/home/lucifer/PY-Tools/Pass_Hash/): ")

try:
    pass_file = open(pass_doc, 'r')
except FileNotFoundError:
    print("Error:")
    print(pass_doc, "is not found.\nPlease give the correct path of the file.")
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')

    hash_word = hashlib.md5(enc_word.strip())

    digest = hash_word.hexdigest()

    if digest == input_hash:
        print("Password found.\nThe password is:", word)
        pass_found = 1
        break

if not pass_found:
    print("Password is not found in the", pass_doc, "file")
    print('\n')
