def roll(a,b,c):
	if (a<b):
		print("Ist condition");
		return(a*b*c);
	elif (c<b):
		print("IInd condetion");
		return(a+b-c);
	else:
		print("rolling over");
		c=c-a+b;
		roll(a,b,c);