import click
from rich.console import Console
from lnmu_scraper.crawler import run_crawler

console = Console()

@click.command()
@click.option("--output", default="json", help="json / csv / both")
@click.option("--headless", is_flag=True, help="Run browser in headless mode")
@click.option("--max-pages", default=10, help="Limit pages")
def main(output, headless, max_pages):
    console.print("[bold cyan]LNMU Scraper Starting...[/bold cyan]")
    
    run_crawler(
        output_format=output,
        headless=headless,
        max_pages=max_pages
    )

if __name__ == "__main__":
    main()
