"""4. What is the survival rate depending on the gender? /
Use a bar plot to show the difference."""

import seaborn as sns

titanic = sns.load_dataset('titanic')

males = len(titanic.query("sex=='male'").index)
malesurvivors = len(titanic.query("sex=='male' and survived==True").index)
females = len(titanic.query("sex=='female'").index)
femalesurvivors = len(titanic.query("sex=='female' and survived==True").index)

# msurvive = survivors[survivors.sex == 'male'].count()

# titanicwomen = titanic['sex'] == 'female'

print('Male survivors: {0} out of {1}\nFemale survivors:{2} out of {3}'.format(
    malesurvivors, males, femalesurvivors, females))

# malesurvival = titanicmen.survived.sum()

# femalesurvival = titanicwomen.survived.sum()

# print('Men    