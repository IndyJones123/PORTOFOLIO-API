from MainModuleADM.Encryption.aes import i_encrypt

user="postgres.dzdzosoalcujtcjdcazo "
password="iDp8n9Dtkj07Txmj"
host="aws-0-ap-southeast-1.pooler.supabase.com"
port=5432
dbname="postgres"

user_encrypt = i_encrypt('WKbWo%Grj)C6YhAq',user)
user_password = i_encrypt('WKbWo%Grj)C6YhAq',password)
user_host = i_encrypt('WKbWo%Grj)C6YhAq',host)
user_dbname = i_encrypt('WKbWo%Grj)C6YhAq',dbname)

print(user_encrypt)
print(user_password)
print(user_host)
print(user_dbname)