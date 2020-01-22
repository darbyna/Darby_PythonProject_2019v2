#Sample test -- base model for functions

def test_code(): 
    try: 
        sample = input("Hello")
        if sample == "Bob":
            print("Hello Bob")
            assert (sample == "Bob") == True
        if sample == "Jill":
            print("Hello Jill")
            assert (sample == "Jill") == True
    except:
        return ("Hello nothing")
    