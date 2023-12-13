# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model is not as accurate. This is due to all the outliers that effect the data, resuting in a different, less accurate outcome. Standardizing our models make sure that there is a trend within the data.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
This is very accurate because it has a .86 r squared value. This is accurate enough for the given use case because it is much closer to 1.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did good in terms o the predicted and actual results. Both of the data matched and there was way less inaccurate results.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
She would buy an SUV.

