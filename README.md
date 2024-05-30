# Stereotypical bias analyzer

Steps to use this website :
1) Pip install flask
2) Download the requirement.txt
3) write Python app.py in the cmd after downloading this folder

What you identify from this website :
Race Color,
Socioeconomic,
Gender,
Disability,
Nationality,
Sexual Orientation,
Physical Appearance,
Religion,
Age,
Profession.

Enter any type of input sentence from this label and check the bias type of the sentence.

Stereotypical bias, an extensive cognitive phenomena, continues to impact perceptions, decisions, and behaviors across a wide range of human interactions.Because pre-trained
language models are quite prominent and are trained on large real-world datasets, there are concerns that these models could incorporate and reinforce stereotypical biases. The necessity to measure the biases inherent in these models is discussed in this work. Previous research usually assesses pre-trained language models using a small number of artificially constructed bias assessing sentences. In order to offer a comprehensive evaluation, we present a novel dataset that combines four distinct datasets to analyze stereotyped biases in ten distinct domains: race/color, socioeconomic, gender, disability, nationality, sexual orientation, physical-appearance, religion, age, profession. We analyze well known models like BERT and RoBERTa systematically, exposing their tendency to show considerable stereotypical biases in a variety of domains. Our results highlight the pervasive nature of the typical biases present in these models are and emphasize how critical it is to eliminate bias in applications involving natural language processing.

Here is the algorithm for the text classification and bias detection :

![image](https://github.com/neha13rana/Stereotypical-Bias-Analyzer/assets/121093178/d0a78462-1f29-4bee-9956-eb7fa17c8a26)

proposed model of our project :

![image](https://github.com/neha13rana/Stereotypical-Bias-Analyzer/assets/121093178/977074eb-9b3e-4ff2-ba15-ee78c9597c70)

Bias Distribution of the dataset :

![image](https://github.com/neha13rana/Stereotypical-Bias-Analyzer/assets/121093178/f1ab7c8a-0009-4095-82d5-5a3cb315b7f1)

The test dataset yielded an impressive accuracy of 0.9832
for our bias identification model, demonstrating the model’s
effectiveness in accurately recognising instances of biases in a
variety of scenarios. This high degree of accuracy highlights
the model’s resilience and potency in identifying minute
linguistic clues that point to biases in text written in natural
language. 

1)Input:

![WhatsApp Image 2024-04-29 at 09 59 47_ed824d43](https://github.com/neha13rana/Stereotypical-Bias-Analyzer/assets/121093178/6dc2d597-ba27-4044-b126-1e3e0787c3f8)

2)Output:

![WhatsApp Image 2024-04-29 at 10 00 03_ee57b731](https://github.com/neha13rana/Stereotypical-Bias-Analyzer/assets/121093178/74f2b060-e010-49fb-b7e5-67fc43b39768)

Limitation :

While our study demonstrates promising results in bias
identification, we acknowledge the inherent challenge posed
by biased training data. Biases within the training set can
stem from various sources, including societal prejudices, algorithmic biases, and sampling biases. These biases may result
in skewed representations of certain demographic groups or
perspectives, potentially leading to inaccurate predictions by
our model, another limitation to consider is the number of bias
classes represented in our model.

Conclusion :

In conclusion, our study provides valuable insights into
the pervasive nature of stereotypical biases across various
dimensions of identity and experience. We have illustrated
the effects of prejudices against people based on race,
gender, disability, nationality, sexual orientation, and other
characteristics on individuals, communities, and society
through an extensive analysis.Our analysis also demonstrates
the potential of advanced methods in identifying stereotypical
biases in textual data by looking at pretrained language
models like BERT and RoBERTa. One key finding of our
experiment is the higher accuracy of RoBERTa compared to
BERT, suggesting the importance of model architecture and
training strategies in addressing biases in NLP tasks. This
underscores the need for continued research and innovation in
developing AI technologies that are more inclusive, equitable,
and fair.


