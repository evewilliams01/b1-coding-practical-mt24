
def pd_controller(reference, depth, e_tminus1, Kp=0.15, Kd=0.6):
    # PD controller for UUV
    
    #Calc error at current time step
    e_t = float(reference) - float(depth)
    u_t = float(Kp) * float(e_t) + float(Kd)*(float(e_t) - float(e_tminus1))
    return e_t, u_t