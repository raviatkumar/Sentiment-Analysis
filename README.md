# Project Name : Sentiment Analysis

### **Summary:**

The project involves sentiment analysis on the IMDb dataset, which comprises 50,000 movie reviews. The dataset is structured for binary sentiment classification, with 25,000 reviews designated for training and an additional 25,000 for testing. The objective is to predict the sentiment of movie reviews, distinguishing between positive and negative sentiments.

### **Approach:**

1. **Exploratory Data Analysis (EDA):** We analyzed the dataset to understand its characteristics. The analysis revealed an equal distribution of positive and negative sentiments, indicating a balanced dataset. Most reviews were observed to be relatively short, with shorter reviews being more frequent. Additionally, a WordCloud analysis highlighted common terms associated with positive and negative sentiments.

2. **Text Preprocessing:** We performed text preprocessing to clean and prepare the text data for modeling. This included removing unwanted characters, URLs, converting text to lowercase, tokenization, removing stopwords, and lemmatization. We also generated uni, bi, tri, and four-gram features from the text data.

3. **Feature Engineering:** We used TF-IDF vectorization to convert the text data into numerical features while preserving the importance of words in the documents. The target variable was encoded using label encoding.

4. **Model Training and Evaluation:** We trained logistic regression and multinomial naive Bayes models on the preprocessed data. Both models were evaluated using classification reports, which provided insights into precision, recall, and F1-score for each class (positive and negative sentiments). Based on the results, logistic regression performed better and was chosen as the final model.

### **Conclusion:**

The sentiment analysis project successfully developed a model capable of accurately predicting the sentiment of movie reviews. The logistic regression model achieved an accuracy of approximately 89%, with balanced performance across both positive and negative sentiments. The project highlights the effectiveness of natural language processing techniques and machine learning algorithms in analyzing textual data and extracting valuable insights. The developed model can be utilized in various applications, including market research, customer feedback analysis, and opinion mining in social media platforms, to gauge public sentiment towards movies. Overall, the project demonstrates the importance of sentiment analysis in understanding user opinions and preferences in the movie industry.
