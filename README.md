<div align='center'>
  
# PM Modi text speech scrapper

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/adiamaan92/modi-speech-scrapper/blob/master/.pre-commit-config.yaml)
[![License](https://img.shields.io/badge/License-MIT-informational.svg)](https://github.com/adiamaan92/modi-speech-scrapper/blob/master/MIT-LICENSE.txt)
[![Runs-Daily](https://img.shields.io/badge/Runs-Daily-brightgreen)](https://github.com/adiamaan92/modi-speech-scrapper/actions)

</div>

## Context
Narendra Damodaradas Modi is an Indian politician serving as the 14th and current prime minister of India since 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is a Member of Parliament from Varanasi.

Modi had a long political career, before quickly rising within his party from the Chief Minister of Gujarat (2001 - 2014) to the Primi Minister candidate in the 2014 election. Known for his excellent oratorical skills and ability to connect to the common man, this dataset gives access to all his text speeches starting from 2018.

<div align='center'>
  
![Modi](https://images.hindustantimes.com/img/2021/09/04/550x309/PTI09-03-2021-000085B-0_1630691680953_1630739078395.jpg)
  
</div>

> The scrapper is scheduled to run every day at 8 AM using a Github Action workflow. 

The dataset contains the speech translated primarily from Hindi to English. The dataset includes speeches starting from 2018.

## Dataset:
Dataset is hosted here, https://www.kaggle.com/adiamaan/modi-speeches
## Data description:
The dataset contains the following columns,

| Column       | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| id           | Unique ID                                                                 |
| url          | URL from where the data is scraped                                        |
| title        | Title of the speech                                                       |
| article_text | Speech in text form                                                       |
| images       | URL of Images taken during the speech, mostly of Modi                     |
| publish_info | Publish info including by, date and time                                  |
| tags         | Tags from the scrapped website, can be used for categorizing the speeches |

