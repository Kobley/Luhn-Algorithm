from luhnutils.luhn import LuhnUtil

# Test Numbers
check_numbers = ['49927398716', '4847352989263095', '79927398713', '5543352315777720', '4624748233249780']
 
if __name__ == "__main__":
    for number in check_numbers:
	    print(LuhnUtil(number, True).runAlgorithm())
