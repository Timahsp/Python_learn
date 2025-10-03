def first():
    def second():
        return "inside function"
    return second

#call the inner fucntion by chain method
print(first()())

# or call it by creating an object callinner and then calling it
callinner = first()
print(callinner())