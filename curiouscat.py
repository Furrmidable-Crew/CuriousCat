from cat.mad_hatter.decorators import tool
from googlesearch import search


@tool(return_direct=True)
def google_search(query, cat):
    """
    When user asks you to "search on google" always use this tool.
    
    Input is the query.
    """
    # Load settings
    settings = cat.mad_hatter.plugins["curiouscat"].load_settings()
    num_results = settings["number_of_results"]
    lang = settings["language"]

    search_results = search(query, num_results=num_results, lang=lang, advanced=True)
    results_string = ""

    for i, result in enumerate(search_results):
        title = result.title
        url = result.url
        description = result.description

        results_string += f"**Title**: {title}\n**Description**: *{description}*\n**URL**: {url}\n---\n"

    return results_string

