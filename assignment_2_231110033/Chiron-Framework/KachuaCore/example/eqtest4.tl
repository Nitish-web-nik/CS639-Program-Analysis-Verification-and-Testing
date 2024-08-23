:y = :x
if :x <= 42 [
   :y = :y + 40
   if :x<=30[
    :y=:y+50
   ]
   else[
    :y=:y+90
   ]
   
] else [
   :y = :y + 22
]