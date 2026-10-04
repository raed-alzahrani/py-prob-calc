exit = 1
def main():
    #Discrete and continuous probability distributions
    print("Welcome to the my Probability Distribution Calculator! \t\t\tMade With Love by: Raed ^-^")

    """dictionary:
        Discrete Distributions:
            (1 = Binomial Distribution), 
            (2 = Poisson Distribution), 
            (3 = HyperGeometric Distribution),

        Continuous Distributions:     
            (4 = Normal Distribution), 
            (5 = Exponential Distribution), 
            (6 = Uniform Distribution)

        Functions: 
            (7 = CDF [Cumulative Distribution Function] )   

    """
    #Libraries
    import math
    #modes
    discrete = [1, 2, 3]
    continuous = [4, 5, 6]
    functions = [7]
    mode = [discrete, continuous, functions]
    #Results function
    def print_result_needed_func():
        result_done_check = 1
        if result_done_check <2:
            nm_result_needed = input(f"Choose what to calculate (P/E/V/S): \n\t (P): P(X=x)\n\t (E): Mean or E(x)\n\t (V): Variance or Var(x)\n\t (S): Standard Deviation or σ\n :   ").lower()
            global p_r
            p_r = 0
            need_P = False
            need_E = False
            need_V = False
            need_S = False
            need_ALL = False
            need_P = "p" in nm_result_needed
            need_E = "e" in nm_result_needed
            need_V = "v" in nm_result_needed
            need_S = "s" in nm_result_needed
            need_ALL = "all" in nm_result_needed
            if need_P == True:
                global p_r
                print(f"P(X=x) = \t {f_prob}\n" )
                p_r = 1 + p_r
            if need_E == True:
                global p_r
                print(f"Mean or E(X) = \t {E_x}\n")
                p_r = 1 + p_r
            if need_V == True:
                global p_r
                print(f"Variance or Var(x) = \t {Var_x}\n")
                p_r = 1 + p_r
            if need_S == True:
                global p_r
                print(f"Standard Deviation Or σ = \t {sigma}\n")
                p_r = 1 + p_r
            if need_ALL == True:
                global p_r
                print(f"P(X=x) = \t {f_prob}\nMean or E(X) = \t {E_x}\nVariance or Var(x) = \t {Var_x}\nStandard Deviation Or σ = \t {sigma}\n")    
                p_r = 1 + p_r
            if p_r == 0:
                print("Wrong input, please choose from the list provided.\nRestarting program.")
                print_result_needed_func()   
            else:
                pass     
    #Input
    def enter_mode():
        global choosed_mode
        enter_mode_r = input("Enter mode: \n\t  Discrete \n \t\t  1 = Binomial Distribution\n \t\t  2 = Poisson Distribution\n \t\t  3 = HyperGeometric Distribution\n\t  Continuous\n \t\t  4 = Normal Distribution\n \t\t  5 = Exponential Distribution\n \t\t  6 = Uniform Distribution\n\t  Functions\n \t\t  7 = CDF [Cumulative Distribution Function]\n :")
        try:
            enter_mode_r = int(enter_mode_r)
            if enter_mode_r in discrete:
                choosed_mode = enter_mode_r
                pass
            elif enter_mode_r in continuous:
                choosed_mode = enter_mode_r
                pass
            elif enter_mode_r in functions:
                choosed_mode = enter_mode_r
                pass
            else:
                print("Invalid input. Please enter a NUMBER between 1 AND 7.")
                enter_mode()
        except ValueError:
            print("Invalid input. Please enter a NUMBER between 1 AND 7.")
            enter_mode()    
    enter_mode()
    #Functions    
    def inverse_error_func():    #Winitzki Approximation
        a = 0.147
        t = math.log(1-(P_x**2))
        bas_pi_sq =  ( 2/( math.pi*a ) + ( t/2 ) )**2 - ( t/a ) 
        bas_neg_pi = ( 2/( math.pi*a ) ) + ( t/2 )
        res_bas = math.sqrt( math.sqrt (bas_pi_sq) - (bas_neg_pi) ) 
        if P_x>0:
            return res_bas
        elif P_x==0:
            return 0
        elif P_x<0:
            res_bas_ng = -(res_bas)
            return res_bas_ng 
    def ncr(n, r):
        if ((n>0 and r>0) and (r<=n)) or (r==0 and r<=n):
            try:
                ncr = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
                return ncr
            except ValueError:
                print("Error, invalid input.\nRestarting program.")
                main()
        else:
            print("Error, invalid input.\nThis function only takes integer number AND positive numbers AND the SECOND number MUST be SMALLER than the FIRST.\nRestarting program.\n")
            pass                
    #Binomial Distribution
    def binomial_dis():
        if mode[0][0]==choosed_mode:
            try:
                global P_x, sigma, Var_x, f_prob, E_x
                n = int(input("Enter number of n: "))
                p = float(input("Enter probability of success p in decimals [80% = 0.80]   :     "))
                q = 1 - p
                P_x = int(input("Enter P(X=x) [small x]  :    "))
                f_prob = ncr(n, P_x) * (p ** P_x) * (q ** (n - P_x))
                E_x = n * p
                Var_x = n * p * q
                sigma = (Var_x) ** 0.5
                print_result_needed_func()
            except ValueError:
                print("Error, invalid input.\n Try again.")
    #Poisson Distribution
    def poisson_dis():
        if mode[0][1]==choosed_mode:
            global P_x, sigma, Var_x, f_prob, E_x
            P_x = int(input("Enter P(X=x) [small x]  :    "))
            e = 2.718281828459045
            delta = float(input("Enter Delta/Mean/Var value:    "))
            f_prob =(e**(-delta))*(delta**P_x)/math.factorial(P_x) 
            E_x = delta
            Var_x = delta
            sigma = (Var_x) ** 0.5
            print_result_needed_func()
    #Hypergeometric Distribution
    def hyper_dis():
        if mode[0][2]==choosed_mode:
            global P_x, sigma, Var_x, f_prob, E_x
            N = int(input("Enter population size N: "))
            K = int(input("Enter number of success states in the population K: "))
            n = int(input("Enter number of draws n: "))
            P_x = int(input("Enter P(X=x) [small x]  :    "))
            N2 = N - K
            n2 = n - P_x
            Nn = N - n
            f_prob = (ncr(K, P_x)*(ncr(N2, n2)))/ncr(N,n)
            E_x = n * (K/N)
            Var_x = n * (K/N) * (1-(K/N)) * (Nn/(N-1))
            sigma = (Var_x) ** 0.5
            print_result_needed_func()
    #CDF [Cumulative Distribution Function]
    def cdf_func():
        if mode[2][0]==choosed_mode:
            e = 2.718281828459045
            P_x = float(input("Enter P(X=x) [small x]  :    "))
            delta = float(input("Enter Mean/Var value:    "))
            f_cdf = 1 - e**(-delta*P_x)
            print(f"CDF = {f_cdf}")
    #Continuous Uniform Distributions
    def cont_uni_dis():
        if mode[1][2]==choosed_mode:
            global P_x, sigma, Var_x, f_prob, E_x
            A = float(input("Enter lower bound A: "))
            B = float(input("Enter upper bound B: "))
            f_prob = 1/(B-A)
            E_x = (A + B) / 2
            Var_x = ((B - A) ** 2) / 12
            sigma = (Var_x) ** 0.5
            print_result_needed_func()
    #Exponential Distribution
    def exp_dis():
        if mode[1][1]==choosed_mode:
            global P_x, sigma, Var_x, f_prob, E_x
            e = 2.718281828459045
            P_x = float(input("Enter P(X=x) [small x]  :    "))
            delta = float(input("Enter Delta value:    "))
            f_prob = delta * (e**(-delta*P_x))
            E_x = 1 / delta
            Var_x = 1 / (delta ** 2)
            sigma = (Var_x) ** 0.5
            print_result_needed_func()
            cdf_exponential_need = input("Do you want to calculate the CDF for Exponential Distribution? (y/n): ")
            if cdf_exponential_need.lower() == "y":
                cdf_form = input("Enter CDF form: \n\t(A)P(X<x)\n\t(B)P(X>x)\n :   ").upper()
                if cdf_form == "A":
                    f_cdf_exponential = 1 - e**(-delta*P_x)
                    print(f"CDF = {f_cdf_exponential}")
                elif cdf_form == "B":
                    f_cdf_exponential = e**(-delta*P_x)
                    print(f"CDF = {f_cdf_exponential}")
                else:
                    print("Invalid input. Please enter 'A' or 'B'.")    
            if cdf_exponential_need.lower() == "n":
                pass
            else:
                pass
    #Normal Distribution
    def normal_dis():
        if mode[1][0]==choosed_mode:
            P_x = float(input("Enter P(X=x)  :    "))
            E_x = float(input("Enter Mean (E(X)): "))
            sigma = float(input("Enter Standard Deviation (σ): "))
            Z = (P_x - E_x) / sigma
            p_value = 0.5 * (1 + math.erf(Z / math.sqrt(2)))
            value_needed = input("Choose the value to calculate:\n\t Z = Z-Score\n\t P = Probability\n\t E = Expected Count/Number \n:   ")
            if value_needed.lower() == "z":
                which_value = input("Calculate Z-score from P(X=x) & E(x) & σ or from P(X=x) & P? (Enter 'A' for the first option or 'B' for the second option): ")
                if which_value.lower() == "a":
                    print(f"Z-score = {Z}")
                elif which_value.lower() == "b":
                    P_value = float(input("Enter Probability (P): "))
                    P_x = ( 2 * P_value ) - 1
                    Z_from_P = inverse_error_func() * (math.sqrt(2))
                    print(f"Z-score from Probability = {Z_from_P}")
                else:
                    print("Invalid input. Please enter 'A' or 'B'.")
            if value_needed.lower() == "p":
                print(f"Probability (P) = {p_value}")
            elif value_needed.lower() == "e":
                print(f"Expected Count/Number (E) = {E_x}")
            else:
                print("Invalid input. Please enter 'P', 'Z', or 'E'.")                        
    def exit_func():       
        exit_program = input("Do you want to exit the program? (y/n): ")
        if exit_program.lower() == "y":
            print("Exiting the program. Goodbye!")
            global exit
            exit = exit + 1       
        elif exit_program.lower() == "n":
            print("You can run the program again to perform more calculations.")
        else:
            print("Error 400. Restarting the program.")  
    def exec_func():
        try:
            binomial_dis()
            poisson_dis()
            hyper_dis()
            cdf_func()
            cont_uni_dis()
            exp_dis()
            normal_dis()
        except (ValueError, ZeroDivisionError):
            print("Error, invalid input.\nTry again.")  
    exec_func()    
    exit_func()                    
while exit < 2:
    main()
exit()