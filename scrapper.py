"""
Speech scrapper
----------------

This module adds the latest speech to the existing dataset and updates
the Kaggle dataset

Workflow
--------
1. Download the latest kaggle dataset
2. Get a list of new speeches that are added after the last run
3. Fetch the latest speeches, update to the existing dataset and
upload back to Kaggle

"""
import datetime
import re
from typing import List, Tuple

import pandas as pd
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def get_speeches(api: KaggleApi) -> pd.DataFrame:
    """Get existing speech from kaggle dataset

    Args:
        api (KaggleApi): Kaggle api

    Returns:
        pd.DataFrame: Speech as dataframe
    """
    api.dataset_download_files("adiamaan/modi-speeches", path="./data", unzip=True)
    return pd.read_csv("./data/modi_speeches.csv")


def extract_new_speeches(latest_speech_title: str) -> Tuple[List[str], List[str]]:
    """
    Extract new speeches from the latest speech title
    --------------------------------------------------

    Given the latest speech title, this function finds all the speeches
    that are delivered after the latest speech title.

    Args:
        latest_speech_title (str): The last speech in the existing dataset

    Returns:
        Tuple[List[str], List[str]]: List of links and titles
    """
    links = []
    titles = []
    i = 1

    while True:
        r = requests.get(
            f"https://www.narendramodi.in/speech/loadspeeche?page={i}&language=en",
            headers=headers,
        )

        if r.status_code != 200:
            break

        tree = etree.fromstring(r.text, parser=etree.HTMLParser())

        for element in tree.xpath("//div[contains(@class, 'speechesItemLink')]"):
            title = element.xpath(".//a//text()")[0]

            if title == latest_speech_title:
                break

            links.append(element.xpath(".//a/@href")[0])
            titles.append(element.xpath(".//a/text()")[0])

        if title == latest_speech_title:
            break
        i += 1

    return links, titles


def extract_speech_details(
    original_links: List[str], original_titles: List[str]
) -> pd.DataFrame:
    """
    Extract the speech text from the link
    -------------------------------------

    Given a list of links and titles, this function

    Args:
        original_links (List[str]): [description]
        original_titles (List[str]): [description]

    Returns:
        pd.DataFrame: [description]
    """
    urls, titles, speeches, images, publish_info, tags = [], [], [], [], [], []

    for link, title in zip(original_links, original_titles):
        r = requests.get(link, headers=headers)

        if r.status_code != 200:
            continue

        tree = etree.fromstring(r.text, parser=etree.HTMLParser())
        speech = "\n".join(
            tree.xpath(
                "(//article[contains(@class, 'main_article_content')])[1]//p/text()"
            )
        )

        # Check if the speech is in english. If it contains hindi, this filter will skip over it.
        if len(re.sub("[^a-zA-Z]", "", speech)) / len(speech) < 0.20:
            continue

        speeches.append(speech)
        publish_info.append(
            tree.xpath("//div[contains(@class, 'captionDate')]//text()")[0]
        )
        tags.append(
            ",".join(tree.xpath("//div[contains(@class, 'tags')]//li//a/text()")[1:])
        )
        images.append(
            ",".join(tree.xpath("//div[contains(@class, 'imageShare')]//img/@src"))
        )

        urls.append(link)
        titles.append(title)

    return (
        pd.DataFrame(
            {
                "url": urls,
                "title": titles,
                "article_text": speeches,
                "images": images,
                "publish_info": publish_info,
                "tags": tags,
            }
        )
        .reset_index()
        .rename(columns={"index": "id"})
    )


if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()

    # Controls how far back we go to extract the speeches that are not translated
    threshold = 10

    speeches = get_speeches(api)
    speeches = (
        speeches.loc[:, ~speeches.columns.str.contains("Unnamed")]
        .reset_index()
        .rename(columns={"index": "id"})
    )

    links, titles = extract_new_speeches(speeches.title.values[threshold])

    existing_titles = speeches.title.values
    new_speeches = extract_speech_details(links, titles)

    delta_speeches = new_speeches.query("title not in @existing_titles").reset_index(
        drop=True
    )

    updated_speeches = pd.concat([delta_speeches, speeches])
    updated_speeches.to_csv("./data/modi_speeches.csv")
    api.dataset_create_version(
        "./data/",
        version_notes=f"Updated on {datetime.datetime.now().strftime('%Y-%m-%d')}",
    )
