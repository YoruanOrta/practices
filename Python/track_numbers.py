import phonenumbers
from phonenumbers import geocoder
phonenumber1 = phonenumbers.parse("+14155552671")
phonenumber2 = phonenumbers.parse("+919876543210")
phonenumber3 = phonenumbers.parse("+14155552671")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phonenumber1, "en"))
print(geocoder.description_for_number(phonenumber2, "en"))
print(geocoder.description_for_number(phonenumber3, "en"))
