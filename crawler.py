import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from rich.console import Console

from lnmu_scraper.parser import extract_links, extract_data
from lnmu_scraper.utils import save_json, save_csv, delay

console = Console()

BASE_URL = "https://www.lnmu.ac.in/acd-faculties"


def run_crawler(output_format="json", headless=False, max_pages=10):
    asyncio.run(_run(output_format, headless, max_pages))


async def _run(output_format, headless, max_pages):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()

        await stealth_async(page)

        console.print("[yellow]Opening main page...[/yellow]")
        await page.goto(BASE_URL)

        html = await page.content()
        links = extract_links(html)[:max_pages]

        console.print(f"[green]Found {len(links)} faculty pages[/green]")

        all_data = []

        for i, link in enumerate(links):
            console.print(f"[cyan]({i+1}) Visiting {link['name']}[/cyan]")

            try:
                await page.goto(link["url"])
                await delay()

                html = await page.content()
                data = extract_data(html, link["name"], link["url"])

                all_data.extend(data)

            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

        console.print(f"[bold green]Collected {len(all_data)} records[/bold green]")

        if output_format in ["json", "both"]:
            save_json(all_data)

        if output_format in ["csv", "both"]:
            save_csv(all_data)

        await browser.close()
