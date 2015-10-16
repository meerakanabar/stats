import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')

plt.savefig("boxplotInvestorsFunding.png")

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("HistogramInvestorsFunding.png")


plt.figure(1)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("ProbabilityPlotInvestorsFunding.png")

loansData.dropna(inplace=True)


loansData.boxplot(column='Amount.Requested')

plt.savefig("boxplotAmountRequested.png")

loansData.hist('Amount.Requested')
plt.savefig("AmountRequested.png")

plt.figure(2)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("AmountRequested.png")
