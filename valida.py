
from validate_email import validate_email

email_from="dagarnue@teleco.upv.es"
print("Introduzca un email para comprobar si es correto")
email_to=input("Destinatario: ")
es_valido=validate_email(email_to,check_regex=True,
check_mx=False, from_address=email_from)
while (es_valido==False):
    #La direccion de correo es incorrecta
    print("Introduzca la direccion de destino de nuevo.")
    email_to=input("Destinatario: ")
    es_valido=validate_email(email_to,check_regex=True,check_mx=False,from_address=email_from)