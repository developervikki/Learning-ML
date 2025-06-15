# #promlem
# -A disease affects 1% of a population
# -A test is 95% accurate for diseased indivisuals and 90% accurate for non diseased indivisuals
# -find probability of having the disease given a positive test result

def byes_therorem(prior, sensitivity,specificity):
    evidence=(sensitivity*prior)+((1-specificity)*(1-prior))
    posterior=(sensitivity*prior)/evidence
    
    return posterior

prior=0.01 #1% prevalence
sensitivity=0.5 # true positive rate  
specificity=0.90 #true negative rate




posterior=byes_therorem(prior,sensitivity, specificity)
print("probability of the disease given a positive test : ",posterior)
