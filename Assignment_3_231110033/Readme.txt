Here are some instruction for running sbfl.Submission.py file

1. sbflSubmission.py file is inside Submission folder.

2. Open command promt or terminal inside ChironCore folder and write following command ,

           python ./chiron.py --SBFL ./example/p3.tl --buggy ./example/p3_buggy.tl -vars '[\":x\", \":y\", \":z\"]' --timeout 10 --ntests 20 --popsize 20 --cxpb 1.0 --mutpb 1.0 --ngen 20 --verbose True

3. 5 test cases are given inside example folder inside ChironCore folder

4. Output for each test case is ranklist of <example>_buggy.tl file which is generating inside <example>_buggy_componentranks.csv file 

5. 5 testcases ( examples ) are given which takes :x,:y, and :z as input.