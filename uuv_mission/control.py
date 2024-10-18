
def pd_controller(r,y,Kp=0.15,Kd=0.6)
#PD controller for UUV

#Initialise list of zeros for control action
    u = [0]*len(r) 

    for t in range(1,len(r)):
        #Calc error at current and previous time steps
        e_t = r[t] - y[t]
        e_tminus1 = r[t-1]-y[t-1]

        u[t] = Kp * e_t + Kd*(e_t - e_tminus1)
    return u