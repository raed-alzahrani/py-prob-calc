exit = False
if exit == True:
    exit()
else:
    pass    
def main():

    #Discrete and continuous probability distributions
    print("Welcome to the my Probability Distribution Calculator!\n Made With Love by: Raed ^-^")

    """dictionary:
        Discrete Distributions:
            (1 = Binomial Distribution), 
            (2 = Poisson Distribution), 
            (3 = Geometric Distribution),

        continuous Distributions:     
            (4 = Normal Distribution), 
            (5 = Exponential Distribution), 
            (6 = Uniform Distribution)

        Functions: 
            (7 = CDF [Cumulative Distribution Function] )   

        Results:
            (8 = P(X=x)),
            (9 = Mean or E(x)), 
            (10 = Variance or Var(x))
            (11 = Standard Deviation or σ)
    """
    #Libraries
    import math

    #modes
    discrete = [1, 2, 3]
    continuous = [4, 5, 6]
    functions = [7]
    mode = [discrete, continuous, functions]
    sub_mod_result = [8, 9, 10, 11] #P(X=x), Mean, Variance, Standard Deviation

    #Results function
    def print_result_needed_func():
        nm_result_needed = input(f"Choose what to calculate (P/E/V/S): \n\t (P): P(X=x)\n\t (E): Mean or E(x)\n\t (V): Variance or Var(x)\n\t (S): Standard Deviation or σ\n :   ").lower()
        need_P = "p" in nm_result_needed
        need_E = "e" in nm_result_needed
        need_V = "v" in nm_result_needed
        need_S = "s" in nm_result_needed
        if need_P == True:
            print(f"P(X=x) = \t {f_prob}\n" )
        if need_E == True:
            print(f"Mean or E(X) = \t {E_x}\n")    
        if need_V == True:
            print(f"Variance or Var(x) = \t {Var_x}\n")
        if need_S == True:
            print(f"Standard Deviation Or σ = \t {sigma}\n")        

    #Input
    enter_mode = input("Enter mode: \n\t  Discrete \n \t\t  1 = Binomial Distribution\n \t\t  2 = Poisson Distribution\n \t\t  3 = Geometric Distribution\n\t  continuous\n \t\t  4 = Normal Distribution\n \t\t  5 = Exponential Distribution\n \t\t  6 = Uniform Distribution\n\t  Functions\n \t\t  7 = CDF [Cumulative Distribution Function]\n :")
    try:
        enter_mode = int(enter_mode)
        if enter_mode in discrete:
            pass
        elif enter_mode in continuous:
            pass
        else:
            print("Invalid input. Please enter a NUMBER between 1 AND 7.")
    except ValueError:
        print("Invalid input. Please enter a NUMBER between 1 AND 7.")    

    #Functions
    def ncr(n, r):
        ncr = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        return ncr


    #Binomial Distribution
    if mode[0][0]==enter_mode:
        n = int(input("Enter number of n: "))
        p = float(input("Enter probability of success p in decimals [80% = 0.80]   :     "))
        q = 1 - p
        P_x = int(input("Enter P(X=x) [small x]  :    "))
        f_prob = ncr(n, P_x) * (p ** P_x) * (q ** (n - P_x))
        E_x = n * p
        Var_x = n * p * q
        sigma = (Var_x) ** 0.5
        print_result_needed_func()

    #Poisson Distribution
    if mode[0][1]==enter_mode:
        P_x = int(input("Enter P(X=x) [small x]  :    "))
        e = 2.718281828459045
        delta = float(input("Enter Delta/Mean/Var value:    "))
        f_prob =(e**(-delta))*(delta**P_x)/math.factorial(P_x) 
        E_x = delta
        Var_x = delta
        sigma = (Var_x) ** 0.5
        print_result_needed_func()
    #Hypergeometric Distribution
    if mode[0][2]==enter_mode:
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
    if mode[2][0]==enter_mode:
        e = 2.718281828459045
        P_x = float(input("Enter P(X=x) [small x]  :    "))
        delta = float(input("Enter Mean/Var value:    "))
        f_cdf = 1 - e**(-delta*P_x)
        print(f"CDF = {f_cdf}")

    #Continuous Uniform Distributions
    if mode[1][2]==enter_mode:
        A = float(input("Enter lower bound A: "))
        B = float(input("Enter upper bound B: "))
        f_prob = 1/(B-A)
        E_x = (A + B) / 2
        Var_x = ((B - A) ** 2) / 12
        sigma = (Var_x) ** 0.5
        print_result_needed_func()

    #Exponential Distribution
    if mode[1][1]==enter_mode:
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
    if mode[1][0]==enter_mode:
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
                Z_from_P = math.sqrt(2) * math.erfinv(2 * P_value - 1)
                print(f"Z-score from Probability = {Z_from_P}")
            else:
                print("Invalid input. Please enter 'A' or 'B'.")
        if value_needed.lower() == "p":
            print(f"Probability (P) = {p_value}")
        if value_needed.lower() == "e":
            print(f"Expected Count/Number (E) = {E_x}")
        else:
            print("Invalid input. Please enter 'P', 'Z', or 'E'.")                        
    exit_program = input("Do you want to exit the program? (y/n): ")
    if exit_program.lower() == "y":
        print("Exiting the program. Goodbye!")
        exit = True        
    elif exit_program.lower() == "n":
        print("You can run the program again to perform more calculations.")
        main()
    else:
        print("Error 400. Restarting the program.")
main()                