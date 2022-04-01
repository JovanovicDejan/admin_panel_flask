class Employee:
    __id:int
    __firstName:str
    __lastName:str
    __order:int
    __linkedIn:str
    __xing:str
    __role:str
    __email:str
    __photoUrl:str

    def __init__(self,id:int, firstName:str,lastName:str,order:int,linkedIn:str,xing:str,role:str,email:str,photoUrl:str):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__order = order
        self.__linkedIn = linkedIn
        self.__xing = xing
        self.__role = role
        self.__email = email
        self.__photoUrl = photoUrl
    
    def get_id(self):
        return self.__id

    def get_firstName(self):
        return self.__firstName
    
    def get_lastName(self):
        return self.__lastName
    
    def get_order(self):
        return self.__order
    
    def get_linkedIn(self):
        return self.__linkedIn
    
    def get_xing(self):
        return self.__xing
    
    def get_role(self):
        return self.__role
    
    def get_email(self):
        return self.__email
    
    def get_pohotUrl(self):
        return self.__photoUrl

    
    def set_id(self,new_id):
        self.__id = new_id

    def set_firstName(self,new_name):
        self.__firstName  = new_name
    
    def set_lastName(self,new_lastName):
        self.__lastName = new_lastName
    
    def set_order(self,new_order):
        self.__order = new_order
    
    def set_linkedIn(self,new_linkedIn):
        self.__linkedIn = new_linkedIn
    
    def set_xing(self, new_xing):
        self.__xing = new_xing
    
    def set_role(self,new_role):
        self.__role = new_role
    
    def set_email(self,new_email):
        self.__email = new_email
    
    def set_pohotUrl(self,new_photoUrl):
        self.__photoUrl = new_photoUrl
    
    
    def __str__(self) -> str:
        res = f"ID: {self.__id} \n"
        res += f"First name: {self.__firstName} \n"
        res += f"Last name: {self.__lastName} \n"
        res += f"Order: {self.__order} \n"
        res += f"LinkedIn: {self.__linkedIn} \n"
        res += f"Xing: {self.__xing} \n"
        res += f"Role: {self.__role} \n"
        res += f"Email: {self.__email} \n"
        res += f"PhotoUrl: {self.__photoUrl} \n"
        return res