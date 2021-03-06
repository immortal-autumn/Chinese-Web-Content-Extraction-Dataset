# Chinese-Web-Content-Extraction-Dataset
A handcrafted dataset for Author / Date / Content 

## Announcement

This dataset is a part of my final project, "A better content extractor". You are free to use/contribute to the dataset if you want to.

## Design:

The dataset structure has the following hierarchy:

- Chinese Web Content Extraction Dataset
  - author
    - (Series of authors... in text format)
  - date
    - (Series of dates... in text format)
  - cleaned
    - (Series of contents... in text format)
  - Original
    - (Series of cached webpages ... in .html format)

Filenames in original folders do have the corresponding filenames in cleaned, date and author folder, which corresponds to the corresponding extracted information of the original HTML file. The dataset is totally handcrafted and includes the following three major information of a web page: content, author, and date.

### Content

Contents are extracted by copying the whole content area to a txt file filtering the header/dates/authors of the HTML file, formats may not be quite as expected, but the content should be quite correct.

### Author

Authors are extracted with a series of author names divided by a blank space format such as "Author1 Author2 Author3". For an unknown author, the result will show as "UNKNOWN."

### Date

Dates are extracted in YYYY-MM-DD HH-MM-SS format. If some fields are missing, the corresponding position will not show the corresponding field in the dataset. If the date is not shown in the dataset, the result will display the corresponding data as "UNKNOWN."
