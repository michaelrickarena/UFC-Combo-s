import itertools
import csv

def comb1(k, available, used):
	if len(used)==k: #hits the required number of units in a combo
		yield tuple(used)
	elif len(available)==0: # went through all avaliable and has none left over
		pass
	else:
		head=available.pop(0)
		used.append(head)
		for c in comb1(k, available[:], used[:]):
			yield c
		used.pop()
		for c in comb1(k, available[:], used[:]):
			yield c

def comb_wrapper(k,s,n):
	for c in comb1(k,list(s),[]):
		if sum(s[i] for i in c) == n:
			yield c



s={'Valentina Shevchenko (12758262)':9600,'Tatiana Suarez (12758264)':9500,'Petr Yan (12758274)':9300,'Yan Xiaonan (12758272)':9100,'Bevon Lewis (12758284)':9000,'Calvin Kattar (12758276)':8800,'Tai Tuivasa (12758268)':8700,'Tony Ferguson (12758286)':8600,'Aljamain Sterling (12758280)':8500,'Karolina Kowalkiewicz (12758278)':8400,'Marlon Moraes (12758270)':8300,'Eddie Wineland (12758282)':8200,'Joanne Calderwood (12758266)':8100,'Katlyn Chookagian (12758267)':8100,'Grigorii Popov (12758283)':8000,'Henry Cejudo (12758271)':7900,'Alexa Grasso (12758279)':7800,'Pedro Munhoz (12758281)':7700,'Donald Cerrone (12758287)':7600,'Blagoy Ivanov (12758269)':7500,'Ricardo Lamas (12758277)':7400,'Darren Stewart (12758285)':7200,'Angela Hill (12758273)':7100,'Jimmie Rivera (12758275)':6900,'Nina Ansaroff (12758265)':6700,'Jessica Eye (12758263)':6600}
k=6
mycombs=list(comb_wrapper(k, s, 49800))



#Put in Excel
with open('Cejudo_vs_Moraes.csv', 'w', newline='') as f:
	thewriter=csv.writer(f)
	thewriter.writerow(['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6'])
	for comb in mycombs:
		thewriter.writerow(comb)