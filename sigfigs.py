import numpy
import sys

si_prefixes = { -12:'p', -9:'n', -6:'u', -3:'m', 0:'', 3:'k', 6:'M', 9:'G', 12:'T', 15:'P' }

def format(value, prec, unit) :
    sign = numpy.sign(value)
    value = numpy.absolute(value)
    prec = numpy.absolute(prec)
    i_value = int(numpy.floor(numpy.log10(value)))
    i_prec =  int(numpy.floor(numpy.log10(prec)))
    sigfigs = 1 + i_value - i_prec
    log1000_value = i_value // 3
    log1000_rem = i_value % 3
    if log1000_rem > sigfigs - 1 :
        log1000_value += 1
        log1000_rem -= 3
    whole = log1000_rem + 1
    frac = sigfigs - whole
    if whole < 0 : whole = 0
    fmt = '%%%d.%df %s%s'%(whole,frac,si_prefixes[3*log1000_value],unit)
    print(i_value,i_prec,sigfigs,log1000_value,log1000_rem,fmt)
    return fmt%(value/numpy.power(1000.,log1000_value))

if '__main__' == __name__ :
    argv = sys.argv
    argc = len(argv)
    value = float(argv[1])
    prec = float(argv[2])
    unit = argv[3]
    print('result: %s'%(format(value,prec,unit)))
    
