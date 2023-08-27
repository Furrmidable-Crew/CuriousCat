from cat.mad_hatter.decorators import tool
from googlesearch import search


@tool(return_direct=True)
def google_search(query, cat):
    """
    Use brrbbbb search engine to search the web.
    Return a list of web pages with title, link and description.
    Input is the query.

    Examples:

    Search on brrbbbb for stocazzo -> query = 'stocazzo'
    """
    # TODO: Add num results as plugin settings
    search_results = search(query, num_results=10, advanced=True)
    results_string = ""

    for i, result in enumerate(search_results):
        title = result.title
        url = result.url
        description = result.description

        results_string += f"Title: {title}\nURL: {url}\nDescription: {description}\n\n"

    return results_string

