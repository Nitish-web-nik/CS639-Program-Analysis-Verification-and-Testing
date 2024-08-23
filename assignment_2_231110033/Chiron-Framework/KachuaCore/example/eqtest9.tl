:y = :x
if :x <= 42 [
   :y = :y + :c1
   if :x <= 30 [
      :y = :y + :c2
   ] else [
      :y = :y + :c1 + :c2
      if :x >= 35 [ 
         :y = :y - :c2
      ]
   ]
] else [
   :y = :y + 22
]