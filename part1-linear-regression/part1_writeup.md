# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?
the r squared value is a measurement that tells you how well the predicted data fits in with the rest of the prediction model.  It can tell you how accurate the model may be.  
2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?
Model's Linear Equation: y = 0.94x + 96.98
R Squared value: 0.6257932855322315
Prediction when x is 43: [137.46185286]
3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?
I dont think that this model is accurate enough to reliably predict someones blood pressure based on age.  First off this model dosent have that much data to work with and i wouldnt trust it to make uper accurate predictions with such little data.  Secondly there are many other factors that affect blood pressure other than age so using age as the sole factor for prediction would lead to wild inconsistency.  If you wanted this model to be more accurate you would have to give it a lot more data so it can do a better job of making its predictions, but yoyu mut also make sure that all of the data is from people in a esting state and make sure there are no other factors affecting their blood pressure.  