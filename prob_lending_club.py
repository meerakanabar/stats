import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

import matplotlib.pyplot as plt
import pandas as pd

loansData.boxplot(column='Amount.Funded.By.Investors')

plt.savefig("boxplotInvestorsFunding.png")

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("HistogramInvestorsFunding.png")

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("ProbabilityPlotInvestorsFunding.png")

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

import matplotlib.pyplot as plt
import pandas as pd

loansData.boxplot(column='Amount.Requested')

plt.savefig("boxplotAmountRequested.png")

loansData.hist('Amount.Requested')
plt.savefig("AmountRequested.png")

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("AmountRequested.png")