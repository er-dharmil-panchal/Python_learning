#==========================================================================================================
#==========================================================================================================
#------->>>>>>>                                Break & Continue                            <<<<<<---------
#==========================================================================================================
#==========================================================================================================



'''
    Break:- Use to end loop ;
    Continue:- Use to skip a part from loop and continue the loop ;
'''

#---->                                       👉🏻BREAK👈🏻


for i in range(15):
    print("5 X ",i+1,"=",5*(i+1))

     #IF I WANT TO STOP THIS LOOP ON 10 ;

    if(i == 10):
        print("Breaking Out Of The Loop")
        break 
     #NOTE But 11 is printing because of 'i+1' , because i start with '0' ;

print("\n\n")

for i in range(15):
    if(i == 10):
        print("Breaking Out Of The Loop")
        break
    print("5 X",i+1,"=",5*(i+1))
print("\n\n")

#NOTE Observe the diffrence in Upper two codes and their result ;


#---->                                       👉🏻CONTINUE👈🏻

for i in range(15):
    if(i==10):
        print("Skip")
        continue
    print(i)

     # 10 will not print ;
    
