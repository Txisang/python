def move(n,fromo,buffer,to):
    if n==1:
        print('Move',n,'from',fromo,'to',to)
    else:
        move(n-1,fromo,to,buffer)
        move(1,fromo,buffer,to)
        move(n-1,buffer,fromo,to)


move(3, 'A', 'B', 'C')

#    要从a到b 那c就是缓冲 move(n-1,from,to,buffer) 
#   要从a到c 那b就是缓冲 move(1,from,buffer,to)     
#    要从b到c 那a就是缓冲 move(n-1,buffer,from,to) 



if s[0]=' '
	s=s[]
return s

