from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:

    research_results = list(
        executor.map(
            research_agent,
            sections
        )
    )