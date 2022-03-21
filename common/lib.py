import re
from email_validator import validate_email, EmailNotValidError

class Validator:    
    def __init__(self, email: str):
        self.__regex = '^([A-Za-z0-9]+[.-_]+&)*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$'
        self.email: str = email
        self.__divide_email: list = self.email.split("@")
        self.__divide_email_domain: list = []
        self.__special_characters: str = "!#$%&'*+-/?^_{|"
        self.__allowed_letter_domain: list = ['g', 'y', 'r']
        self.__allowed_workspace_domain: list = ['cjc', 'ppl', 'prs']
        self.__allowed_domain: list = ['com', 'net', 'org', 'edu']
        self.__allowed_country_domain: list = ['ph', 'us', 'fr', 'esp']
        self.__result: bool = False

    def divide_email(self):
        self.__divide_email_domain: list = self.__divide_email[1].split(".")
        if len(self.__divide_email_domain) == 2:
           self.__result = True
        return self.__result

    def full_match(self)-> bool:
        if(re.fullmatch(self.__regex, self.email)):
           self.__result = True
        return self.__result

    def validate_email_vwp(self) -> bool:                
        try:            
            divide_email: list = self.email.split("@")
            if len(divide_email[0]) > 3 and len(divide_email[1]) > 3:
                if "." in self.email and "@" in self.email:
                    number_of_astricks = self.email.count('@')
                    number_of_periods = self.email.count('.')
                    domain = self.email[-3:]
                    allowed_domain = ['com', 'net', 'org']
                    if  '@' not in self.email \
                        or '.' not in self.email \
                        or number_of_astricks != 1 \
                        or number_of_periods < 1 \
                        or domain not in allowed_domain \
                        or " " in self.email:
                        return self.__result
                    else:
                        special_character = "!#$%&'*+-/?^_{|."
                        index_of_astrick = self.email.index('@')
                        name = self.email[:index_of_astrick]
                        if self.email[0] in special_character or self.email[index_of_astrick-1] in special_character:
                            return self.__result
                        elif len(name) > 64:
                            return self.__result
                        else:
                            self.__result = True
                else:
                    return self.__result
        except Exception as error:
            print(f"Error->validate_email_vwp(): {error}")
        return self.__result

    def validate_email_package(self) -> bool:
        try:            
            valid = validate_email(self.email)                        
            self.__result = True
        except EmailNotValidError as error:            
            print(f"Error->validate_email_vwp(): {error}")
        return self.__result

    def validate_email(self) -> bool:       
        try:
            if self.divide_email(): 
                if(self.email != '' or "@" in self.email or "." in self.email):
                    if(self.email.count('@') == 1):
                        if((len(self.__divide_email[0]) >= 3 and len(self.__divide_email[0]) <= 15) and 
                        (len(self.__divide_email[1]) >= 3 and len(self.__divide_email[0]) <= 15)):
                            for char in self.__divide_email[0]:
                                if(char in self.__special_characters):
                                    return self.__result
                            if(self.__divide_email[1].count('.') == 1 ):
                                if(self.__divide_email_domain[1] in self.__allowed_domain):                                
                                    self.__result = True                            
                            elif(self.__divide_email[1].count('.') == 3):
                                if  (self.__divide_email_domain[0] not in self.__allowed_letter_domain) or \
                                    (self.__divide_email_domain[1] not in self.__allowed_workspace_domain) or \
                                    (self.__divide_email_domain[2] not in self.__allowed_domain):
                                    return self.__result
                                elif(self.__divide_email_domain[3] in self.__allowed_country_domain):                                
                                    self.__result = True                            
        except Exception as error:
                print(f"Error from -> validate_email(): {error}")
        return self.__result