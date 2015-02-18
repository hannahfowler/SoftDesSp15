def is_excited(s): 
	capitals = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
	for c in s:
		if c == '!' or c in capitals:
			return True
		else:
			return False
print is_excited('Hi')