from dataclasses import dataclass # importing dataclass decorator

@dataclass # auto generating constructor and other methods
class User:
    UserID: int
    UserName: str
    Email: str  
    PassWord: str
    Role: str
    Status: bool

    def login(self, Email: str, PassWord: str)-> bool:
        return self.Email == Email and self.PassWord == PassWord and self.Status
    
    def logout(self) -> None:
        pass
    
    def reset_PassWord(self, new_PassWord: str) -> None:
        self.PassWord = new_PassWord