import matplotlib
import matplotlib.pyplot as plt

def afficheResult(file, angle_or_duration=0):
    num,time,angle,duration,errorX,errorY=[],[],[],[],[],[]
    with open(file, 'r') as f:
        ligne = f.readline()
        ligne = f.readline()
        while(ligne):
            #ligne = f.readline()
            n,t,a,d,eX,eY=ligne.split(';')
            num.append(int(n))
            time.append(float(t))
            duration.append(float(d))
            angle.append(float(a))
            errorX.append(float(eX))
            errorY.append(float(eY)*float(eY))
            ligne=f.readline()
            
    data = [num,time,angle,duration,errorX,errorY]
    data = sorted(zip(*data), key=lambda args: args[2+angle_or_duration])
    data = list(zip(*data))
    
    plt.plot(data[2+angle_or_duration],errorY,"g+")
    plt.xlabel(("angle", "duration")[angle_or_duration])
    plt.ylabel("errorY^2")
    plt.show()
    