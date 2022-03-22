class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx<tx and sy<ty:
            if tx<ty:
                ty=ty%tx
            else:
                tx=tx%ty
        return((sy==ty and sx<=tx and (tx-sx)%sy==0) or (sx==tx and sy<=ty and (ty-sy)%sx==0))
        
