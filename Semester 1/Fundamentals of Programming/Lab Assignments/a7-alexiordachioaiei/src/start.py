"""
Starting main function
My problems: 2
"""

"""
    - it creates objects for Repo, Service and UI
    Repo - change this object to change the repo type
    
    Domain Entity - __init__
    Services
        - code that implements the functionalities [add, filter, undo, get all]
    
    Repository 
        - code that changes the list
        - read/write to file: add, remove, .., get all elems, binary, idk
    
    UI -> SERVICE -> REPOSITORY -> READ/WRITE TO FILE
    That's what each of them has access to
    
    Tests and Specifications 
        - for all NonUI functions (methods) related to add
        - for Service/Repo/Domain, each of them has a different add
            - Domain: test object creation
            
    Generate 10 random objects at the start
        - generate only if the list is empty 
            - If we have some objects that we save to a file, then we will have those when we start the application again, so no need to generate 10 more
"""

from ui.UI import UI

if __name__ == "__main__":
    UI = UI()
    UI.menu()