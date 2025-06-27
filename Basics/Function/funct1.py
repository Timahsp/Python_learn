def first():
    def second():
        return "inside function"
    return second

print(first()())
callinner = first()
print(callinner())