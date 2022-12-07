#Function named days_in_feb()

def days_in_feb(user_year):    
    if(user_year % 4 == 0):                
        if(user_year % 100 == 0):                                                
            if(user_year % 400 == 0):                
                days = 29                                
            else:
                days = 28        
        else:            
            days = 29    
    else:        
        days = 28        
    return days        
if __name__=="__main__":    
    user_year = int(input())    
    print(user_year,"has",days_in_feb(user_year),"days in February.")