# Parliament Speech Analyzer
This project aims to analyze the speeches and discussions from parliamentary meetings in the Fédération Wallonie-Bruxelles and provide insights into different 
aspects such as themes, projects, and sentiment. 
The data used in this project consists of PDF files of parliamentary meetings, converted into JSON files containing structured information about the meetings.

The project is on going. 

# 1st part : Selenium scrapper (finished)
This Python script utilizes Selenium WebDriver for automated browsing, specifically, it scrapes PDF documents from the Belgian Parliament website (Parlement de la Fédération Wallonie-Bruxelles) at https://www.pfwb.be/documents-parlementaires.

Description
* The script performs the following operations:

* Initializes a Selenium WebDriver instance with specific Chrome options to download files directly without a prompt, opening PDF files externally, and enable safe browsing.

* It navigates to the Belgian Parliament website.

* After the site loads, it interacts with a form on the page to access a list of document types and selects a specific filter.

* Once the filter is selected, the script iterates through all the pages of the website. For each page, it attempts to find and click a link that leads to a specific document.

* After clicking on the document link, it finds a download link on the new page, gets its href attribute (the URL of the file), and navigates to this URL. This action initiates the file download due to the previously set Chrome options.

* After downloading the file, the script navigates back to the list of documents and moves on to the next document. This process repeats until all documents on the page have been downloaded.

* Finally, the script finds and clicks on the 'next page' button to go to the next page of the list and repeats the whole process for the new page. If there are no more pages (i.e., if the 'next page' button cannot be clicked), it ends the process.

# 2nd part: Connection to the Google Drive (on going)

# 3d part: Transforming the pdf file to JSON (on going - available for now in the Jupyter Notebooks files)

# 4th part: Analysis 
