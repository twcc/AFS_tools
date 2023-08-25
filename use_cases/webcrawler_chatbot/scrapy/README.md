To crawl webpages from desired website, please use following instructions:



## Step 1: Install Scrapy Tools

First, you need to install a toolkit called [Scrapy](https://scrapy.org), which is a tool used for web scraping. To do this, follow these steps:

Open your command prompt or terminal on your computer.
Type the following command and press Enter: `python -m pip install -r requirements.txt`
This command will install the necessary tools and libraries that Scrapy requires to work.

## Step 2: Create a Scrapy Project

Now that you have Scrapy installed, you'll need to set up a new Scrapy project. This is like creating a workspace for your web scraping tasks. Follow these steps:

1. Still in your command prompt or terminal, enter: `scrapy startproject website`
2. This command will create a new folder named "website" where your project files will be organized.

For more detailed guidance, you can explore the [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)) which provides comprehensive instructions.

## Step 3: Add WebSpider

To actually start scraping webpages, you need to use something called a spider. Here's how you can do that:

1. Inside the "assets" folder, locate a file named `WebSpider.py`.
2. Copy this file and move it to the "spiders" folder within the "website" project folder.

## Step 4: Update Items

Scraped data needs a place to be stored. Scrapy uses something called "items" for this purpose. Let's update them:

1. Still in the "assets" folder, find the `items.py` file.
2. Replace the existing `items.py` file in the "website" project folder with the one you found in the "assets" folder.

## Step 5: Start Crawling

With the setup in place, it's time to start the crawling process:

1. Open your command prompt or terminal.
2. Navigate to your "website" project folder using the `cd` command (e.g., `cd` scrapy_project/website).
3. Enter the following command: `scrapy crawl website -o website.json`
4. This command will initiate the crawling process using the spider you added, and it will save the output in a file named `website.json`.

## Step 6: Review and Clean Data

After the crawling is done, you'll have a `website.json` file with the scraped data. It's a good idea to review this file and remove any unnecessary or irrelevant data to keep your dataset clean and manageable.

And that's it! You've successfully crawled webpages from a desired website using Scrapy. Remember to refer back to these steps whenever you need to perform web scraping tasks.