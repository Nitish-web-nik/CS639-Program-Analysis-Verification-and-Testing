This explains a simple example of adding  `goto` command in Kachua language. However adding any new command should follow these steps only.

**1. Adding new grammar rule in `tlang.g4`**

 - The grammar rules are defined in `KachuaCore/parser/tlang.g4`

 - Since we are adding a new Command/Instruction. we should add it under the `instruction` rule in the grammar.

    - ```antlr4
      instruction : assignment                                                                                 
                  | conditional                                                                                
                  | loop                                                                                       
                  | moveCommand                                                                                
                  | penCommand                                                                                 
                  | gotoCommand  // <--- new command added --->
                  ;
                  
      gotoCommand : 'goto' '(' expression ',' expression ')'; // <--- goto command rule --->
      ```

 - Next step, is to regenerate antlr4 parser code. Execute the following command from `parser` directory.

    - ```bash
      java -cp ../extlib/antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener  tlang.g4
      ```



**2. Create a python class for `goto` command in `KachuaCore/ast/kachuaAST.py`**

- ```python
  class GotoCommand(Instruction):
      def __init__(self, x, y):
          self.xcor = x
          self.ycor = y
  
      def __str__(self):
          return "goto " + str(self.xcor) + " " + str(self.ycor)
  ```

  - You must implement `__str__` , this is used by IR pretty print and sometimes by Kachua interpreter.



**3. Adding visitor for the new parse tree nodes**

- antlr4 generates visitors for parse tree nodes which we can override to create corresponding objects in the `kachuaAST.py`

- The file `KachuaCore/parser/tlangVisitor.py` has a base visitor class which is inherited by `astGenPass` in `KachuaCore/ast/builder.py`

- For our implementation we need to override `visitGotoCommand` in `KachuaCore/parser/tlangVisitor.py`. Following is the visitor definition we want to add to `astGenPass` in `KachuaCore/ast/builder.py`. This will create a `kachuaAST.GotoCommand` object which will be added to the IR.

  - ```python
    def visitGotoCommand(self, ctx: tlangParser.GotoCommandContext):
        xcor = self.visit(ctx.expression(0))
        ycor = self.visit(ctx.expression(1))
        return [(kachuaAST.GotoCommand(xcor, ycor), 1)]
    ```
 - Ref. https://sourcemaking.com/design_patterns/visitor to understand the visitor design pattern

