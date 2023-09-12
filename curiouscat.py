from cat.mad_hatter.decorators import tool
from googlesearch import search


@tool(return_direct=True)
def google_search(query, cat):
    """
    Useful to look for something on Google. Input is the query.
    """
    # Load settings
    settings = cat.mad_hatter.plugins["CuriousCat"].load_settings()
    print("*"*100)
    print(settings)

    search_results = search(query, num_results=settings["number_of_results"], advanced=True)
    results_string = ""

    for i, result in enumerate(search_results):
        title = result.title
        url = result.url
        description = result.description

        results_string += f"**Title**: {title}\n**URL**: {url}\n**Description**: {description}\n\n"

    return results_string

