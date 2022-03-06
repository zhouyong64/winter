import os,sys

def get_info(idd,idx):
    m = '| idx <audio src="vc/src/ID.wav" controls preload></audio> | idx <audio src="vc/ref/ID.wav" controls preload></audio> | idx resultA <audio src="vc/res1/ID.wav" controls preload></audio> | idx resultB <audio src="vc/res2/ID.wav" controls preload></audio> | idx resultC <audio src="vc/res3/ID.wav" controls preload></audio> |'
    return m.replace('ID', idd).replace('idx', idx)

print(get_info(sys.argv[1], sys.argv[2]))
