# Creating Functions That Call And Modify That Function And Add Extra In It
#Stil I'm Not Understand Use Of It LOL 
# It Can used to give access only if user is login

def anounce(f):
    def wraper():
        print("This Is Function")
        f()
        print("Done With Function")
    return wraper

@anounce
def hello():
    print("Hello")

hello()
