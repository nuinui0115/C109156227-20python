a=int(input(""))
if a<=120:
    print("Summer-months:",a*2.1)
    print("Non-Summer-months:",a*2.1)
if a>=121 and a<=330:
    print("Summer-months:",120*2.10+3.02*(a-120))
    print("Non-Summer-months:",120*2.10+2.68*(a-120))
if (a>=331 and a<=500):
    print("Summer-months:",120*2.10+3.02*210+4.39*(a-120-210))
    print("Non-Summer-months:",120*2.10+2.68*210+3.61*(a-120-210))
if a>=501 and a<=700:
    print("Summer-months:",120*2.10+3.02*210+4.39*170+4.97*(a-120-210-170))
    print("Non-Summer-months:",120*2.10+2.68*210+3.61*170+4.01*(a-120-210-170))
if a>=701:
    print("Summer-months:",120*2.10+3.02*210+4.39*170+5.44*200+5.36*(a-120-210-170-200))
    print("Non-Summer-months:",120*2.10+3.02*210+3.61*170+4.48*200+4.50*(a-120-210-170-200))
