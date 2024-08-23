# 🚀 CS639 - Program, Verification, Analysis, and Testing 🧪

Welcome to the world of Program Analysis, where bugs fear to tread, and code gets the scrutiny it deserves! This README will guide you through the various assignments I've tackled, sprinkled with some humor and practical tips. Grab your coffee, let's dive in!

---

## 📝 Assignment 1: Program Analysis Verification and Testing

### Location of Examples:
You'll find my 5 brilliant examples nestled in the `Chiron-Framework\KachuaCore\example` directory, all in the glorious `.tl` format.

### How to Run (Windows x64):
1. **Step into the Matrix (or Command Prompt):**
   - Open CMD and navigate to the `KachuaCore` directory.
   - Run the command:
     ```bash
     python ./kachua.py -r -t 60 -d {':x':30,':y':3,':z':7} --fuzz tests/<example_name>.tl
     ```

2. **For the Bash Ninjas:**
   - Open your terminal and execute:
     ```bash
     ./kachua.py -r -t 60 -d {':x':0,':y':89,':z':69} --fuzz tests/<example_name>.tl
     ```

### A Little Tip:
Feel free to get creative with the input values! Whether you’re more of a `:x=42` kind of person or prefer `:z=7` for some lucky debugging, the choice is yours.

---

## 🤔 Assignment 2: Program Synthesis using Symbolic Execution

### Test Cases Galore:
Check out my 10 test cases in the `assignment_2_231110033\Chiron-Framework\KachuaCore\example` folder.

### How to Run:

1. **Step i: Unzip the Magic:**
   - Extract the `Assignment_2_231110033` folder.
   
2. **Step ii: Dive into Code Editor:**
   - Change your directory to `assignment_2_231110033\Chiron-Framework\Submission`.
   - Run the script:
     ```bash
     python symbSubmission.py -b optimized1.kw -e '["x","y"]'
     ```
   - **Default behavior:** Runs with `testfile3` and `testfile4`. (Spoiler: They pass with flying colors! 😎)

3. **Want to Switch It Up?**
   - Modify `symbSubmission.py` on lines 32 and 36 to switch test files. Go ahead, make `testfile2` feel included!

### Outputs:
All the output files are lounging comfortably in `assignment_2_231110033\Chiron-Framework\outputs of each test case of tl file`.

### Running `sbflSubmission.py`:
1. **Locate the File:**
   - It's chilling inside the `Submission` folder.
   
2. **Execute the Magic:**
   - In the `ChironCore` directory, run:
     ```bash
     python ./chiron.py --SBFL ./example/p3.tl --buggy ./example/p3_buggy.tl -vars '["x", "y", "z"]' --timeout 10 --ntests 20 --popsize 20 --cxpb 1.0 --mutpb 1.0 --ngen 20 --verbose True
     ```

3. **Test Cases:**
   - Located in the `example` folder with inputs for `:x`, `:y`, and `:z`.

4. **Output:**
   - Generated as `<example>_buggy_componentranks.csv`. Just think of it as your buggy code getting a report card! 📈

---

## 🔍 Assignment 4: Program Analysis Verification and Testing

### (a) Example Locations:
Check out my 5 top-tier examples in `assignment_4_231110033\Chiron-Framework\KachuaCore\tests`, complete with their JSON sidekicks.

### (b) Output Location:
All outputs are safely stored in `assignment_4_231110033\Chiron-Framework`.

### (c) Code Implementation:
All required functions are packed into `assignment_4_231110033\Chiron-Framework\Submission\submissionAI.py`.

### How to Run:

1. **Step i: Download the Zip:**
   - Unzip `Assignment_4_231110033`.

2. **Step ii: Open in a Code Editor:**
   - Visual Studio Code works like a charm! 🛠️

3. **Step iii: Terminal Adventures:**
   - Navigate to `\Chiron-Framework\KachuaCore`.
   - Run the following commands for examples 1 to 4:
     ```bash
     python kachua.py -ai example/<example_name>.tl
     ```

4. **Special Treatment for Example 5:**
   - Since this one’s a bit fancier, run:
     ```bash
     python kachua.py -d '{":a": 5}' -ai example/example_5.tl
     ```

---

That's it! You've now got the full scoop on how to navigate through these assignments like a pro. Remember, debugging is just another way of showing how much you care about your code. Happy coding! 😄
