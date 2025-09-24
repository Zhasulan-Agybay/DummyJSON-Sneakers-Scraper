# DummyJSON Sneakers Scraper 👟

This project demonstrates working with the **DummyJSON e-commerce API**. 
The script automatically retrieves a list of categories, selects categories containing shoes, downloads products, and saves them to a CSV file.

## Features
- Retrieving categories and products via API
- Filtering data (leaving only shoes)
- Saving results to CSV
- Minimal dependencies, easy to launch


## Project Structure
```
NHL-Teams-Stats-Scraper/
├── src/ 
│   └── main.py # main scraper script
├── output/ 
│   └── sneakers_dummyjson.csv # CSV file with scraped data 
├── gif/
│   └── demo.gif # optional demo animation
├── .gitignore
├── requirements.txt # dependencies 
└── README.md # project description
```

## Installation
```bash
# Clone the repository
git clone https://github.com/Zhasulan-Agybay/DummyJSON-Sneakers-Scraper.git
cd DummyJSON-Sneakers-Scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python src/main.py
```

## Demo.gif
![Demo_GIF](GIF/demo.gif)

#### 👨💻 About This Project

Hi, my name is Zhasulan Agybay and this is my API scraping project. This project was created as a demonstration of API and data processing skills. It shows how to work with the REST API, filter and structure data, and save the results in a convenient format. You can check out my other projects on GitHub.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
