# PM Modi Text Speeches

This scrapper gets the latest text speeches of Indian PM [Narendra Modi](https://en.wikipedia.org/wiki/Narendra_Modi). The scrapper extracts the text speech and article URL, title, publish info, and tags. The dataset is hosted in Kaggle, [Narendra Modi - Text Speeches](https://www.kaggle.com/adiamaan/modi-speeches).

![Modi](https://images.hindustantimes.com/img/2021/09/04/550x309/PTI09-03-2021-000085B-0_1630691680953_1630739078395.jpg)

The scrapper is scheduled to run every day at 8 AM using a Github Action workflow. The dataset contains the speech translated primarily from Hindi to English. The dataset includes speeches starting from 2018.

## Data description:
The dataset contains the following columns,

| Syntax       | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| id           | Unique ID                                                                 |
| url          | URL from where the data is scraped                                        |
| title        | Title of the speech                                                       |
| article_text | Speech in text form                                                       |
| images       | URL of Images taken during the speech, mostly of Modi                     |
| publish_info | Publish info including by, date and time                                  |
| tags         | Tags from the scrapped website, can be used for categorizing the speeches |

