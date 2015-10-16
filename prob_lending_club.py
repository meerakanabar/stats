import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

plt.figure(1)
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("boxplotInvestorsFunding.png")

plt.figure(2)
loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("HistogramInvestorsFunding.png")


plt.figure(3)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("ProbabilityPlotInvestorsFunding.png")

plt.figure(4)
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplotAmountRequested.png")

plt.figure(5)
loansData.hist('Amount.Requested')
plt.savefig("AmountRequested.png")

plt.figure(6)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("AmountRequested.png")
