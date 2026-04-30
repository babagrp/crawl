from setuptools import setup, find_packages

setup(
    name="lnmu-scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "playwright-stealth",
        "beautifulsoup4",
        "lxml",
        "click",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "lnmu-scraper=lnmu_scraper.cli:main"
        ]
    }
)
