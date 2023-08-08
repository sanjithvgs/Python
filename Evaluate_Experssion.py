def evalRPN(A):
      if len(A) == 1:
          return A[0]
      operator = ['*', '+', '-', '/']
      mstack = []
      for item in A:
          if item not in operator:
              mstack.append(item)
          else:
              if (len(mstack) < 2):
                  return -1
              op2 = mstack.pop()
              op1 = mstack.pop()
              res = eval(op1 + item + op2)
              mstack.append(str(res))

      return int(res)

A =   ["2", "1", "+", "3", "*"]
print(evalRPN(A))

# output:
# 9

# starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9