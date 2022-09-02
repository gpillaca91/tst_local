from genericpath import exists
import json
json_str = '''
{
    "private_data": {
        "user_data": {
            "name": "Juan Perez",
            "email": "bepsaprueba2@gov.com",
            "address": "Asuncion",
            "order_description": "Bepsa Prueba",
            "identification_number": "00000000",
            "ip_terminal_client": "181.94.210.15"
        },
        "visa_3d_secure_data": {
            "cavv_verification_result":"",
            "eci_secure_3d_transactions": "05",
            "cavv_secure_3d_transactions": "0002010269210900000027106002007400000000"
        },
        "mastercard_3d_secure_data": {
            "sli_security_level_indicator": "",
            "aav_account_authentication_value": "",
            "program_protocol": "",
            "directory_server_transaction_id": ""
        }
    }
}
'''
data = json.loads(json_str)

name = (data['private_data']['user_data']['name'])
email = (data['private_data']['user_data']['email'])
address = (data['private_data']['user_data']['address'])
order_description = (data['private_data']['user_data']['order_description'])

eci_secure_3d_transactions = data['private_data']['visa_3d_secure_data']['eci_secure_3d_transactions']
cavv_verification_result = data['private_data']['visa_3d_secure_data']['cavv_verification_result']
cavv_secure_3d_transactions = data['private_data']['visa_3d_secure_data']['cavv_secure_3d_transactions']

sli_security_level_indicator = data['private_data']['mastercard_3d_secure_data']['sli_security_level_indicator']
aav_account_authentication_value = data['private_data']['mastercard_3d_secure_data']['aav_account_authentication_value']
program_protocol = data['private_data']['mastercard_3d_secure_data']['program_protocol']
directory_server_transaction_id = data['private_data']['mastercard_3d_secure_data']['directory_server_transaction_id']


field_58 = ''
visa_3d_secure_data  =''
mastercard_3d_secure_data = ''
#if cavv_verification_result!='' or additional_information_cavv!='' or cavv_secure_3d_transactions!='' :

if  cavv_verification_result!='':
    visa_3d_secure_data +='B110'+cavv_verification_result.rjust(10)

if  cavv_secure_3d_transactions!='' or eci_secure_3d_transactions!='':
    visa_3d_secure_data += 'B202'+eci_secure_3d_transactions.rjust(2)
    visa_3d_secure_data += 'B340'+cavv_secure_3d_transactions.rjust(40)
                        
if sli_security_level_indicator!='' or aav_account_authentication_value!='' or program_protocol!='' or directory_server_transaction_id!='':
    mastercard_3d_secure_data += 'C119'+sli_security_level_indicator.rjust(19)+'C232'
    mastercard_3d_secure_data+=aav_account_authentication_value.rjust(32)+'C301'
    mastercard_3d_secure_data+=program_protocol.rjust(1)+'C436'
    mastercard_3d_secure_data+=directory_server_transaction_id.rjust(36)


user_data = 'A180' + name.rjust(80)+'A250' +\
            email.rjust(50)+'A350' +\
            address.rjust(50)+'A430' +\
            order_description.rjust(30)+'A515' +\
            data['private_data']['user_data']['identification_number'].rjust(15)+'A615' +\
            data['private_data']['user_data']['ip_terminal_client'].rjust(15)+\
            visa_3d_secure_data +\
            mastercard_3d_secure_data
     
field_58 += user_data
print(field_58)