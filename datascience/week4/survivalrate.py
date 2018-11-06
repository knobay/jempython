"""3. What is the overall survival /
rate of the people that were on board?"""

import seaborn as sns

titanic = sns.load_dataset('titanic')

survivalrate = titanic.survived.sum()/titanic.survived.count()

print('Survival rate {0}'.format(survivalrate))
