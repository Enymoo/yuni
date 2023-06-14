class User:

    def __init__(self, userid, balance, color):
        if not isinstance(userid, int):
            raise TypeError("userid must be an integer")
        if not isinstance(balance, int):
            raise TypeError("balance must be an integer")
        if not isinstance(color, str) and len(color) == 7:
            raise TypeError("color must be a string and have a length of 7")
        self.userid = userid
        self.balance = balance
        self.color = color
        